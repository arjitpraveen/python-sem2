import shutil
import os.path

archive = shutil.make_archive('backup-file', 'zip', r'C:\Users\arjit\Downloads\pysem2\backup-folder')

archive = shutil.make_archive

if os.path.exists(r'backup-folder\backup-file.zip'):
    print(f"The file is zipped in: {archive}")
else:
    print("The zip folder does not exist")