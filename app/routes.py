from flask import render_template, request, send_file
from app import app
from createQR import generate_qr_codes, createZip 
import os
import shutil


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'csv_file' not in request.files:
        #Handle error - no file part
        return redirect(request.url)
    
    csv_file = request.files['csv_file']

    if csv_file.filename == '':
        #Handle error - no selected file 
        return redirect(request.url)
    
    #save the uploaded csv file 
    csv_path = 'uploads/' + csv_file.filename
    csv_file.save(csv_path)

    #Generate QR codes
    tickets = int(request.form['tickets'])
    generate_qr_codes(csv_path, tickets)

    #Create ZIP file 
    zip_path = '../'+createZip('uploads/')
    print(zip_path)

    #Remove the uploaded CSV file and the generated QR code images
    os.remove(csv_path)
    qrImagesPath = 'uploads/' + 'qr_images'
    shutil.rmtree(qrImagesPath)

    #Send the zip file to the user
    return send_file(zip_path, as_attachment=True, download_name='qrcodes.zip')