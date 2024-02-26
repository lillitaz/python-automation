import PyPDF2
import re

# Open the PDF file in read-binary mode
with open("/home/user/Documents/test.pdf", "rb") as file:
    # Create a PDF object using PdfReader
    pdf = PyPDF2.PdfReader(file)

    # Initialize an empty string to store the extracted text
    text = ""

    # Loop through each page and extract text
    for page in pdf.pages:
        text += page.extract_text()

# Use regular expression to find all occurrences of "ich"
matches = re.findall("test", text)

# Print the number of occurrences found
print("Found", len(matches), "occurrences of 'test' in the PDF file")
