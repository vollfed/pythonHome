from tika import parser

raw = parser.from_file('test.pdf')
print(raw['content'])


# import PyPDF2
# pdf_file = open('test.pdf', 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(0)
# page_content = page.extractText()
# print (page_content.encode('utf-8'))