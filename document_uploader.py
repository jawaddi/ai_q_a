from PyPDF2 import PdfReader
def load_documents(uploaded_files):
    documents = []
    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8")
            documents.append({"text": text, "source": uploaded_file.name})
        elif uploaded_file.name.endswith(".pdf"):
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append({"text": text, "source": uploaded_file.name})
    return documents