from flask import Blueprint, request, flash, redirect, render_template
from werkzeug.utils import secure_filename
from .file import allowed_file
from .upload import handle_upload
import config

import argparse
parser = argparse.ArgumentParser(description="Cloud database with insights.")
parser.add_argument('--online', type=bool, default=False, help='Enable GCP upload.')
parser.add_argument('--metadata', type=bool, default=False, help='Enable metadata upload.')
args, unknown = parser.parse_known_args()

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET','POST'])
def index():
    # check if the request has the file
    if request.method == 'POST':
        file = request.files.get('file')

        if not file:
            flash('No file part')
            return redirect(request.url)

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if not allowed_file(file.filename, config.Config.ALLOWED_EXTENSIONS):
            flash('File type not allowed')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        handle_upload(file, filename, args)

        return redirect(request.url)

    return render_template('index.html')
