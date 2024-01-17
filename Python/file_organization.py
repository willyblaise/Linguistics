import os
import shutil

def organize_files(directory_path):
    # Create directories if they don't exist
    pdfs = os.path.join(directory_path, 'pdf')
    vidz = os.path.join(directory_path, 'video')
    muse = os.path.join(directory_path, 'music')
    docs = os.path.join(directory_path, 'docs')
    javas = os.path.join(directory_path, 'javas')
    python = os.path.join(directory_path, 'python')
    perl = os.path.join(directory_path, 'perl')
    html = os.path.join(directory_path, 'html')
    csv = os.path.join(directory_path, 'csv')

    for folder in [pdfs, vidz, muse, docs, javas, python, perl, html]:
        os.makedirs(folder, exist_ok=True)

    # Iterate through files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename.lower())

        # Organize files based on extension
        if file_extension == '.pdf':
            destination_folder = pdfs
        elif file_extension in ['.mp4', '.mkv', '.avi']:
            destination_folder = vidz
        elif file_extension in ['.mp3', '.wav', '.flac']:
            destination_folder = muse
        elif file_extension in ['.docx', '.txt']:
            destination_folder = docs
        elif file_extension in ['.java']:
            destination_folder = javas
        elif file_extension in ['.py']:
            destination_folder = python
        elif file_extension in ['.pl']:
            destination_folder = perl
        elif file_extension in ['.html']:
            destination_folder = html
        elif file_extension in ['.csv']:
            os.makedirs("csv", exist_ok=True)
            destination_folder = csv
        else:
            # Skip files with unknown extensions
            continue

        # Move the file to the appropriate directory
        print(f"Destination: {destination_folder}")
        shutil.move(file_path, os.path.join(destination_folder, filename))

    print("Files organized successfully!")


def main():
    # Replace 'your_directory_path' with the actual path to your directory
    #dp = "/home/champ/"
    dp = os.environ.get("HOME")
    organize_files(dp)


if __name__ == "__main__":
    main()