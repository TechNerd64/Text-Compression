# Text Compression

Text Compression is a simple python utility that was made to compress large .txt files into a much smaller format, such that I can store large chunks of text in a compact fashion.

## Features
 - Compression: Encoded text into compact character codes using a pre-defined of over 50,000 possible token values.
 - Decompression:  Lossless reconstrucion of the compacted, encoded text using reference files.
 - File Comparison:  Uses SHA-256 hashing to validate two files are identical.
 - Size Comparison:  Displays the compressed file size of the main compacted data (not including the reference lists) relative to the source file.

 ## Installation
Clone the repository:

```bash
git clone https://github.com/TechNerd64/Text-Compression.git
cd Text-Compression
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage
Start the program:
```bash
python main.py
```
Then choose one of the avaliable operations when prompted:
| Operation | Description |
|---|---|
|compress|Compresses a .txt file.|
|decompress|Restores a previously compressed file.|
|compare|Compare two files using SHA-256 hashes.|

## Generated Files
Compression Produces three distinct files:
|File|Description|
|---|---|
|compressed_data.txt|Contains the compacted, encoded text.|
|compressed_word-reference.txt|Stores the original reference tokens.|
|compressed_character-reference.txt|Stores the corresponding character codes.|