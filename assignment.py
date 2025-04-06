# Sirion Eigen Coding Assignment
# This script aims to extract a word, sentence or paragraph from a text file based on user input. A list of the most frequent interesting words, along with a summary table showing where those words are located in the text, is also generated. 
# The script uses the Spacy library for natural language processing and the Pandas library for data manipulation and visualization.

import nltk
import os
import string

import pandas as pd

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
# directory = "/Users/sxmmy/Documents/Projects/Eigen/Eigen" # Replace with your directory path
# text_files = load_text_files(directory)
 # print(text_files)

# Step 2: Process the text to remove punctuation
def process_text(text: str):
    """
    Remove punctuation from the text and return the cleaned text.
    
    Args:
        text (str): The original text.
        
    Returns:
        str: The cleaned text without punctuation.
    """
    # Remove '\n' and escape characters
    text = text.replace('\n', ' ').replace('\\', '').replace('\'', '')

    # Remove extra spaces
    text = ' '.join(text.split())

    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])

    return text

# Test the process_text function
# processed_text = process_text(text_files['doc6.txt'])

# Print the processed text
# print(processed_text)

# Step 3: Tokenize the text into words
def tokenize_text(text: str):
    """
    Tokenize the text into words.
    
    Args:
        text (str): The cleaned text.
        
    Returns:
        list: A list of tokens (words).
    """
    tokens = text.split()
    return tokens

# Test the tokenize_text function
# tokens = tokenize_text(processed_text)
# print(tokens)

# Step 4: Count the frequency of each word in a document
def count_word_frequency(tokens: list):
    """
    Count the frequency of each word in the tokenized text.
    
    Args:
        tokens (list): A list of tokens (words).
        
    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    word_frequency = {}
    for word in tokens:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

# Test the count_word_frequency function
# word_frequency = count_word_frequency(tokens)
# print(word_frequency)

# Identify interesting words based on frequency
# def identify_interesting_words(word_frequency: dict, threshold: int = 2):
#     """
#     Identify interesting words based on their frequency.
    
#     Args:
#         word_frequency (dict): A dictionary of word frequencies.
#         threshold (int): The frequency threshold for interesting words.
        
#     Returns:
#         list: A list of interesting words.
#     """
#     interesting_words = [word for word, freq in word_frequency.items() if freq >= threshold]
#     return interesting_words

# Test the identify_interesting_words function
# interesting_words = identify_interesting_words(word_frequency)
# print(interesting_words)

# Step 5: Create a summary table for all documents
def create_summary_table(all_word_frequencies: dict):
    """
    Create a summary table of word frequencies across all documents.
    
    Args:
        all_word_frequencies (dict): A dictionary where keys are file names and values are word frequency dictionaries.
        
    Returns:
        pd.DataFrame: A DataFrame containing the summary table.
    """
    summary_data = []
    for filename, word_freq in all_word_frequencies.items():
        for word, frequency in word_freq.items():
            summary_data.append({
                'Word': word,
                'Frequency': frequency,
                'Document': filename
            })
    
    return pd.DataFrame(summary_data)

# Test the create_summary_table function
# summary_table = create_summary_table(word_frequency, interesting_words)
# print(summary_table)

# Main Execution
directory = "/Users/sxmmy/Documents/Projects/Eigen/Eigen"  # Replace with your directory path
text_files = load_text_files(directory)

# Step 7: Process each file and calculate word frequencies
all_word_frequencies = {}
for filename, content in text_files.items():
    processed_text = process_text(content)
    tokens = tokenize_text(processed_text)
    word_frequency = count_word_frequency(tokens)
    all_word_frequencies[filename] = word_frequency

# Step 8: Create the summary table
summary_table = create_summary_table(all_word_frequencies)

# Step 9: Save the summary table to a CSV file
summary_table.to_csv('word_frequencies.csv', index=False)
print("Summary table saved to 'word_frequencies.csv'")

# # Step 7: Save the summary table to a CSV file
# def save_summary_table(summary_table: pd.DataFrame, filename: str):
#     """
#     Save the summary table to a CSV file.
    
#     Args:
#         summary_table (pd.DataFrame): The DataFrame containing the summary table.
#         filename (str): The name of the CSV file to save.
#     """
#     summary_table.to_csv(filename, index=False)

# # Test the save_summary_table function
# save_summary_table(summary_table, 'summary_table.csv')