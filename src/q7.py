import shutil
import os.path

# Creating the ZIP file
archived = shutil.make_archive('backup-folder', 'zip', 'backupfolder')

if os.path.exists('backup-folder.zip'):
    print(f"The path the folder is zipped in:\n{archived}")
else:
    print("ZIP file not created")

