import ast
import sys
import os
from colorama import Fore, Style, Back, just_fix_windows_console, init
# Initialize colorama for Windows compatibility
just_fix_windows_console()
init(autoreset=True)

def load_references():
    # Check file existence
    if not os.path.isfile(get_path("compressed_word-reference.txt")) or not os.path.isfile(get_path("compressed_character-reference.txt")):
        print(Fore.RED + "Error: Reference files not found. Please ensure that 'compressed_word-reference.txt' and 'compressed_character-reference.txt' exist in the current directory.")
        return None

    # Load Tokens
    with open(get_path("compressed_word-reference.txt"), "r", encoding="utf-8") as file:
            words = [ast.literal_eval(line) for line in file]

    with open(get_path("compressed_character-reference.txt"), "r", encoding="utf-8") as file:
            codes = [line.rstrip("\r\n") for line in file]

    # Validate that the number of words and codes match
    if len(words) != len(codes):
        print(Fore.RED + "Error: The number of words and codes do not match.")
        print(f"Words: {len(words)}, Codes: {len(codes)}")
        print("Please try compresing your file again.")
        return

    references = dict(zip(codes, words))

    return references

def decompress():
    # Load references
    references = load_references()
    if references is None:
        print(Fore.RED + "Decompression aborted due to reference loading error.")
        return

    if not os.path.isfile(get_path("compressed_data.txt")):
        print(Fore.RED + "Error: Compressed data file 'compressed_data.txt' not found. Please ensure that the file exists in the current directory.")
        return
    # Read compressed data
    with open(get_path("compressed_data.txt"), "r", encoding="utf-8") as file:
         compressed_data = file.read()

    print(f"Loaded {len(references)} references.")
    print(f"Compressed data contains {len(compressed_data)} characters.")

    # Decode compressed data
    decompressed_tokens = []

    for character in compressed_data:
        if character not in references:
            print(Fore.RED + "Error: Compressed data contains a character not found in the references.")
            return
        decompressed_tokens.append(references[character])

    #reconstruct the original text
    decompressed_text = "".join(decompressed_tokens)

    # Write decompressed data
    with open("decompressed_data.txt", "w", encoding="utf-8") as file:
        file.write(decompressed_text)

    print(Fore.GREEN + "Decompression completed successfully!")
    print(f"Recovered {len(decompressed_text)} tokens.")
    print("Decompressed data written to 'decompressed_data.txt'.")

def get_path(relative_path):
    # Check if running as a compiled PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)