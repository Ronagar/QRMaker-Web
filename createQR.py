# -*- coding: utf-8 -*-
from pathlib import Path
import qrcode
#from PIL import Image
import csv 
import zipfile
import os

def generate_qr_codes(csvPath, ntickets):
    print("he entrado en generar qrs")
    #csvPath = 'uploads/alumns.csv'
    with open(csvPath, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        headers = [header.strip() for header in reader.fieldnames]
        for row in reader:
            #store the attendant full name writing '_' instead of spaces
            name = row.get(headers[0]).replace(' ', '_')
            surnames = row.get(headers[1]).replace(' ', '_')
            attendant = surnames+'_'+name
            

            #Creation of the path if neccessary
            Path('uploads/qr_images/'+attendant).mkdir(parents=True, exist_ok=True)
            
            for n in range(ntickets):
                QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
                #extract the attendant id from the dataSet
                data = row.get(headers[2]) + row.get(headers[3])
                #Feed the QR Code data
                data = data+'_'+str(n+1)
                QRcode.add_data(data)
                QRcode.make(fit=True)
                # Insert the image to the QR code and create the final image
                QRimg = QRcode.make_image(fill_color='Black', back_color='White').convert('RGB')

                #We define the image position (center)
                #pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
                #QRimg.paste(logo, pos)
            
                #Save the image .png
                path = 'uploads/qr_images/'+attendant+'/'+data+'.png'
                QRimg.save(path)
        
    file.close()


def createZip(Path):
    zipPath = os.path.join(Path+'codes.zip')
    with zipfile.ZipFile(zipPath, 'w') as myZip:
        # Recorre los archivos en qr_images y los añade al archivo ZIP
        for root, dirs, files in os.walk(os.path.join(Path, 'qr_images')):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.join(Path, 'qr_images'))
                myZip.write(file_path, arcname)
    return zipPath

