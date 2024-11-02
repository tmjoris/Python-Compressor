# Python-Compressor
File Compressor/Decompressor GUI
This is a simple GUI application to compress multiple files into a single ZIP archive or decompress ZIP files into a folder. The application is built with Python's tkinter for the graphical interface and zipfile for compression/decompression functionality.

Features
Select multiple files to compress into a ZIP file.
Choose a name for the output ZIP file.
Select a ZIP file to decompress and specify the destination folder.
User-friendly GUI with prompts for each action.
Requirements
Python 3.x
Installation
Clone or download this repository to your local machine.

Make sure you have Python 3 installed. You can check your Python version with:

bash
Copy code
python3 --version
No external libraries are required beyond the Python Standard Library.

Project Structure
compressor.py: Handles file compression logic.
decompressor.py: Handles file decompression logic.
app.py: Defines the GUI layout and connects button actions to compression/decompression functions.
main.py: Initializes and runs the GUI.
Usage
Open a terminal and navigate to the project folder.

Run the following command to launch the GUI:

bash
Copy code
python main.py
