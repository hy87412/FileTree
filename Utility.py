import hashlib
import pathlib

def get_hash(file_path):
    file_path = pathlib.Path(file_path)
    data = file_path.read_bytes()

    header = f"blob {len(data)}\0".encode('utf-8')

    return hashlib.sha1(header + data).hexdigest()

