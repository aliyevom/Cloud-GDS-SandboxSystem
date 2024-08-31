import os
import shutil
from deduplicator.py import FileDeduplicator

class Sandbox:
    def __init__(self, storage_directory):
        self.storage_directory = storage_directory
        self.deduplicator = FileDeduplicator(storage_directory)
        
        if not os.path.exists(storage_directory):
            os.makedirs(storage_directory)

    def upload_file(self, file_path):
        """Simulate uploading a file to the sandbox."""
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return
        
        # Store the file using the deduplicator
        stored_path = self.deduplicator.store_file(file_path)
        print(f"File uploaded and stored at: {stored_path}")

    def list_files(self):
        """List all files stored in the sandbox."""
        files = self.deduplicator.get_stored_files()
        for file_hash, file_path in files.items():
            print(f"{file_path} - {file_hash}")

if __name__ == "__main__":
    # Create a sandbox instance
    sandbox = Sandbox(storage_directory="sandbox_storage")
    
    # Simulate uploading files
    sandbox.upload_file("test_files/file1.txt")
    sandbox.upload_file("test_files/file2.txt")
    sandbox.upload_file("test_files/file1_duplicate.txt")  # Assuming this is a duplicate of file1.txt
    
    # List all stored files
    sandbox.list_files()
