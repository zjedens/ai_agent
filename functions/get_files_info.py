
import os

def get_files_info(working_directory: str, directory: str) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_wd, directory))
        is_valid_target_dir = os.path.commonpath([abs_wd, target_dir]) == abs_wd
        
        dir_name_to_print = "current" if directory == "." else f"'{directory}'"
        result_header = f"Result for {dir_name_to_print} directory:"

        if not is_valid_target_dir:
            return result_header + "\n    " + f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return result_header + "\n    " + f'Error: "{directory}" is not a directory'
        
        contents = os.listdir(target_dir)
        contents_info = list(
            map(lambda c: f"  - {c}: file_size={os.path.getsize(os.path.join(target_dir, c))}, is_dir={os.path.isdir(os.path.join(target_dir, c))}", contents)
        )
        
        dir_name_to_print = "current" if directory == "." else f"'{directory}'"
        return "\n".join([f"Result for {dir_name_to_print} directory:"] + contents_info)

    
    except Exception as e:
        return f'Error: The following exception was raised, "{e}"'
