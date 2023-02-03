import PyPDF2

password=open('dictionnary.txt')
password=password.read()
password=password.split('\n')

pdf = open('encrypted.pdf', 'rb')
pdf_reader=PyPDF2.PdfFileReader(pdf)
pdf_writer=PyPDF2.PdfFileWriter()

for words in password:
    try:
        if pdf_reader.decrypt(words)==1:
            print("The password is " + words + '!!')
    except:
        print("Password not found...")

for num_page in range(pdf_reader.numPages):
    page_obj = pdf_reader.getPage(num_page)
    pdf_writer.addPage(page_obj)

newPdf=open('Topsecrect.pdf', 'wb')
pdf_writer.write(newPdf)
newPdf.save()
newPdf.close()
pdf.close()