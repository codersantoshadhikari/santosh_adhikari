"""
Manages all Git operations
"""

import subprocess
import os
from pathlib import Path
import sys

class GitManager:
    def __init__(self, repo_path, branch_name="main", user_name=None, user_email=None):
        self.repo_path = Path(repo_path)
        self.branch_name = branch_name
        self.user_name = user_name
        self.user_email = user_email
        self.ensure_repo()
    
    def run_git_command(self, command, check=True):
        """Execute a git command and return output"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if check and result.returncode != 0:
                print(f"Git command failed: {command}")
                print(f"Error: {result.stderr}")
                return None
            
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            print(f"Git command timed out: {command}")
            return None
        except Exception as e:
            print(f"Error running git command: {e}")
            return None
    
    def ensure_repo(self):
        """Ensure repository exists and is properly configured"""
        if not self.repo_path.exists():
            print(f"Creating repository at {self.repo_path}")
            self.repo_path.mkdir(parents=True, exist_ok=True)
            self.run_git_command("git init")
            self.run_git_command(f"git branch -M {self.branch_name}")
        
        # Configure git user if provided
        if self.user_name:
            self.run_git_command(f'git config user.name "{self.user_name}"')
        if self.user_email:
            self.run_git_command(f'git config user.email "{self.user_email}"')
    
    def add_files(self, files=None):
        """Add files to staging area"""
        if files:
            if isinstance(files, list):
                for file in files:
                    self.run_git_command(f'git add "{file}"')
            else:
                self.run_git_command(f'git add "{files}"')
        else:
            self.run_git_command("git add .")
        return True
    
    def commit(self, message):
        """Create a commit with given message"""
        result = self.run_git_command(f'git commit -m "{message}"')
        return result is not None
    
    def push(self):
        """Push changes to remote"""
        # Check if remote exists
        remotes = self.run_git_command("git remote")
        if not remotes:
            print("No remote repository configured. Skipping push.")
            return False
        
        result = self.run_git_command(f"git push origin {self.branch_name}")
        return result is not None
    
    def add_remote(self, remote_url):
        """Add remote repository"""
        self.run_git_command(f"git remote add origin {remote_url}")
    
    def get_status(self):
        """Get git status"""
        return self.run_git_command("git status --porcelain")
    
    def has_changes(self):
        """Check if there are changes to commit"""
        status = self.get_status()
        return bool(status)