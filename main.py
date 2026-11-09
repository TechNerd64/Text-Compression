import os 
import sys
import compression
import decompression

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <file_path>")
        return

    file_path = sys.argv[1]
    # Validate input
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    if not file_path.endswith('.txt'):
        print("Error: Input file must be a .txt file.")
        return
    operation = input("Enter operation (compress/decompress): ").strip().lower()
    
    try:
        if operation == "compress":
            compression.compress(file_path)
        elif operation == "decompress":
            decompression.decompress(file_path)
    except Exception as error:
        print(f"An error occurred: {error}")
        return


if __name__ == "__main__":
    main()