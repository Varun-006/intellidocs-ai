
from pdf_reader import extract_text

pdf_path = input("Enter the path to your PDF file: ")

try:
    text = extract_text(pdf_path)

    if text.strip():
        print("\n--- Extracted PDF Text ---\n")
        print(text[:2000])
    else:
        print("No extractable text found in this PDF.")

except Exception as error:
    print(f"Could not read PDF: {error}")
