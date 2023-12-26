import os
import shutil

def copy_files(source_directory, destination_directory):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Get a list of files in the source directory
        files = os.listdir(source_directory)

        for file in files:
            source_path = os.path.join(source_directory, file)

            # Ensure a unique name in the destination directory
            destination_path = os.path.join(destination_directory, file)
            while os.path.exists(destination_path):
                base, ext = os.path.splitext(destination_path)
                destination_path = f"{base}_copy{ext}"

            # Copy the file to the destination directory
            shutil.copy(source_path, destination_path)

        print("Files copied successfully.")
    except Exception as e:
        print(f"Error copying files: {e}")

if __name__ == "__main__":
    source_directory = '/home/champ/Videos'
    destination_directory = '/home/champ/Videos2'

    copy_files(source_directory, destination_directory)
