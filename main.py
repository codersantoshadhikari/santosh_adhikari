"""
Main entry point for auto-commit system
"""

import os
import sys
import time
from pathlib import Path

# Import our modules
from config import Config
from safety_check import RateLimiter, ProgressTracker
from file_generator import FileGenerator
from git_manager import GitManager
from batch_processor import BatchProcessor

def setup_repository(config):
    """Setup or verify repository"""
    repo_path = Path(config.REPO_PATH)
    
    if not repo_path.exists():
        print(f"Creating repository at: {repo_path}")
        repo_path.mkdir(parents=True, exist_ok=True)
    
    # Check if we need to setup remote
    setup_remote = input("Do you want to setup a GitHub remote? (y/n): ").lower() == 'y'
    
    if setup_remote:
        github_url = input("Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): ")
        return github_url
    
    return None

def main():
    """Main function"""
    print("="*60)
    print("AUTO-COMMIT SYSTEM FOR 100,000 COMMITS")
    print("="*60)
    print("\nWARNING: This will create 100,000 commits!")
    print("This process will take several hours/days.")
    print("Make sure you understand GitHub's terms of service.")
    print("\nPress Ctrl+C to stop at any time (progress will be saved).")
    print("-"*60)
    
    # Load configuration
    config = Config()
    
    # Confirm with user
    response = input(f"\nProceed with creating {config.TOTAL_COMMITS} commits? (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted.")
        return
    
    # Setup repository
    remote_url = setup_repository(config)
    
    # Initialize components
    print("\nInitializing components...")
    
    # Rate limiter (protects against GitHub blocks)
    rate_limiter = RateLimiter(
        max_commits_per_hour=config.MAX_COMMITS_PER_HOUR,
        min_delay=config.MIN_DELAY_SECONDS
    )
    
    # Progress tracker (allows resume after interruption)
    progress_file = Path(config.REPO_PATH) / config.PROGRESS_FILE
    progress_tracker = ProgressTracker(progress_file)
    
    # File generator
    file_gen = FileGenerator(config.REPO_PATH, config.FILES_TO_UPDATE)
    
    # Git manager
    git_manager = GitManager(
        config.REPO_PATH,
        config.BRANCH_NAME,
        config.GIT_USER_NAME,
        config.GIT_USER_EMAIL
    )
    
    # Setup remote if provided
    if remote_url:
        git_manager.add_remote(remote_url)
        print(f"Remote configured: {remote_url}")
    
    # Batch processor
    processor = BatchProcessor(
        git_manager,
        file_gen,
        rate_limiter,
        progress_tracker,
        config
    )
    
    # Handle Ctrl+C gracefully
    try:
        # Start processing
        processor.process_all_commits()
        
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user!")
        processor.stop()
        print(f"Progress saved: {progress_tracker.completed_commits} commits completed")
        print("You can resume later by running this script again.")
    
    print("\nProcess completed!")

if __name__ == "__main__":
    main()