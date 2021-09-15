'''This script helps you merge any specified number of images inside a folder into
a single PDF file without the need to download any third party software'''

#IMPORT THE REQUIRED PYTHON LIBRARIES FOR THIS WORKFLOW
import fpdf
import os
from PIL import Image
from fpdf import FPDF

pdf = FPDF()

#SPECIFY THE NAME OF THE OUTPUT PDF FILE
PDF_Name = input("PDF file name:") + ".pdf"

#SPECIFY A GENERAL WIDTH AND HEIGHT OF THE IMAGES IN PIXELS
W_pixels = 1000
H_pixels = 1000

#THIS LINE OF CODE CONVERTS THE SIZE OF THE IMAGES FROM PIXELS TO MILLIMETERS
Pixel_MM_Converter = 0.2645833333
w = Pixel_MM_Converter * W_pixels
h = Pixel_MM_Converter * H_pixels

#SPECIFY THE FILE DIRECTORY WHERE THE IMAGES ARE LOCATED
Files_Path = r'C:\Users\m\Dropbox\KS DIGITAL INNOVATIONS\05 - SOCIAL MEDIA CONTENTS\01 - BIM 4 STRUCTURAL ENGINEERS'

os.chdir(Files_Path)

#SPECIFY THE IMAGE NAME IN AN ARRAY OF NUMBERS
imageName = r"\POST {}.png"

#CHECK IF FILE DIRECTORY EXISTS
os.path.exists(Files_Path)

output = []
Total_Files = 12 #Specify the number of image files in the directory you want to merge into PDF

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