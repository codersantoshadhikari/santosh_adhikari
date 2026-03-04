"""
Handles file modifications for commits
"""

import os
import random
import string
from datetime import datetime
from pathlib import Path

class FileGenerator:
    def __init__(self, repo_path, files_to_update):
        self.repo_path = Path(repo_path)
        self.files_to_update = files_to_update
        self.ensure_files_exist()
    
    def ensure_files_exist(self):
        """Create files if they don't exist"""
        for file in self.files_to_update:
            file_path = self.repo_path / file
            if not file_path.exists():
                with open(file_path, 'w') as f:
                    f.write(f"# Auto-generated log file\n")
                    f.write(f"# Created: {datetime.now()}\n\n")
    
    def generate_random_content(self, length=50):
        """Generate random string for file content"""
        return ''.join(random.choices(string.ascii_letters + string.digits + '\n', k=length))
    
    def modify_file(self, file_index=None):
        """
        Modify a file to create a git-worthy change
        If file_index is None, pick random file
        """
        if file_index is not None:
            file_to_modify = self.files_to_update[file_index % len(self.files_to_update)]
        else:
            file_to_modify = random.choice(self.files_to_update)
        
        file_path = self.repo_path / file_to_modify
        
        try:
            with open(file_path, 'a') as f:
                # Add timestamp and random data
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                random_data = self.generate_random_content(30)
                f.write(f"[{timestamp}] Update #{self.get_next_sequence(file_path)}: {random_data}\n")
            
            return file_to_modify
        except Exception as e:
            print(f"Error modifying {file_to_modify}: {e}")
            return None
    
    def get_next_sequence(self, file_path):
        """Get next sequence number for this file"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                # Count occurrences of "Update #" to get sequence
                return content.count("Update #") + 1
        except:
            return 1
    
    def create_massive_change(self):
        """Create a change that modifies multiple files (for batch commits)"""
        modified_files = []
        for i in range(random.randint(1, 3)):  # Modify 1-3 files per commit
            file = self.modify_file()
            if file:
                modified_files.append(file)
        return modified_files