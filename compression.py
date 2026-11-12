
import os
import sys
import re
from colorama import Fore, Style, Back, just_fix_windows_console, init

# Initialize colorama for Windows compatibility
just_fix_windows_console()
## start color auto reset
init(autoreset=True, strip=False)


def get_path(relative_path):
    # Check if running as a compiled PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


def output_path(relative_path):
    # Get the directory containing the executable or script
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


# Load character dictionary
dictionary = []

with open(get_path("dictionary.txt"), "r", encoding="utf-8") as file:
    dictionary = [line.rstrip("\r\n") for line in file if line.rstrip("\r\n")]


def compress_token(token, references):

    # Reuse an existing code if the token was already encountered
    if token in references:
        return references[token]

    # Check dictionary capacity
    if len(references) >= len(dictionary):
        raise ValueError(Fore.RED + "Dictionary exhausted!" + Style.RESET_ALL)

    # Assign a new code
    code = dictionary[len(references)]
    references[token] = code

    return code


def compress(file_path):

    # Convert input path to absolute path
    file_path = os.path.abspath(file_path)

    # Store token-to-code references
    word_reference = {}

    # Read input file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Split text into words, punctuation, and whitespace
    tokens = re.findall(r"\w+|[^\w\s]|\s+", text)
    print(f"Dictionary entries: {len(dictionary)}")
    print(f"Generated {len(tokens)} tokens.")

    # Compress tokens
    compressed_tokens = []

    for token in tokens:
        compressed_tokens.append(compress_token(token, word_reference))

    # Define output file paths
    compressed_file = output_path("compressed_data.txt")
    word_reference_file = output_path("compressed_word-reference.txt")
    character_reference_file = output_path("compressed_character-reference.txt")

    # Write compressed data
    with open(compressed_file, "w", encoding="utf-8") as file:
        file.write("".join(compressed_tokens))

    # Write original word references
    with open(word_reference_file, "w", encoding="utf-8") as file:
        for word in word_reference:
            file.write(repr(word) + "\n")

    # Write character references
    with open(character_reference_file, "w", encoding="utf-8") as file:
        for code in word_reference.values():
            file.write(code + "\n")

    print(Fore.GREEN + "Compression completed successfully!")
    print(f"Unique tokens: {len(word_reference)}")
    print("Generated:")
    print("- compressed_data.txt")
    print("- compressed_word-reference.txt")
    print("- compressed_character-reference.txt" + "\n")
    print("Comparing to original file size...")

    compare_file_sizes(
        file_path,
        compressed_file,
        word_reference_file,
        character_reference_file
    )


def compare_file_sizes(original_file, compressed_file, word_reference_file, character_reference_file):
    if not all(os.path.isfile(path) for path in [original_file, compressed_file, word_reference_file, character_reference_file]):
        print(Fore.RED + "Error: One or more file paths are invalid. Cannot compare sizes.")
        return

    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file) + os.path.getsize(word_reference_file) + os.path.getsize(character_reference_file)

    print(f"Original file size: {original_size} bytes")
    print(f"Compressed file size: {compressed_size} bytes")

    percentage = (compressed_size / original_size) * 100 if original_size > 0 else 0

    if percentage < 100:
        print(f"Compressed file is " + Fore.GREEN + f"{percentage:.2f}%" + Style.RESET_ALL + " of the original file size.")
    elif percentage == 100:
        print(f"Compressed file is " + Fore.YELLOW + f"{percentage:.2f}%" + Style.RESET_ALL + " of the original file size.")
    else:
        print(f"Compressed file is " + Fore.RED + f"{percentage:.2f}%" + Style.RESET_ALL + " of the original file size.")
