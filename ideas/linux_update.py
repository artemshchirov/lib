import os
import time

os.system("clear")
print("\n\tFetching updates:\n")
time.sleep(1)
os.system("sudo apt update -y")
time.sleep(2)

print("\n\tUpdating system:\n")
time.sleep(1)
os.system("sudo apt upgrade -y")
time.sleep(2)

print("\n\tUpgrading distro:\n")
time.sleep(1)
os.system("sudo apt dist-upgrade -y")
time.sleep(2)

print("\n\tRemoving temporary packages:\n")
time.sleep(1)
os.system("sudo apt autoremove -y")
time.sleep(2)

print("\n\tSystem now fully upgraded...\n")
