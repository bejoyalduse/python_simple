# -*- coding: utf-8 -*-
"""
Created on Sun Nov 3 04:31:05 2019

@author: bejoyalduse
"""

import img2pdf 
from PIL import Image 
import os 

#Specify the folder path to find the jpeg files and save the created pdf files
#change folder names accordingly if you want to save pdf files in a different folder

# Step 0 - Specify folder paths
folder_path = "C:\Personal\Folder1"
folder_path_jpeg = folder_path
folder_path_pdf = folder_path


#Step1 - List of all the jpeg files in the folder
file_all = os.listdir(folder_path)

#Step 2 -  Run loop through all jpeg files and convert each to pdf

for filename in file_all:
    pp = filename
    pp1 = pp.replace("jpeg", "pdf")

    #Step2-1 File path of image i
    # current image file
    img_path = folder_path_jpeg +'\\'+pp
  
    #Step2-2 File path of pdf i
    # storing pdf path 
    pdf_path = folder_path_pdf + '\\'+pp1
    
    #Step 2- 3 opening image 
    image = Image.open(img_path) 
      
    #Step 2- 4 converting into chunks using img2pdf 
    pdf_bytes = img2pdf.convert(image.filename) 
      
    #Step 2- 5 opening or creating pdf file 
    file = open(pdf_path, "wb") 
      
    #Step 2 -6 writing pdf files with chunks 
    file.write(pdf_bytes) 
  
    #Step 2 -7 closing image file 
    image.close() 
  
    #Step 2 -8 closing pdf file 
    file.close() 
    
    