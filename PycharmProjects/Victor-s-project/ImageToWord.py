#pip Install docx
#pip install Pillow
from docx import document
from docx.shared import Inches
import os
def open(imag):
    img = Image.open(imag)
    document = document()
    document.add_heading("python word Doc")
    document.add_paragraph(img)
    document.save('demo1.docx')