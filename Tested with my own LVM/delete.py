import os
import time

# Define the directories to clean up
directories = ['/mnt/lv1', '/mnt/lv2']

# Time threshold in seconds (2 hours)
time_threshold = 2 * 60 * 60

# Function to delete files older than the threshold
def delete_old_files(directory):
    current_time = time.time()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_mtime = os.path.getmtime(file_path)
            # Check if the file was modified within the last 2 hours
            if (current_time - file_mtime) <= time_threshold:
                try:
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    for directory in directories:
        delete_old_files(directory)

# Run delete.py every hour
#0 * * * * /usr/bin/python3 /path/to/delete.py
