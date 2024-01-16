import os
import shutil

def organize_files(directory_path):
    # Create directories if they don't exist
    folders = {
        'pdf': 'pdf',
        'video': 'video',
        'music': 'music',
        'docs': 'docs',
        'javas': 'javas',
        'python': 'python',
        'perl': 'perl',
        'html': 'html',
        'csv': 'csv'
#        'other': 'other'  # New folder for unknown extensions
    }

    for folder_name in folders.values():
        os.makedirs(os.path.join(directory_path, folder_name), exist_ok=True)

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename.lower())

        # Organize files based on extension
        destination_folder = folders.get(file_extension[1:], folders['other'])

        # Move the file to the appropriate directory
        print(f"Destination: {destination_folder}")
        shutil.move(file_path, os.path.join(directory_path, destination_folder, filename))

    print("Files organized successfully!")

def main():
    # Replace 'your_directory_path' with the actual path to your directory
    dp = os.environ.get("HOME")
    organize_files(dp)

if __name__ == "__main__":
    main()
