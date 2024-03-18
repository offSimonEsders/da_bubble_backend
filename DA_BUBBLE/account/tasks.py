import mimetypes


def get_file_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type.replace('/', '.').replace('image', '')