import os
import psutil
import subprocess
import time

# Define the directories for the logical volumes (change to your actual mount points)
lv1_dir = '/mnt/lv1'
lv2_dir = '/mnt/lv2'

# Threshold for disk usage (percentage)
threshold = 80

# Function to check disk usage of a partition
def check_disk_usage(directory):
    usage = psutil.disk_usage(directory)
    return usage.percent

# Function to extend the logical volume if disk usage is above the threshold
def extend_partition(directory):
    print(f"Disk usage of {directory} is above threshold! Extending the partition...")
    # Run the command to extend the logical volume
    # Assuming lvextend command with a fixed amount (e.g., 10GB) or by 100% (use your preferred method)
    try:
        # Example of extending LV by 10GB (adjust this based on your setup)
        subprocess.run(['lvextend', '-L+10G', '/dev/vgname/lvname'], check=True)
        # After extending the volume, resize the filesystem
        subprocess.run(['resize2fs', '/dev/vgname/lvname'], check=True)
        print(f"Successfully extended the partition: {directory}")
    except subprocess.CalledProcessError as e:
        print(f"Error extending partition: {e}")

# Function to monitor and act based on disk usage
def monitor_partitions():
    while True:
        # Check disk usage for lv1 and lv2
        for directory in [lv1_dir, lv2_dir]:
            usage_percent = check_disk_usage(directory)
            print(f"Disk usage for {directory}: {usage_percent}%")
            
            if usage_percent > threshold:
                extend_partition(directory)
        
        # Wait for 60 seconds before checking again
        time.sleep(10)

if __name__ == "__main__":
    monitor_partitions()

#* * * * * /usr/bin/python3 /home/sunsey/monitor.py

