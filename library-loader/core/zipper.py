import zipfile

"""
This function is used to unzip the library archive file 
"""
def unzip_library(src: str, dest: str):
    folder_name = src.rstrip(".zip")
    if dest[-1] != "/":
        dest += "/"

    with zipfile.ZipFile(src) as myzip:
        myzip.extractall(dest + folder_name)
