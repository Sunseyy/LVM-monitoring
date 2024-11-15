import os
import sys
from time import sleep
import pyfiglet
from termcolor import colored
from pyfiglet import figlet_format

while True:
    print("**************************************************************************************")
    print(colored(figlet_format("LVM MANGEMENT SYSTEM", "standard"), color='red'))
    print("**************************************************************************************")
    print("1] Check Disk Information")
    print("2] Create a Partition")
    print("3] Create a Physical Volume")
    print("4] Create a Volume Group")
    print("5] Create, Format, Mount LVM")
    print("6] Extend LVM")
    print("7] Display Physical Volumes")
    print("8] Display Volume Groups")
    print("9] Display Logical Volumes")
    print("10] Delete Logical Volume")
    print("11] Delete Volume Group")
    print("12] Delete Physical Volume")
    print("13] Exit")
    print()
    option = input("Select an option: ")

    if option == "1":
        os.system("fdisk -l")
        sleep(2)
    elif option == "2":
        os.system("gparted")
        sleep(2)

    elif option == "3":
        disk_name = input("Please specify the disk name: ")
        os.system(f"pvcreate {disk_name}")
        sleep(2)
    elif option == "4":
        vgname = input("Name of the Volume Group: ")
        disks = input("Please specify all the Disk Names (with spaces): ")
        os.system(f"vgcreate {vgname} {disks}")
        sleep(2)
    elif option == "5":
        vgname = input("Name of the Volume Group: ")
        lvmname = input("Name of the LVM: ")
        size = input("Enter the size: ")
        db = input("Create a Directory: Name it: ")
        os.system(f"mkdir /{db}")
        mount_point = input("Specify the Mount Point: ")
        os.system(f"lvcreate --size {size} --name {lvmname} {vgname}")
        os.system(f"mkfs.ext4 /dev/{vgname}/{lvmname}")
        os.system(f"mount /dev/{vgname}/{lvmname} {mount_point}")
        sleep(2)
    elif option == "6":
        vgname = input("Specify the name of the Volume Group: ")
        lvmname = input("Specify the name of the LVM: ")
        size = input("Size to be increased: ")
        os.system(f"lvextend --size +{size} /dev/{vgname}/{lvmname}")
        os.system(f"resize2fs /dev/{vgname}/{lvmname}")
        sleep(2)
    elif option == "7":
        os.system("pvdisplay")
        sleep(2)
    elif option == "8":
        os.system("vgdisplay")
        sleep(2)
    elif option == "9":
        os.system("lvdisplay")
        sleep(2)
    elif option == "10":
        vgname = input("Specify the name of the Volume Group: ")
        lvmname = input("Specify the name of the Logical Volume: ")
        os.system(f"lvremove /dev/{vgname}/{lvmname}")
        sleep(2)
    elif option == "11":
        vgname = input("Specify the name of the Volume Group: ")
        os.system(f"vgremove {vgname}")
        sleep(2)
    elif option == "12":
        pvname = input("Specify the name of the Physical Volume: ")
        os.system(f"pvremove {pvname}")
        sleep(2)
    elif option == "13":
        print("Exiting LVM Configuration... Please Wait...")
        sleep(2)
        break
    else:
        print("Invalid option, please try again.")
        sleep(2)
