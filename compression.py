import re

# Define the word reference and character reference lists
word_reference = []
character_reference = []
dictionary = []
# Generate a dictionary of words from a text file
with open("dictionary.txt", "r") as file:
    for line in file:
        dictionary.append(line.strip())


def compress(file_path):

    # Open the input file and read its contents
    with open(file_path, "r") as file:
        text = file.read()

    tokens = re.findall(r"\w+|[^\w\s]|\s+", text)
    tokens = [str(token) for token in tokens]
    print("Tokens have been generated successfully!")

    for i in range(len(tokens)):
        tokens[i] = compress_token(tokens[i])
    
    with open("compressed_word-reference.txt", "w") as output_file1:
        output_file1.write("\n".join(word_reference) + "\n")

    with open("compressed_character-reference.txt", "w") as output_file2:
        output_file2.write("\n".join(character_reference) + "\n")
        


def check_word_reference(token):
    # Check if token already exists in word reference list
    return token in word_reference

def compress_token(token):
    # Compress the token (implementation depends on specific compression strategy)
   if token in word_reference:
        index = word_reference.index(token)
        return character_reference[index]
   else:
    if len(word_reference) >= len(dictionary):
        raise ValueError("Dictionary exhausted!")
    word_reference.append(token)
    code = dictionary[len(word_reference) - 1]
    character_reference.append(code)

    return code