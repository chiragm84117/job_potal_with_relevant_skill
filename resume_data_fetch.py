import PyPDF2 as pdf

def input_pdf_text(uploaded_file):
    with open(uploaded_file, 'rb') as file:
        reader = pdf.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text