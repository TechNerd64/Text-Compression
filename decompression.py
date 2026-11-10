import ast

def load_references():
    # Load Tokens
    with open("compressed_word-reference.txt", "r", encoding="utf-8") as file:
            words = [ast.literal_eval(line) for line in file]

    with open("compressed_character-reference.txt", "r", encoding="utf-8") as file:
            codes = [line.rstrip("\r\n") for line in file]

    # Validate that the number of words and codes match
    if len(words) != len(codes):
        print("Error: The number of words and codes do not match.")
        print(f"Words: {len(words)}, Codes: {len(codes)}")
        print("Please try compresing your file again.")
        return

    references = dict(zip(codes, words))

    return references

def decompress():
    # Load references
    references = load_references()
    if references is None:
        print("Decompression aborted due to reference loading error.")
        return

    # Read compressed data
    with open("compressed_data.txt", "r", encoding="utf-8") as file:
         compressed_data = file.read()

    print(f"Loaded {len(references)} references.")
    print(f"Compressed data contains {len(compressed_data)} characters.")

    # Decode compressed data
    decompressed_tokens = []

    for character in compressed_data:
        if character not in references:
            raise ValueError("Error: Compressed data contains a character not found in the references.")
        decompressed_tokens.append(references[character])

    #reconstruct the original text
    decompressed_text = "".join(decompressed_tokens)

    # Write decompressed data
    with open("decompressed_data.txt", "w", encoding="utf-8") as file:
        file.write(decompressed_text)

    print("Decompression completed successfully!")
    print(f"Recovered {len(decompressed_text)} tokens.")
    print("Decompressed data written to 'decompressed_data.txt'.")
