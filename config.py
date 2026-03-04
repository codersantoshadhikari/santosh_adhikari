"""
Configuration settings for auto-commit system
"""

import os
from pathlib import Path

# Get the directory where this script is located
BASE_DIR = Path(__file__).parent.absolute()

class Config:
    # Repository settings
    REPO_PATH = os.getenv('REPO_PATH', str(BASE_DIR / 'my_auto_repo'))
    BRANCH_NAME = "main"
    
    # Commit settings
    COMMIT_MESSAGE_PREFIX = "Auto Commit"
    TOTAL_COMMITS = 100000  # One lakh commits
    
    # File generation settings
    FILES_TO_UPDATE = [
        "log1.txt",
        "log2.txt", 
        "data.txt",
        "changes.log",
        "updates.txt"
    ]
    
    # Batch processing
    COMMITS_PER_BATCH = 100
    PUSH_FREQUENCY = 50  # Push every 50 commits
    
    # Safety settings (prevents GitHub from blocking you)
    MIN_DELAY_SECONDS = 0.5  # Minimum delay between commits
    MAX_COMMITS_PER_HOUR = 1000  # GitHub's unofficial limit ~5000/hr
    
    # Progress tracking
    PROGRESS_FILE = "commit_progress.txt"
    
    # Git user configuration (update with your details)
    GIT_USER_NAME = "Your Name"
    GIT_USER_EMAIL = "your.email@example.com"