import PyPDF2
import pdfminer.high_level


filename = "Design brief - 20052020 - Wikipedia.pdf"
# filename = "Natural Language Processing with Python.pdf"

with open(filename, "rb") as file:

    # pdf = PyPDF2.PdfFileReader(file)
    
    text = pdfminer.high_level.extract_text(file)
    print(text)
