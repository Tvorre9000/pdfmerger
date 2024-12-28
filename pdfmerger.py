from PyPDF2 import PdfMerger

# TODO: add support for partial file concatenations

# Implement prompt to select files and arrange order of the files
pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()