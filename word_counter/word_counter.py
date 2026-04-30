import os

def count_words(file):
    file = os.path.abspath(file)
    print(file)
    if not os.path.isfile(file) or file[-4:] != ".txt":
        print("Invalid File")
        return 0
    
    try:
        with open(file, "r") as fhand:
            text = fhand.read()
            count = len(text.split())
    except FileNotFoundError as e:
        print("File could not be opened: ", e)
        return 0

    return count

def main():
    file = input("Please enter file name (MUST BE TXT): ").lower()
    print(f"Word Count: {count_words(file)}")

main()