# Word Counter

A simple Python utility to count the number of words in a text file.

## Features

- Reads `.txt` files and counts total words
- Validates file existence and format
- Handles errors gracefully with informative messages
- Supports both relative and absolute file paths

## Usage

Run the program:
```bash
python word_counter.py
```

When prompted, enter the file path (must be a `.txt` file):
```
Please enter file name (MUST BE TXT): example.txt
Word Count: 42
```

## Requirements

- Python 3.x
- No external dependencies

## How It Works

1. Prompts user to input a file path
2. Validates that the file exists and has a `.txt` extension
3. Reads the file and counts words (separated by whitespace)
4. Displays the total word count

## Error Handling

- **Invalid File**: Shown if file doesn't exist or doesn't have `.txt` extension
- **File could not be opened**: Shown if there's an error reading the file (permissions, encoding, etc.)

## Example

```
Please enter file name (MUST BE TXT): example.txt
Word Count: 156
```
