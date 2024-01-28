from flask import render_template, request, send_file
from app import app


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
    csv_file.save('uploads/' + csv_file.filename)

    #Generate QR codes


    #Create ZIP file 
    zip_path = "path del zip"

    #Send the zip file to the user
    return send_file(zip_path, as_attachment=True, download_name='qrcodes.zip')