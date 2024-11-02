import zipfile
import os

def compress_files(file_list, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for file in file_list:
            zipf.write(file, os.path.basename(file))
    print("Compression successful")

files_to_compress = ['prompt.js', 'prompt.html']

output_zip_file = 'compressed_files.zip'

compress_files(files_to_compress, output_zip_file)