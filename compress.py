import zipfile
import os

def compress_files(file_list, output_filename):
    try:
        with zipfile.ZipFile(output_filename, 'w') as zipf:
            for file in file_list:
                zipf.write(file, os.path.basename(file))
        return "Compression successful"
    except Exception as e:
        return f"Failed to compress: {e}"