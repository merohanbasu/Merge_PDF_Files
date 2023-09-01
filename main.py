import pypdf

# open the pdf's
pdf1 = open("1.pdf", "rb")
pdf2 = open("2.pdf", "rb")

# create instances for reader
pdf_reader1 = pypdf.PdfReader(pdf1)
pdf_reader2 = pypdf.PdfReader(pdf2)

# create instance for writer
pdf_writer = pypdf.PdfWriter()

# add pages
for i in range(len(pdf_reader1.pages)):
    page = pdf_reader1.pages[i]
    pdf_writer.add_page(page)

for i in range(len(pdf_reader2.pages)):
    page = pdf_reader2.pages[i]
    pdf_writer.add_page(page)

# save and merge pdf's
#open the final pdf
merged_pdf = open("merged_pdf.pdf", "wb")
#add the merged pdf to the final pdf
pdf_writer.write(merged_pdf)

# close all the input and output files
pdf1.close()
pdf2.close()
merged_pdf.close()
