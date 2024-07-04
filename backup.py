import os
import sys
import shutil
import datetime


def file_check(src_dir,target_dir):
    try:
        # Checking if the source and target directories exist or not:
        if not os.path.isdir(src_dir):
            print(f"The source directory {src_dir} is not present ")
        if not os.path.isdir(target_dir):
            print(f"The target directory {target_dir} does not exist")
        
        # Retrieving the files from the source folder
        file_name=os.listdir(src_dir)
        files=[item for item in file_name if os.path.isfile(os.path.join(src_dir,item))]
        for file_name in files:
            target_file=os.path.join(target_dir,file_name)

            
        #Checking if filename exist then append with timestamp
        if os.path.exists(target_file):
            filename,extension=os.path.splitext(file_name)
            timestr=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            new_filename=f"{filename}_{timestr}{extension}"
            new_target_dir=os.path.join(target_dir,new_filename)
            shutil.copy(target_file,new_target_dir)
            print(f"File already exists.Copied as {new_filename}")
        
        # else the copy of the file directly from the src to target
        else:
            shutil.copy(src_dir,target_dir)
            print( f"File copied to {target_dir}")
    except Exception as e:
        print(f"ERROR: {e}")


if len(sys.argv) !=3:
    print("Syntax: Backup.py <source_directory> <target directory>")
    sys.exit(2)

src_dir=sys.argv[1]
target_dir=sys.argv[2]
file_check(src_dir,target_dir)
    
    
    