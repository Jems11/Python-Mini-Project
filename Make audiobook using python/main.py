from PyPDF2 import pdf
import pyttsx3
import PyPDF2

book = open('Thebusiness.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

speaker= pyttsx3.init()
for num in range(15,pages):
    page = pdfreader.getPage(num)
    text = page.extractText()

    speaker.say(text)
    speaker.runAndWait()