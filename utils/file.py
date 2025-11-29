
from pathlib import Path

def allowed_file(filename : str, allowed_extensions: set) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_file_metadata(file_path : Path, filename : str) -> dict:

    stat_info = file_path.stat()
    file_extension = file_path.suffix.lower()  # Including the dot (e.g., '.txt', '.jpg')

    return {
        "filename": filename,
        "filetype": file_extension,
        "size": stat_info.st_size,
        "created": stat_info.st_birthtime,
        "modified": stat_info.st_mtime,
    }
