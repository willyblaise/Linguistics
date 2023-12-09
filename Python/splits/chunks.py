import os

def split_file(input_file_path, max_chunk_size_kb=300, max_lines_per_chunk=200):
    # Calculate max size in bytes
    max_chunk_size_bytes = max_chunk_size_kb * 1024

    # Output directory for chunks
    output_directory = "output_chunks"
    os.makedirs(output_directory, exist_ok=True)

    # Initialize variables
    current_chunk_lines = 0
    current_chunk_size = 0
    current_chunk_number = 1

    # Open the input file
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        # Read the entire file
        lines = input_file.readlines()

        for line in lines:
            current_chunk_size += len(line.encode("utf-8"))
            current_chunk_lines += 1
            print(f"Current Chunks size: {current_chunk_size}")
            # Create a new chunk if conditions are met
            if (
                current_chunk_size > max_chunk_size_bytes
                or current_chunk_lines > max_lines_per_chunk
            ):
                output_chunk_path = os.path.join(
                    output_directory, f"chunk_{current_chunk_number}.txt"
                )
                with open(output_chunk_path, "w", encoding="utf-8") as output_chunk:
                    output_chunk.writelines(lines[:current_chunk_lines])

                # Reset variables for the next chunk
                current_chunk_lines = 0
                current_chunk_size = 0
                current_chunk_number += 1

                # Remove the lines that were written to the current chunk
                lines = lines[current_chunk_lines:]

        # Handle the last chunk
        output_chunk_path = os.path.join(
            output_directory, f"chunk_{current_chunk_number}.txt"
        )
        with open(output_chunk_path, "w", encoding="utf-8") as output_chunk:
            output_chunk.writelines(lines)

if __name__ == "__main__":
    input_file_path = "gfileten.txt"  # Replace with the path to your large file
    split_file(input_file_path)
