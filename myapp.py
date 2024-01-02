from PyPDF2 import PdfReader
from transformers import GPT2Tokenizer, GPT2LMHeadModel

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

# Load the fine-tuned model
model_directory = "your_trained_model_directory"
model = GPT2LMHeadModel.from_pretrained(model_directory)
tokenizer = GPT2Tokenizer.from_pretrained(model_directory)
model.eval()

# Generate responses using the raw text
def generate_response_from_text(text, max_length=100, num_return_sequences=1):
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate responses using the model
    output = model.generate(
        input_ids,
        max_length=50000,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )

    # Decode the generated responses
    decoded_responses = [tokenizer.decode(output_seq, skip_special_tokens=True) for output_seq in output]

    return decoded_responses

# Example usage
responses = generate_response_from_text(raw_text)

# Print the generated responses
for i, response in enumerate(responses):
    print(f"Response {i + 1}: {response}")



