
from pathlib import Path
from datetime import datetime

def allowed_file(filename : str, allowed_extensions: set) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def get_file_metadata(file_path : Path, filename : str) -> dict:

    stat_info = file_path.stat()
    file_extension = Path(filename).suffix.lower().strip('.')  # Including the dot (e.g., '.txt', '.jpg')

    created_time = datetime.fromtimestamp(stat_info.st_birthtime).strftime('%Y-%m-%d %H:%M:%S')
    modified_time = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

    print(stat_info)

    return {
        "filename": filename,
        "filetype": file_extension,
        "size": stat_info.st_size,
        "created": created_time,
        "modified": modified_time,
    }
