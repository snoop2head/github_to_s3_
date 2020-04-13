import os
from os import fdopen, remove
import glob
from tempfile import mkstemp
import shutil
from shutil import move, copymode

# 출처: https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, "w") as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                # If it is previously replaced with S3 URL, then don't change the address
                if "http" in line:
                    new_file.write(line)
                # If not, replace local image URL with S3 image URL
                else:
                    new_file.write(line.replace(pattern, subst))
    # Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


# read markdown file and edit urls
def change_image_src():
    orig = "](/img/"
    # Put your AWS S3 bucket root url
    new = "]({{AWS_S3_ROOT_URL}}/markdown_files/img/"

    # read markdown files
    read_files_list = glob.glob("markdown_files/*.md")
    print(read_files_list)
    for markdown_file in read_files_list:
        replace(markdown_file, orig, new)


change_image_src()
