import zipfile

def decompress_files(zip_file, output_folder):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(output_folder)
        print("Decompression successful")
    except Exception as e:
        return f"Failed to decompress: {e}"