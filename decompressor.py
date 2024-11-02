import zipfile

def decompress_files(zip_file, output_folder):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_folder)
    print("Decompression successful")

zip_file_path = 'compressed_files.zip'

output_folder = 'Extracted_files'

decompress_files(zip_file_path, output_folder)