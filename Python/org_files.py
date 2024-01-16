import os
import shutil

def organize_files(directory_path):
    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        # Skip hidden files
        if filename.startswith('.'):
            continue

        file_path = os.path.join(directory_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename.lower())

        # Skip files with unknown extensions
        if not file_extension:
            continue

        # Create directory for the extension if it doesn't exist
        destination_folder = os.path.join(directory_path, file_extension[1:])
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the appropriate directory
        print(f"Destination: {destination_folder}")
        shutil.move(file_path, os.path.join(destination_folder, filename))

    print("Files organized successfully!")

def main():
    # Replace 'your_directory_path' with the actual path to your directory
    dp = os.environ.get("HOME")
    organize_files(dp)

if __name__ == "__main__":
    main()
