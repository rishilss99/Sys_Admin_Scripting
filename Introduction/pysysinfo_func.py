#!/usr/bin/env python3
#A System Information Gathering Script
#System Information Gathering Script
import subprocess

#Command 1
def uname_func():

    uname = "uname"
    uname_arg = "-a"
    print ("Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])

#Command 2
def disk_func():

    diskspace = "df"
    diskspace_arg = "-h"
    print ("Gathering diskspace information %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])

#Command 3
def tmp_space():
    
    print("Space used in /tmp directoy\n")
    subprocess.call("du -h ~/Desktop", shell=True)

#Main function that call other functions
def main():
    uname_func()
    disk_func()
    tmp_space()

if __name__ == "__main__":
    main()