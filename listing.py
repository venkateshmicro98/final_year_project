
import static_feature as st
import dynamic.dynamic_feature as dy

import os
import numpy as np
from androguard.core.bytecodes.apk import APK

#paths and filenames
benignware_path  = "/home/venkatesh/fyp/sample_apk/"
permissions_path = "/home/venkatesh/fyp/github/final_year_project/"
permissions_file = "list_of_permissions.txt"
total_syscall_path = "/home/venkatesh/fyp/github/final_year_project/"    
total_syscall_file = "list_of_syscalls.txt"


#number of application in benignware
files_count = len(os.listdir(benignware_path))
print ("Total no. of benignware files : " + str(files_count))

#converting text permission to list
with open(permissions_path + permissions_file) as f:
    permissions_list = f.read().splitlines()


#number of permissions in permission list
permissions_list_length = len(permissions_list)

static_vector = np.zeros((0,permissions_list_length),dtype = int)

#dynamic

#converting text extracted_syscall to list
with open(total_syscall_path + total_syscall_file) as f:
    total_syscall_list = f.read().splitlines()

#number of extracted_syscall in extracted_syscall list
total_syscall_list_length = len(total_syscall_list)

print("Total List : " + str(total_syscall_list))
print("Length of total_syscall list : " + str(total_syscall_list_length))

#sorting list to optimise the matching 
total_syscall_list.sort()

total_vector = np.zeros((0,(permissions_list_length + total_syscall_list_length)),dtype = int)

# read the entries
with os.scandir(benignware_path) as listOfEntries:  
    for appln_num,entry in enumerate(listOfEntries):
        # Application Number
        print (appln_num)
        if entry.is_file():
            #application file name
            print(entry.name)