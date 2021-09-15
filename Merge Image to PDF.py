import fpdf
import os
from PIL import Image
from fpdf import FPDF

pdf = FPDF()
PDF_Name = input("PDF file name:") + ".pdf"

#BIM for Structural Engineers - Start-Up Guide - 0.pdf"

W_pixels = 1000
H_pixels = 1000

Pixel_MM_Converter = 0.2645833333
w = Pixel_MM_Converter * W_pixels
h = Pixel_MM_Converter * H_pixels

Files_Path = r'C:\Users\m\Dropbox\KS DIGITAL INNOVATIONS\05 - SOCIAL MEDIA CONTENTS\01 - BIM 4 STRUCTURAL ENGINEERS'

os.chdir(Files_Path)

imageName = r"\POST {}.png"


os.path.exists(Files_Path)

output = []
Total_Files = 12 #This is the total number of files in the directory

for n in range(1,Total_Files+1):
    fname = Files_Path + imageName.format(n)
    if os.path.exists(fname):
        if n == 1:
            cover = Image.open(fname)
            w,h = cover.size
            pdf = FPDF(unit= "mm", format= [w,h])
        pdf.add_page()
        pdf.image(fname,0,0,w,h)
        print("processed " + imageName.format("%d") %n)

    else:
        print("File not found:", fname)

pdf.output(PDF_Name)

print("PDF Image file merging done")
os.startfile(PDF_Name)