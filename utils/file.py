
from pathlib import Path

def allowed_file(filename : str, allowed_extensions: set) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_file_metadata(file_path : Path, filename : str) -> dict:

    stat_info = file_path.stat()

    return {
        "filename": filename,
        "size": stat_info.st_size,
        "created": stat_info.st_birthtime,
        "modified": stat_info.st_mtime
    }
