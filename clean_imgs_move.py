import os
from os import fdopen, remove
import glob
from tempfile import mkstemp
import shutil
from shutil import move, copymode


def sort_and_move_image_file():
    # change the source directory to your project directory
    # source = 'absolute/path/to/source_folder'
    source = "/Users/noopy/github_to_s3/"

    # change the destination directory to your project directory
    # dest = 'absolute/path/to/source_folder'
    dest = "/Users/noopy/github_to_s3/markdown_files/img"

    jpg_file_list = glob.glob("markdown_files/*.jpg")
    jpeg_file_list = glob.glob("markdown_files/*.jpeg")
    png_file_list = glob.glob("markdown_files/*.png")

    for item in jpg_file_list:
        shutil.move(source + item, dest)

    for item in png_file_list:
        shutil.move(source + item, dest)

    for item in jpeg_file_list:
        shutil.move(source + item, dest)


# source: https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, "w") as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if "img/" in line:
                    new_file.write(line)
                elif "http" in line:
                    new_file.write(line)
                else:
                    new_file.write(line.replace(pattern, subst))
    # Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


# read markdown file and edit urls
def move_images():
    sort_and_move_image_file()
    orig = "]("
    new = "](img/"

    # read markdown files
    read_files_list = glob.glob("markdown_files/*.md")
    print(read_files_list)
    for markdown_file in read_files_list:
        replace(markdown_file, orig, new)


move_images()
