import os

def decompress():
    # Load Tokens
    with open("compressed_word-reference.txt", "r", encoding="utf-8") as file:
            words = [line.rstrip("\r\n") for line in file]

    with open("compressed_character-reference.txt", "r", encoding="utf-8") as file:
            codes = [line.rstrip("\r\n") for line in file]

    # Validate that the number of words and codes match
    if len(words) != len(codes):
        print("Error: The number of words and codes do not match.")
        print(f"Words: {len(words)}, Codes: {len(codes)}")
        print("Please try compresing your file again.")
        return

    references = dict(zip(codes, words))

    