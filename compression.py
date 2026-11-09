import os
import re

# Load character dictionary
dictionary = []

with open("dictionary.txt", "r", encoding="utf-8") as file:
    dictionary = [line.rstrip("\r\n") for line in file if line.rstrip("\r\n")]


def compress_token(token, references):

    # Reuse an existing code if the token was already encountered
    if token in references:
        return references[token]

    # Check dictionary capacity
    if len(references) >= len(dictionary):
        raise ValueError("Dictionary exhausted!")

    # Assign a new code
    code = dictionary[len(references)]
    references[token] = code

    return code


def compress(file_path):

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

    # Write compressed data
    with open("compressed_data.txt", "w", encoding="utf-8") as file:
        file.write("".join(compressed_tokens))

    # Write original word references
    with open("compressed_word-reference.txt", "w", encoding="utf-8") as file:
        for word in word_reference:
            file.write(repr(word) + "\n")

    # Write character references
    with open("compressed_character-reference.txt", "w", encoding="utf-8") as file:
        for code in word_reference.values():
            file.write(code + "\n")

    print("Compression completed successfully!")
    print(f"Unique tokens: {len(word_reference)}")
    print("Generated:")
    print("- compressed_data.txt")
    print("- compressed_word-reference.txt")
    print("- compressed_character-reference.txt")
    print()
    print(f"Comparing to original file size...")
    compare_file_sizes(file_path, "compressed_data.txt")

def compare_file_sizes(original_file, compressed_file):
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)

    print(f"Original file size: {original_size} bytes")
    print(f"Compressed file size: {compressed_size} bytes")

    percentage = (compressed_size / original_size) * 100 if original_size > 0 else 0
    print(f"Compressed file is {percentage:.2f}% of the original file size.")


