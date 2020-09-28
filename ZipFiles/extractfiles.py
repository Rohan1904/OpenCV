import os
import zipfile

# mention path of zip file
z_file = zipfile.ZipFile("Dataset.zip")
# Mention Directory or Folder in which You want to extract files
z_file.extractall("MY_EXTRACTED_FOLDER")
#close file after use
z_file.close()
print("Extracted Successfully")
