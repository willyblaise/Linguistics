import json
import os

# Load the JSON data
with open('output_file.json', 'r') as file:
    data = json.load(file)

# Convert the data back to a JSON-formatted string
json_string = json.dumps(data)

# Calculate the chunk size in bytes
chunk_size_bytes = 200 * 1024

# Break the JSON data into chunks
chunks = [json_string[i:i + chunk_size_bytes] for i in range(0, len(json_string), chunk_size_bytes)]

# Create a directory to store the chunks
output_directory = 'output_chunkz'
os.makedirs(output_directory, exist_ok=True)

# Save each chunk to a separate file
for i, chunk in enumerate(chunks):
    output_file_path = os.path.join(output_directory, f'chunk_{i + 1}.json')
    with open(output_file_path, 'w') as file:
        file.write(chunk)
