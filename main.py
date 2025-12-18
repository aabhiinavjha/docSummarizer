import sys
from src.reader import read_document
from src.summarizer import summarize


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <document>")
        exit(1)

    text = read_document(sys.argv[1])
    summary = summarize(text)

    print("\n----- SUMMARY -----\n")
    print(summary)
