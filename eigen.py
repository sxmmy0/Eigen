# Sirion Eigen Coding Assignment
# This script aims to extract a word, sentence or paragraph from a text file based on user input. A list of the most frequent interesting words, along with a summary table showing where those words are located in the text, is also generated. 
# The script uses the Spacy library for natural language processing and the Pandas library for data manipulation and visualization.

import os
# import spacy
import pandas as pd
from collections import Counter
from typing import List, Tuple, Dict

# Load the English NLP model from Spacy
# nlp = spacy.load("en_core_web_sm")

# 1. Function to read the text file and return its content
def load_text_files(directory: str) -> Dict[str, str]:
    """
    Load text files from a directory and return their content as a dictionary.
    
    Args:
        directory (str): The path to the directory containing text files.
        
    Returns:
        Dict[str, str]: A dictionary where keys are file names and values are file contents.
    """
    text_files = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text_files[filename] = file.read()
    return text_files

# 2. Function to remove punctuation from a text.
def process_text(text: str) -> str:
    """
    Remove punctuation from the text and return the cleaned text.
    
    Args:
        text (str): The original text.
        
    Returns:
        str: The cleaned text without punctuation.
    """
    # doc = nlp(text.lower())
    # tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    # return tokens