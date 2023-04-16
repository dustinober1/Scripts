import os
import shutil

# define the source directory where the files are located
source_directory = '/Users/dustinober/Scripts/train'

# define the destination directory where the 'cat' files should be moved
destination_directory = os.path.join(source_directory, 'airplane')

# create the destination directory if it doesn't already exist
if not os.path.exists(destination_directory):
    os.mkdir(destination_directory)

# loop through each file in the source directory
for filename in os.listdir(source_directory):
    # check if the filename contains the word 'cat'
    if 'airplane' in filename:
        # construct the full path to the file
        file_path = os.path.join(source_directory, filename)
        # move the file to the 'cat' folder
        shutil.move(file_path, destination_directory)