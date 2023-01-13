import os
import sys
import psutil
import subprocess

def check_usb():
    for drive in psutil.disk_partitions():
        if drive.fstype == 'vfat' or drive.fstype == 'ntfs':
            if 'removable' in drive.opts:
                return drive.device
    return None

base_path = check_usb()
if base_path is None:
    print("No external USB drive found.")
    sys.exit()
else:
    user_response = input(f"An external USB drive has been found at {base_path}. Is this the correct path to use as "
                          f"the base path? (y/n)")
    if user_response.lower() != 'y':
        print("Exiting...")
        sys.exit()

if len(sys.argv) != 2:
    print("Usage: python script.py subdirectory")
    sys.exit()

path = os.path.join(base_path, sys.argv[1])

if not os.path.isdir(path):
    print(f"{path} is not a valid directory")
    sys.exit()

files = os.listdir(path)

for index, file in enumerate(sorted(files, key=lambda x: os.path.getctime(os.path.join(path, x)))):
    os.rename(os.path.join(path, file), os.path.join(path, str(index+1) + '_' + file))

# Start the "Movies & TV" application and open the specified directory
subprocess.run(["start", "movies & tv", path], shell=True)
