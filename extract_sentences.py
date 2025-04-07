import nltk
import os
import string

import pandas as pd

# import nltk
# nltk.download('popular')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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

