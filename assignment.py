# Sirion Eigen Coding Assignment
# This script aims to extract a word, sentence or paragraph from a text file based on user input. A list of the most frequent interesting words, along with a summary table showing where those words are located in the text, is also generated. 
# The script uses the Spacy library for natural language processing and the Pandas library for data manipulation and visualization.

import nltk
import os
import string

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
directory = "/Users/sxmmy/Documents/Projects/Eigen/Eigen"
text_files = load_text_files(directory)
 # print(text_files)

