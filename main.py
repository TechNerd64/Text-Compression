
import os
import sys
import hashlib
import compression
import decompression
from colorama import Fore, just_fix_windows_console, init

init(autoreset=True, strip=False)
just_fix_windows_console()
ORANGE_RGB = '\033[38;2;255;165;0m'

def main():
    print(f"Welcome to the Text Compression by{ORANGE_RGB} TechNerd64" + Fore.RESET)

    while True:
        operation = input("Enter operation (compress/decompress/compare/help): ").strip().lower()
        if operation in ["compress", "decompress", "compare", "help"]:
            break
        else:
            print(Fore.RED + "Invalid operation. Please try again!")
            continue

    if operation == "compress":
        while True:
            file_path = input("Enter the path of the text file to compress: ").strip()

            if os.path.isfile(file_path):
                if not file_path.lower().endswith(".txt"):
                    print(Fore.RED + "Error: The file must be a .txt file. Please try again.")
                    continue
                else:
                    break
            else:
                print(Fore.RED + "Invalid file path. Please try again.")

        compression.compress(os.path.abspath(file_path))

    elif operation == "decompress":
        decompression.decompress()

    elif operation == "compare":
        original_file = input("Enter the path of the original text file: ").strip()
        compressed_file = input("Enter the path of the decompressed data file: ").strip()

        if os.path.isfile(original_file) and os.path.isfile(compressed_file):
            file1 = get_hash(original_file)
            file2 = get_hash(compressed_file)

            if file1 == file2:
                print(Fore.GREEN + "The files are identical.")
            else:
                print(Fore.RED + "The files are different.")

        else:
            print(Fore.RED + "One or both file paths are invalid. Please try again.")

    elif operation == "help":
        print("Available operations:")
        print("- compress: Compress a text file.")
        print("- decompress: Decompress the previously compressed data.")
        print("- compare: Compare the original and decompressed files for integrity.")
        print("- help: Shows this help message ;)")


def get_hash(file_path):
    ## Calculate the SHA-256 hash of a file
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


def get_path(relative_path):
    # Check if running as a compiled PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)


if __name__ == "__main__":
    main()
