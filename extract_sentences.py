import os
import string

import pandas as pd

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download the required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('popular')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Step 1: Load the text files
def load_text_files(directory: str):
    """
    Load text files from a directory and return their content as a dictionary.
    
    Args:
        directory (str): The path to the directory containing text files.
        
    Returns:
        dict: A dictionary where keys are file names and values are file contents.
    """
    text_files = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text_files[filename] = file.read()
    return text_files

# Test the load_text_files function
directory = "/Users/sxmmy/Documents/Projects/Eigen/Eigen" # Replace with your directory path
text_files = load_text_files(directory)
# print(text_files)

# Step 2: Process text to remove line breaks, escape characters, and extra spaces.
def process_text(text: str):
    """
    Clean the text by removing unwanted characters and extra spaces,
    while preserving sentence structure (full stops remain, stopwords are not removed).
    
    Args:
        text (str): The original text.
        
    Returns:
        str: The cleaned text with sentences preserved.
    """
    # Remove '\n' and escape characters
    text = text.replace('\n', ' ').replace('\\', '').replace('\'', '')

    # Remove extra spaces
    text = ' '.join(text.split())

    # Convert to lowercase
    # text = text.lower()

    # Remove punctuation except full stops, commas, exclamation marks, question marks, colons, and semicolons
    text = ''.join([char for char in text if char not in string.punctuation or char in {'.', ',', '!', '?', ':', ';'}]) 

    # Remove extra spaces again
    text = text.replace('  ','')

    return text

# Test the process_text function
# processed_text = process_text(text_files['doc6.txt'])
# Print the processed text
# print(processed_text)

# Step 3: Score sentences
def score_sentences(text: str, word_frequencies: dict, top_n: int = 3):
    """
    Score sentences based on the importance of the words they contain.
    
    Args:
        text (str): The cleaned text with sentences preserved.
        word_frequencies (dict): A dictionary of word frequencies.
        top_n (int): The number of top sentences to extract.
        
    Returns:
        list: A list of the top N most important sentences.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Calculate sentence scores
    sentence_scores = []
    for sentence in sentences:
        score = 0
        words = sentence.split()  # Split sentence into words
        for word in words:
            if word in word_frequencies:
                score += word_frequencies[word]
        sentence_scores.append((sentence, score))
    
    # Sort sentences by score in descending order
    sorted_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)
    
    # Extract the top N sentences
    top_sentences = [sentence for sentence, score in sorted_sentences[:top_n]]
    
    return top_sentences

# Test the score_sentences function

# Step 4: Create a summary table with context
def create_summary_table(text_files: dict, top_n_sentences: int = 3):
    """
    Create a summary table with word frequencies and top sentences for context.
    
    Args:
        text_files (dict): A dictionary where keys are file names and values are file contents.
        top_n_sentences (int): The number of top sentences to extract for context.
        
    Returns:
        pd.DataFrame: A DataFrame containing the summary table.
    """
    # Dictionary to store word frequencies for all documents
    all_word_frequencies = {}
    # Dictionary to store top sentences for all documents
    all_top_sentences = {}

    # Process each document
    for filename, content in text_files.items():
        # Step 1: Clean the text
        cleaned_text = process_text(content)
        
        # Step 2: Calculate word frequencies
        word_frequencies = {}
        for word in cleaned_text.split():
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
        all_word_frequencies[filename] = word_frequencies
        
        # Step 3: Extract top sentences
        top_sentences = score_sentences(content, word_frequencies, top_n=top_n_sentences)
        all_top_sentences[filename] = top_sentences

    # Step 5: Combine results into a summary table
    summary_data = []
    unique_words = set(word for freqs in all_word_frequencies.values() for word in freqs.keys())
    
    for word in unique_words:
        row = {"Word": word, "Total Occurrences": sum(freqs.get(word, 0) for freqs in all_word_frequencies.values())}
        for filename in text_files.keys():
            # Add top sentences containing the word for each document
            sentences_with_word = [sentence for sentence in all_top_sentences[filename] if word in sentence]
            row[filename] = " | ".join(sentences_with_word[:top_n_sentences])  # Join top sentences with '|'
        summary_data.append(row)

    # Convert to DataFrame
    summary_table = pd.DataFrame(summary_data)
    return summary_table

# Main Execution
directory = "/Users/sxmmy/Documents/Projects/Eigen/Eigen"  # Replace with your directory path
text_files = load_text_files(directory)

# Create the summary table
summary_table = create_summary_table(text_files, top_n_sentences=3)

# Save the summary table to a CSV file
summary_table.to_csv('extract_sentences.csv', index=False)
print("Summary table saved to 'extract_sentences.csv'")