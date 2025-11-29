from pathlib import Path

def load_sql(file_name):
    path = Path(__file__).parent.parent / 'queries' / file_name
    with open(path, 'r') as f:
        return f.read()

INSERT_FILE_QUERY = load_sql('insert.sql')