# LVM Management System

## Overview

The LVM Management System is a command-line interface (CLI) tool for managing Logical Volume Manager (LVM) on Linux systems. This system allows users to perform various tasks related to managing disks, partitions, physical volumes, volume groups, and logical volumes (LVM). The tool simplifies tasks such as creating, extending, and deleting volumes, formatting and mounting LVMs, and more. Additionally, it provides disk usage monitoring and automatic cleanup functionalities.

## Features

The tool provides the following functionalities:

1. **Check Disk Information**: View details about the disk partitions on your system.
2. **Create a Partition**: Use GParted to create new partitions.
3. **Create a Physical Volume (PV)**: Create a physical volume on a disk.
4. **Create a Volume Group (VG)**: Create a volume group from one or more physical volumes.
5. **Create, Format, Mount LVM**: Create a logical volume, format it, and mount it to a specified directory.
6. **Extend LVM**: Increase the size of an existing logical volume.
7. **Display Physical Volumes**: Display details of all physical volumes.
8. **Display Volume Groups**: Display details of all volume groups.
9. **Display Logical Volumes**: Display details of all logical volumes.
10. **Delete Logical Volume**: Delete a specified logical volume.
11. **Delete Volume Group**: Delete a specified volume group.
12. **Delete Physical Volume**: Delete a specified physical volume.
13. **Monitor Disk Usage**: Monitor the disk usage of specified volumes and automatically extend them when usage exceeds a set threshold.
14. **Delete Old Files**: Automatically delete files older than a certain period to free up disk space.
15. **Exit**: Exit the tool.

## Requirements

- Python 3.x
- `os`, `sys`, `time`, `psutil`, `pyfiglet`, `termcolor` Python modules.
- Linux system with LVM installed.

## Usage

1. Clone or download the repository.
2. Run the script:
   ```bash
   python3 lvm_management_system.py
# LVM Management System

This tool provides an interface for managing Logical Volume Management (LVM) on a Linux system. It allows you to create, manage, and monitor logical volumes, physical volumes, and volume groups.

## Available Options

1. **Check Disk Information**: Lists all disk partitions using `fdisk -l`.
2. **Create a Partition**: Opens GParted to create a new partition.
3. **Create a Physical Volume**: Prompts for a disk name and creates a physical volume on that disk.
4. **Create a Volume Group**: Prompts for the name of the volume group and disk names to create a volume group.
5. **Create, Format, Mount LVM**: Prompts for volume group name, LVM name, size, and mount point. Creates a logical volume, formats it as ext4, and mounts it at the specified directory.
6. **Extend LVM**: Increases the size of an existing logical volume.
7. **Display Physical Volumes**: Displays details of all physical volumes using `pvdisplay`.
8. **Display Volume Groups**: Displays details of all volume groups using `vgdisplay`.
9. **Display Logical Volumes**: Displays details of all logical volumes using `lvdisplay`.
10. **Delete Logical Volume**: Removes a specified logical volume.
11. **Delete Volume Group**: Removes a specified volume group.
12. **Delete Physical Volume**: Removes a specified physical volume.
13. **Monitor Disk Usage**: Monitors the disk usage of specified logical volumes and automatically extends them if their usage exceeds the defined threshold. The script checks disk usage every minute and extends the logical volume by 10GB when the usage exceeds 80%.
14. **Delete Old Files**: Periodically deletes files older than 2 hours from specified directories (`/mnt/lv1`, `/mnt/lv2`) to free up space. This helps manage disk usage by automatically cleaning up older files.
15. **Exit**: Exits the tool and terminates the script.

---

## Features

### Monitoring Disk Usage and Auto-Extension
The `monitor_partitions` function continuously monitors disk usage for the logical volumes `/mnt/lv1` and `/mnt/lv2`. If the usage exceeds a defined threshold (set to 80% by default), it automatically triggers the `extend_partition` function to extend the logical volume by 10GB and resize the filesystem. This ensures that disk space is managed effectively without requiring manual intervention.

**How it works:**
- The script checks disk usage every 60 seconds.
- If usage exceeds the threshold, it triggers the command to extend the logical volume and resize the filesystem.
- This process runs indefinitely until the script is terminated.

### Auto-Delete Old Files
The `delete_old_files` function automatically deletes files older than 2 hours from the specified directories (`/mnt/lv1`, `/mnt/lv2`). This helps to free up disk space by removing old and unnecessary files.

**How it works:**
- The script checks the modification time of each file in the specified directories.
- If a file is older than the 2-hour threshold, it is deleted automatically.

---

## Example Usage

1. **Check Disk Information**
   - Choose option `1` to list all disk partitions using `fdisk -l`.
   
2. **Monitor Disk Usage and Auto-Extension**
   - Choose option `13` to start monitoring disk usage and automatically extend logical volumes when usage exceeds 80%.
   
3. **Auto-Delete Old Files**
   - Choose option `14` to start deleting files older than 2 hours from specified directories (`/mnt/lv1`, `/mnt/lv2`).

4. **Exit the Tool**
   - Choose option `15` to exit the tool.

---

## Requirements

- Linux-based operating system with LVM installed.
- `fdisk`, `vgdisplay`, `lvdisplay`, `pvdisplay`, `resize2fs` commands must be available.
- GParted for partition creation (if needed).

---



