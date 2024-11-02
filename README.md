# Python-Compressor

This is a simple GUI application to compress multiple files into a single ZIP archive or decompress ZIP files into a folder. The application is built with Python's tkinter for the graphical interface and zipfile for compression/decompression functionality.

**Features** <br/>
Select multiple files to compress into a ZIP file.<br/>
Choose a name for the output ZIP file.<br/>
Select a ZIP file to decompress and specify the destination folder.<br/>
User-friendly GUI with prompts for each action.<br/>
Requirements<br/>
Python 3<br/>

**Installation**<br/>
Clone or download this repository to your local machine.<br/>
Make sure you have Python 3 installed. You can check your Python version with:<br/>
- ```python3 --version```
- No external libraries are required beyond the Python Standard Library.<br/>

**Project Structure**<br/>
- compressor.py: Handles file compression logic.<br/>
- decompressor.py: Handles file decompression logic.<br/>
- app.py: Defines the GUI layout and connects button actions to compression/decompression functions.<br/>
- main.py: Initializes and runs the GUI.<br/>

**Usage**<br/>
Open a terminal and navigate to the project folder.<br/>

Run the following command to launch the GUI:<br/>

```python main.py```
