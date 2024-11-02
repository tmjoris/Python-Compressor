import tkinter as tk
from tkinter import filedialog, messagebox
from compress import compress_files
from decompressor import decompress_files

class CompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Compressor/Decompressor")
        self.root.geometry("400x300")

        self.files_to_compress = []
        self.zip_file_path = ""

        #will add the select files button
        tk.Label(root, text="Select Files or Folders to Compress").pack(pady=10)
        self.select_button = tk.Button(root, text="Select Files", command=self.select_files)
        self.select_button.pack(pady=5)

        #Allow the user to choose a name for his Zip File
        tk.Label(root, text="Enter Output Zip File Name").pack(pady=10)
        self.zip_name_entry = tk.Entry(root)
        self.zip_name_entry.pack(pady=5)

        #Compress button
        self.compress_button=tk.Button(root, text="Compress File(s)", command=self.compress)
        self.compress_button.pack(pady=5)

        #Decompress button
        tk.Label(root, text="Or Select a Zip File to Decompress").pack(pady=10)
        self.decompress_button = tk.Button(root, text="Decompress Zip File", command=self.decompress)
        self.decompress_button.pack(pady=5)

    def select_files(self):
        self.files_to_compress = filedialog.askopenfilenames(title="Select Files To Compresss")
        if not self.files_to_compress:
            messagebox.showwarning("Warning", "No files selected")
        
    def compress(self):
        output_zip = self.zip_name_entry.get().strip()
        if not output_zip.endswith(".zip"):
            output_zip += ".zip"

        if self.files_to_compress and output_zip:
            result = compress_files(self.files_to_compress, output_zip)
            messagebox.showinfo("Info", result)
        else:
            messagebox.showwarning("Warning", "Please select files and enter a zip file name")
    
    def decompress(self):
        zip_file = filedialog.askopenfilename(title ="Select Zip File to Decompress", filetypes=[("Zip files", ".zip")])
        if zip_file:
            output_folder = filedialog.askdirectory(title="Select Folder to Extract To")
            if output_folder:
                result = decompress_files(zip_file, output_folder)
                messagebox.showinfo("Info", result)
            else:
                messagebox.showwarning("Warning", "No output folder selected")
        else:
            messagebox.showwarning("Warning", "No zip file selected")


