import os
import sys
import re

def compress(file_path):
    # Open the input file and read its contents
    with open(file_path, "r") as file:
        text = file.read()

    tokens = re.findall(r"\w+|[^\w\s]|\s+", text)

    print(tokens)

