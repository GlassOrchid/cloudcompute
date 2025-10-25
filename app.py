'''
References: 
# https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
'''

import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import functions.upload as upload

UPLOAD_FOLDER = 'file_uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'446'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def index():
    # check if the request has the file
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        # The browser submits an empty file if user doesn't select
        if file.name == '':
            flash('No selected file')
            return redirect(request.url)
        
        # Validate file 
        if file and allowed_file(file.filename):
            # ensures the file name is safe for upload
            filename = secure_filename(file.filename)
            
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = upload.upload_file(file, filename)

            flash(result)
            return redirect(request.url)
    
    
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)