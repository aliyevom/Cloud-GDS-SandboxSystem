import hashlib
import os

class FileDeduplicator:
    def __init__(self, storage_directory):
        self.storage_directory = storage_directory
        self.hash_map = {}

    def generate_file_hash(self, file_path):
        """Generate a SHA-256 hash for the given file."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def store_file(self, file_path):
        """Store the file if it's not already stored based on its hash."""
        file_hash = self.generate_file_hash(file_path)
        
        if file_hash in self.hash_map:
            print(f"Duplicate file detected: {file_path} already stored as {self.hash_map[file_hash]}")
            return self.hash_map[file_hash]  # Return the already stored file path

        # Generate a new file name based on the hash
        new_file_name = f"Hash{file_hash[:8]}"  # Taking only first 8 characters for simplicity
        new_file_path = os.path.join(self.storage_directory, new_file_name)
        
        # Move or copy the file to the storage directory
        os.rename(file_path, new_file_path)
        
        # Store the hash and file path
        self.hash_map[file_hash] = new_file_path
        print(f"Stored file: {new_file_path}")
        return new_file_path

    def get_stored_files(self):
        """Get a dictionary of stored files with their hashes."""
        return self.hash_map
