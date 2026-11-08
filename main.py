import os 
import sys
import compression

def main():
    if len(sys.argv) < 2:
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

    try:
        compression.compress(file_path)
    except Exception as error:
        print(f"An error occurred: {error}")
        return


if __name__ == "__main__":
    main()