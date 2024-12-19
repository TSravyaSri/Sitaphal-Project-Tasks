from flask import Flask, render_template, request, redirect, url_for
import os
import spacy
import pytesseract
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import re

app = Flask(__name__)

# Configure the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Load the spaCy language model
nlp = spacy.load("en_core_web_md")  # Using a medium-sized model for better word vectors

def clean_text(text):
    text = re.sub(r"[©®™~”“]", "", text)  # Remove copyright, trademarks, and special quotes
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces/newlines with a single space
    return text.strip()

def extract_text_from_pdf(pdf_path):
    full_text = ""

    # First attempt: Extract text using PyPDF2
    try:
        reader = PdfReader(pdf_path)
        pdf_text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
        full_text += pdf_text
    except Exception as e:
        print(f"Error reading PDF: {e}")

    # Second attempt: Extract text using OCR (if necessary)
    try:
        images = convert_from_path(pdf_path)
        ocr_text = ""
        for image in images:
            ocr_text += pytesseract.image_to_string(image, config="--psm 6")
        full_text += ocr_text
    except Exception as e:
        print(f"Error with OCR: {e}")

    return clean_text(full_text)

def remove_unwanted_section(text, unwanted_keywords):
    for keyword in unwanted_keywords:
        pattern = rf"(?i){keyword}.*?(\n[A-Z][A-Za-z ]+\n|$)"  # Matches the unwanted section, stopping at the next header
        text = re.sub(pattern, "", text)
    
    return text

def extract_query_section(text, query):
    doc = nlp(text)
    query_doc = nlp(query)
    related_sentences = []
    query_found = False
    next_sentences = []
    unwanted_keywords = ["Key Responsibilities", "Qualifications", "Skills", "Education", "Experience", "Benefits"]
    
    for i, sent in enumerate(doc.sents):
        if query.lower() in sent.text.lower() and not query_found:
            related_sentences.append(sent.text.strip())
            query_found = True
            next_sentences = [sent.text.strip() for sent in list(doc.sents)[i+1:i+4]]
            break

    extracted_text = " ".join(related_sentences + next_sentences)
    extracted_text = remove_unwanted_section(extracted_text, unwanted_keywords)
    
    return clean_text(extracted_text)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        query = request.form['query']
        
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            print("Extracting text from the PDF...")
            text = extract_text_from_pdf(filename)

            print(f"Extracting information related to the query: '{query}'...")
            query_section = extract_query_section(text, query)

            return render_template('index.html', query_section=query_section)

    return render_template('index.html', query_section=None)

if __name__ == "__main__":
    app.run(debug=True)
