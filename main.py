import os 
import sys
import compression
import decompression

def main():
    operation = input("Enter operation (compress/decompress): ").strip().lower()
    if operation == "compress":
        file_path = input("Enter the path to the input file: ").strip()
        # Validate input
        if not os.path.isfile(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return
        if not file_path.endswith('.txt'):
            print("Error: Input file must be a .txt file.")
            return
        compression.compress(file_path)
    elif operation == "decompress":
        decompression.decompress()


if __name__ == "__main__":
    main()