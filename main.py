import os 
import sys
import compression

def main():
    if len(sys.argv < 2):
        print("Usage: python main.py <file_path>")
        return

    operation  = sys.argv[1]
    file_path = sys.argv[2]

    # Validate input
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    if not file_path.endswith('.txt'):
        print("Error: Input file must be a .txt file.")
        return

    try:
        if operation == "compress":
            compression.compress(file_path)
        else:
            print("Error: Invalid operation. Use 'compress' to compress the file.")

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()