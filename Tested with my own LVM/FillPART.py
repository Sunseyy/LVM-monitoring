import os
import random
import string
import time
import psutil

# Define the directories for the logical volumes (change to your actual mount points)
lv1_dir = '/mnt/lv1'
lv2_dir = '/mnt/lv2'

# Function to generate random data (using uniform distribution for simplicity)
def generate_random_data(size):
    # Generate random data based on a uniform distribution
    random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return random_data

# Function to print the current disk usage of a partition
def print_disk_usage(directory):
    usage = psutil.disk_usage(directory)
    print(f"Disk Usage for {directory}: {usage.percent}% - {usage.used / (1024 ** 3):.2f} GB used of {usage.total / (1024 ** 3):.2f} GB total")

# Function to fill the partitions with random data
def fill_partition(directory):
    data = generate_random_data(1024 * 1024 * 10)  # 10MB per write
    while True:
        with open(os.path.join(directory, 'random_data.txt'), 'a') as f:
            f.write(data)
        
        # Print the state of the partition after each write
        print(f"Writing 10MB of data to {directory}...")
        print_disk_usage(directory)
        
        time.sleep(10)  # Sleep for 10 seconds before writing more data

if __name__ == "__main__":
    while True:
        fill_partition(lv1_dir)
        fill_partition(lv2_dir)

#automate this in crontab:
#* * * * * /usr/bin/python3 /home/sunsey/FillPART.py

