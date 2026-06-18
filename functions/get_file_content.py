
import os
from config import MAX_READ_BYTES

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(abs_wd, file_path))
        if os.path.commonpath([abs_wd, full_file_path]) != abs_wd:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_ptr = open(full_file_path, mode="r")
        content = file_ptr.read(MAX_READ_BYTES)
        if file_ptr.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_READ_BYTES} characters]'
        
        return content

    except Exception as e:
        return f"Error: Failed to read contents of file \"{full_file_path}\" [{e}]"