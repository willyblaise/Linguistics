import unittest
import os
from chunks import split_file  # Assuming the file with the splitting function is named split_file.py

class TestSplitFile(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory and its contents after the tests
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def create_test_file(self, lines):
        # Create a test file with specified lines
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(test_file_path, "w", encoding="utf-8") as test_file:
            test_file.writelines(lines)
        return test_file_path

    def test_split_file(self):
        # Test splitting a file with 500 lines and 300 KB size limit
        lines = ["Line {}\n".format(i) for i in range(1, 201)]
        test_file_path = self.create_test_file(lines)

        # Call the split_file function
        split_file(test_file_path, max_chunk_size_kb=300, max_lines_per_chunk=200)

        # Check if chunks are created and their sizes are within limits
        chunk_files = os.listdir(self.test_dir)
        self.assertTrue(chunk_files)  # Check if there are any chunk files

        for chunk_file in chunk_files:
            chunk_path = os.path.join(self.test_dir, chunk_file)
            size_kb = os.path.getsize(chunk_path) / 1024.0
            self.assertLessEqual(size_kb, 300)  # Check if chunk size is within 300 KB

            with open(chunk_path, "r", encoding="utf-8") as chunk:
                chunk_lines = chunk.readlines()
                self.assertLessEqual(len(chunk_lines), 200)  # Check if chunk has 200 lines or less

if __name__ == '__main__':
    unittest.main()
