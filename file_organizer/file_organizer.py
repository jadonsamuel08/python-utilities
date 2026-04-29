import os, shutil, sys

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.txt', '.docx', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac']
}

def file_search(file_name):
    extension = os.path.splitext(file_name)[1]  # Gets the extension
    if not extension:
        return False
    
    for cat, extensions in file_categories.items():
        if extension in extensions:
            return cat
    return "Other"

def organize_files(target_folder):
    for item in os.listdir(target_folder):
        source_path = os.path.join(target_folder, item)

        if os.path.isfile(source_path):
            category = file_search(item)
            destination_folder = os.path.join(target_folder, category)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(source_path, os.path.join(destination_folder, item))

def reset_folder(target_folder):
    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)
        
        if os.path.isdir(item_path):
            # Move all files from the category folder back to root
            for filename in os.listdir(item_path):
                file_path = os.path.join(item_path, filename)
                if os.path.isfile(file_path):
                    shutil.move(file_path, os.path.join(target_folder, filename))
            
            # Remove the now-empty category folder
            os.rmdir(item_path)
            
def main():
    try:
        folder = sys.argv[1]
    except:
        folder = input("Enter folder path: ")
    
    if not os.path.isfile(folder):
        print("Invalid PATH")
        exit()
    
    action = input("(o)rganize or (r)eset? ").lower()
    
    if action == 'o':
        organize_files(folder)
        print(f"Files organized in {folder}")
    elif action == 'r':
        reset_folder(folder)
        print(f"Folder reset: {folder}")

if __name__ == "__main__":
    main()