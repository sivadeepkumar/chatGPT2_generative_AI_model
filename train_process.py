from PyPDF2 import PdfReader
# List of PDF filenames

pdf_filenames = ["one.pdf","two.pdf","three.pdf","four.pdf","five.pdf",]   # "one.pdf","two.pdf","three.pdf","four.pdf","five.pdf","six.pdf","seven.pdf","eight.pdf","nine.pdf","ten.pdf","a.pdf","b.pdf","c.pdf","d.pdf","e.pdf","f.pdf","g.pdf","h.pdf","i.pdf","j.pdf","k.pdf","l.pdf"

raw_text = ""

# Loop through PDFs and extract text
for pdf_filename in pdf_filenames:
    pdfreader = PdfReader(pdf_filename)
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content


# print(raw_text)


# Save the extracted text to a file
with open("preprocessed_data.txt", "w", encoding="utf-8") as file:
    file.write(raw_text)
