'''
References: 
# https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
'''

import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import argparse
parser = argparse.ArgumentParser(description="Cloud database with insights.")
parser.add_argument('--online', type=bool, default=False, help='Default turns off GCP Connection--Saves money.')
parser.add_argument('--metadata', type=bool, default=False, help='Default turns off GCP DB--Saves money.')
args = parser.parse_args()

import functions.upload as upload

app = Flask(__name__)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


from pathlib import Path
import tempfile

def get_file_metadata(file_path : Path, filename):

    stat_info = file_path.stat()

    return {
        "filename": filename,
        "size": stat_info.st_size,
        "created": stat_info.st_birthtime,
        "modified": stat_info.st_mtime
    }

    

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
            
            if args.online:
                # only upload the file if enabled
                result = upload.upload_file(file, filename)
                flash(result)
            else:
                flash("Application is currently not uploading files.")


            with tempfile.NamedTemporaryFile(delete_on_close=True) as tmp:
                file.save(tmp)
                tmp_path = Path(tmp.name)
                tmp.flush()
                os.fsync(tmp.fileno())
                metadata = get_file_metadata(tmp_path, filename)
                print(metadata)

                if args.metadata:
                    upload.upload_metadata(metadata)
    
        return redirect(request.url)
    
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)


