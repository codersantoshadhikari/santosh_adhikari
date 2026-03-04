"""
Handles batch processing of commits with progress tracking
"""

import time
from datetime import datetime, timedelta
import threading
from queue import Queue

class BatchProcessor:
    def __init__(self, git_manager, file_generator, rate_limiter, progress_tracker, config):
        self.git = git_manager
        self.file_gen = file_generator
        self.rate_limiter = rate_limiter
        self.progress = progress_tracker
        self.config = config
        self.stop_flag = False
        self.stats = {
            'start_time': None,
            'commits_done': 0,
            'failed_commits': 0,
            'push_count': 0
        }
    
    def create_commit(self, commit_number):
        """Create a single commit"""
        try:
            # Wait if rate limited
            self.rate_limiter.wait_if_needed()
            
            # Modify files
            modified_files = self.file_gen.create_massive_change()
            
            if not modified_files:
                print(f"Warning: No files modified for commit #{commit_number}")
                return False
            
            # Add files to git
            self.git.add_files(modified_files)
            
            # Create commit
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            commit_message = f"{self.config.COMMIT_MESSAGE_PREFIX} #{commit_number} [{timestamp}]"
            
            if self.git.commit(commit_message):
                self.progress.increment()
                self.stats['commits_done'] += 1
                
                # Print progress every 100 commits
                if commit_number % 100 == 0:
                    self.print_progress(commit_number)
                
                return True
            else:
                self.stats['failed_commits'] += 1
                return False
                
        except Exception as e:
            print(f"Error creating commit #{commit_number}: {e}")
            self.stats['failed_commits'] += 1
            return False
    
    def push_if_needed(self, commit_number):
        """Push commits in batches"""
        if commit_number % self.config.PUSH_FREQUENCY == 0:
            print(f"\nPushing batch after {commit_number} commits...")
            if self.git.push():
                self.stats['push_count'] += 1
                print(f"Push successful! (Push #{self.stats['push_count']})")
            else:
                print("Push failed, will retry later")
    
    def print_progress(self, commit_number):
        """Print progress statistics"""
        if self.stats['start_time']:
            elapsed = datetime.now() - self.stats['start_time']
            commits_per_second = commit_number / elapsed.total_seconds() if elapsed.total_seconds() > 0 else 0
            
            print(f"\n{'='*50}")
            print(f"PROGRESS UPDATE - Commit #{commit_number}")
            print(f"Time elapsed: {elapsed}")
            print(f"Speed: {commits_per_second:.2f} commits/second")
            print(f"Failed commits: {self.stats['failed_commits']}")
            print(f"Pushes completed: {self.stats['push_count']}")
            
            # Estimate time remaining
            remaining = self.config.TOTAL_COMMITS - commit_number
            if commits_per_second > 0:
                eta_seconds = remaining / commits_per_second
                eta = timedelta(seconds=eta_seconds)
                print(f"Estimated time remaining: {eta}")
            
            rate_stats = self.rate_limiter.get_stats()
            print(f"Rate limit: {rate_stats['commits_last_hour']}/{rate_stats['max_per_hour']} commits in last hour")
            print(f"{'='*50}\n")
    
    def process_all_commits(self):
        """Process all commits"""
        self.stats['start_time'] = datetime.now()
        start_commit = self.progress.completed_commits + 1
        remaining = self.progress.get_remaining(self.config.TOTAL_COMMITS)
        
        print(f"\n{'*'*60}")
        print(f"Starting batch commit process")
        print(f"Target: {self.config.TOTAL_COMMITS} total commits")
        print(f"Already completed: {self.progress.completed_commits}")
        print(f"Remaining: {remaining}")
        print(f"Estimated time: ~{remaining * self.config.MIN_DELAY_SECONDS / 3600:.2f} hours")
        print(f"{'*'*60}\n")
        
        for commit_num in range(start_commit, self.config.TOTAL_COMMITS + 1):
            if self.stop_flag:
                print("\nProcess stopped by user")
                break
            
            # Create commit
            success = self.create_commit(commit_num)
            
            if success:
                # Push in batches
                self.push_if_needed(commit_num)
            else:
                print(f"Commit #{commit_num} failed, retrying...")
                time.sleep(2)  # Wait before retry
                # Simple retry logic
                for retry in range(3):
                    if self.create_commit(commit_num):
                        break
                    time.sleep(5 * (retry + 1))
        
        # Final push
        print("\nFinal push of all commits...")
        self.git.push()
        
        # Final statistics
        self.print_final_stats()
    
    def print_final_stats(self):
        """Print final statistics"""
        elapsed = datetime.now() - self.stats['start_time']
        print(f"\n{'='*60}")
        print("FINAL STATISTICS")
        print(f"{'='*60}")
        print(f"Total commits attempted: {self.config.TOTAL_COMMITS}")
        print(f"Successful commits: {self.stats['commits_done']}")
        print(f"Failed commits: {self.stats['failed_commits']}")
        print(f"Total pushes: {self.stats['push_count']}")
        print(f"Total time: {elapsed}")
        if self.stats['commits_done'] > 0:
            avg_speed = self.stats['commits_done'] / elapsed.total_seconds()
            print(f"Average speed: {avg_speed:.2f} commits/second")
        print(f"{'='*60}")
    
    def stop(self):
        """Stop the processing"""
        self.stop_flag = True