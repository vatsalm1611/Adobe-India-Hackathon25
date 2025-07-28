import fitz  # PyMuPDF
import os
import json
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(file_path, output_path):
    doc = fitz.open(file_path)
    outline = extract_outline(doc)
    with open(output_path, "w") as f:
        json.dump(outline, f, indent=2)

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            process_pdf(input_path, output_path)

if __name__ == "__main__":
    main()
