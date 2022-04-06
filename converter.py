from pdf2docx import Converter

pdf_file = 'cover letter.pdf'

docx_file = 'output.docx'

c = Converter(pdf_file)
c.convert(docx_file)
c.close()