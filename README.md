# Text Compression

Text Compression is a simple python utility that was made to compress large .txt files into a much smaller encoded format, such that I can store large chunks of text in a compact fashion.

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

After, the program will prompt you for the next steps!

## Generated Files
Compression Produces three distinct files:
|File|Description|
|---|---|
|compressed_data.txt|Contains the compacted, encoded text.|
|compressed_word-reference.txt|Stores the original reference tokens.|
|compressed_character-reference.txt|Stores the corresponding character codes.|

# The Development Process
## Coming Up with the Idea
So I came up with the idea around ~2 weeks ago, in which I wanted to build a Scratch project that could store the entirity of the english Bible locally.  But due to being on a OSWars team that directly faced the strict project.json limits of Scratch project, I knew compression was required.  Thus, I began researching compression algorithms, but then, in a CS50 lecture about C dictionaries, I had the bright idea, "Wait, why not just make a literal dictionary with single character tokens?"  And, that idea made this project.  

## What was Challenging or New?
There were certainly some new things I had to learn with this project, such as how to properly manage loaded files, terminal text color with colorama, and finally, how to compile project using pyinstaller while including something like dictionary.txt