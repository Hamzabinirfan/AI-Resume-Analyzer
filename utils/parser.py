from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if not text:
            print(f"Warning: No text extracted from {uploaded_file.name}")
        return text
    except Exception as e:
        print(f"Error reading {uploaded_file.name}: {e}")
        return ""
