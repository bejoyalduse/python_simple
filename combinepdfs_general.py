"""
Created on Mon Sep 16 09:58:11 2019

@author: bejoyalduse
"""
import os
from PyPDF2 import PdfFileMerger

folder_path = "C:\Personal"

os.chdir(folder_path)

#Step1 - List of all the jpeg files in the folder
pdfs = os.listdir(folder_path)

merger = PdfFileMerger()

for pdf in pdfs:
    if pdf.endswith(".pdf"):
        merger.append(pdf)

merger.write("MergedFile.pdf")

merger.close()