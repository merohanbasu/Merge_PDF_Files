import pypdf

# open the pdf file
pdf_path = "Diet.pdf"
pdf_file = open(pdf_path, "rb")  # open the pdf file in binary read mode

# Create an instance or an object
pdf_reader = pypdf.PdfReader(pdf_file)

#number of pages
no_of_pages = len(pdf_reader.pages)
print(no_of_pages)

#individual pages
page = pdf_reader.pages[0]

# text extraction the page
text = page.extract_text()
print(text)

# close the pdf
pdf_file.close()