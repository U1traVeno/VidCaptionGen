import os

def rename_txt2crt(txt_file_dir, crt_file_dir):
    """
    Change txt file to crt file.
    """
    for filename in os.listdir(txt_file_dir, crt_file_dir):
        if filename.endswith(".txt"):
            new_filename = 
