# docSummarizer

Simple document summarizer project.

Project layout

docSummarizer/
- src/
  - reader.py        # read txt/pdf/docx
  - summarizer.py    # clustering + ranking
  - __init__.py
- main.py            # CLI entry point
- requirements.txt
- README.md
- sample/
  - example.txt

Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the CLI on a document:

```bash
python3 main.py sample/example.txt
```
