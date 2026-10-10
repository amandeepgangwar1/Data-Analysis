print("__________File Organizer__________")

import os
import shutil


# Folder path you want to organize...
FOLDER_PATH = r'C:\Users\amand\Desktop\Data Analysis\Python in Data Analysis\Mini Projects'

# File mapping
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt', '.pages'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.alac'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm', '.m4v', '.mpg', '.mpeg'],
    'Code': ['.java', '.js', '.html', '.css', '.cpp', '.c', '.go', '.rs', '.php', '.rb', '.swift'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'],
    'Data': ['.csv', '.json', '.xml', '.sql', '.db', '.parquet'],
}

# Create folders if they don't exist
for folder in FILE_TYPES.keys():     # Create folders for each file type
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    # Skip folder 
    if os.path.isdir(file_path):
        continue

    # Get file extension
    # print(os.path.splitext(file))
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))

print("Files Organized successfully...✅")
