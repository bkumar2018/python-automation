import PyPDF2

# Open the PDF file
pdf_file = open('sampledata.pdf', 'rb')

# Initialize PDF reader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from all pages
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    print(page.extract_text())

pdf_file.close()
