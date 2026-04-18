#for OS to access files and directories
import os

#To move files around
import shutil

#path.expanduser = defines path for you automatically
directory = os.path.join(os.path.expanduser("~"), "")

#define file types to go in specific directories
extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".wav": "Music"
}

#Go through every file in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename) #define name and directory

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower() #checks file type by taking ext and making lower case

        if extension in extensions:
            folder_name = extensions[extension]

            #joins directory with folder name
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension")
    else:
        print(f"Skipped {filename}. It is a directory")
    
print("File organization complete")
