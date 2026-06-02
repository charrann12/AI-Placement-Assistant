from langchain_community.document_loaders import PyPDFLoader

def load_pdf(uploaded_resume):

    temp_pdf = "./temp.pdf"

    with open(temp_pdf, "wb") as file:
        file.write(uploaded_resume.getvalue())

    loader = PyPDFLoader(temp_pdf)

    return loader.load()

