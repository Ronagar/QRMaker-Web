# -*- coding: utf-8 -*-
from pathlib import Path
import qrcode
from PIL import Image
import csv 

imagenlogo = './etsii.jpeg'
logo = Image.open(imagenlogo)
# Resize the image
hsize = int((float(logo.size[1])*float(60/float(logo.size[0]))))
#logo = logo.resize((100, hsize), Image.ANTIALIAS)
logo = logo.resize((60, hsize))

with open('alumnos.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = [header.strip() for header in reader.fieldnames]
    for row in reader:
        #store the student full name writing '_' instead of spaces
        name = row.get(headers[0]).replace(' ', '_')
        surnames = row.get(headers[1]).replace(' ', '_')
        student = surnames+'_'+name
        

        #Creation of the path if neccessary
        Path('./outputs/'+student).mkdir(parents=True, exist_ok=True)
        

        for letter in ('a','b','c'):
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            #extract the student id from the dataSet
            data = row.get(headers[2])
            #Feed the QR Code data
            data = data+'_'+letter
            QRcode.add_data(data)
            QRcode.make
            # Insert the image to the QR code and create the final image
            QRimg = QRcode.make_image(fill_color='Black', back_color='White').convert('RGB')

            #We define the image position (center)
            pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
            QRimg.paste(logo, pos)
        
            #Save the image .png
            path = './outputs/'+student+'/'+data+'.png'
            QRimg.save(path)
     
file.close()




