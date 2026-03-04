"""
Safety mechanisms to prevent GitHub blocks
"""

import time
import datetime
from collections import deque
from threading import Lock

class RateLimiter:
    def __init__(self, max_commits_per_hour=1000, min_delay=0.5):
        self.max_commits_per_hour = max_commits_per_hour
        self.min_delay = min_delay
        self.commit_timestamps = deque(maxlen=max_commits_per_hour)
        self.lock = Lock()
        self.last_commit_time = 0
    
    def can_commit(self):
        """Check if we can make another commit based on rate limits"""
        with self.lock:
            now = time.time()
            
            # Check minimum delay between commits
            if now - self.last_commit_time < self.min_delay:
                return False
            
            # Remove timestamps older than 1 hour
            one_hour_ago = now - 3600
            while self.commit_timestamps and self.commit_timestamps[0] < one_hour_ago:
                self.commit_timestamps.popleft()
            
            # Check if we've exceeded hourly limit
            if len(self.commit_timestamps) >= self.max_commits_per_hour:
                return False
            
            return True
    
    def wait_if_needed(self):
        """Wait until we can make another commit"""
        while not self.can_commit():
            time.sleep(1)  # Check every second
        
        with self.lock:
            now = time.time()
            self.commit_timestamps.append(now)
            self.last_commit_time = now
    
    def get_stats(self):
        """Get current rate limit statistics"""
        with self.lock:
            now = time.time()
            one_hour_ago = now - 3600
            commits_last_hour = sum(1 for t in self.commit_timestamps if t > one_hour_ago)
            return {
                'commits_last_hour': commits_last_hour,
                'max_per_hour': self.max_commits_per_hour,
                'remaining_this_hour': self.max_commits_per_hour - commits_last_hour
            }

class ProgressTracker:
    """Tracks commit progress to allow resume after interruption"""
    
    def __init__(self, progress_file):
        self.progress_file = progress_file
        self.completed_commits = self.load_progress()
    
    def load_progress(self):
        """Load progress from file"""
        try:
            with open(self.progress_file, 'r') as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return 0
    
    def save_progress(self, count):
        """Save progress to file"""
        with open(self.progress_file, 'w') as f:
            f.write(str(count))
        self.completed_commits = count
    
    def increment(self):
        """Increment commit count"""
        self.completed_commits += 1
        self.save_progress(self.completed_commits)
        return self.completed_commits
    
    def get_remaining(self, total):
        """Get remaining commits"""
        return max(0, total - self.completed_commits)