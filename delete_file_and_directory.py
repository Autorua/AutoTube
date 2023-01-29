import os
import shutil

# getting the filename from the user

file_path = "video.mp4"

# checking whether file exists or not
if os.path.exists(file_path):
    # removing the file using the os.remove() method
   os.remove(file_path)
else:
    # file not found message
    print("File not found in the directory")

# Delete with shutil

# Replace with the path to the directory you want to remove
directory = 'data'
#directory = 'new_folder'
shutil.rmtree(directory)

