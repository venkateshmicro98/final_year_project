
import static_feature as st
import dynamic.dynamic_feature as dy

import os
import numpy as np
from androguard.core.bytecodes.apk import APK

#paths and filenames
Appln_Path  = "/home/venkatesh/fyp/sample_apk/"    
mal_Appln_Path = "/home/venkatesh/fyp/mal_sample_apk/"
permissions_path = "/home/venkatesh/fyp/github/final_year_project/"
permissions_file = "list_of_permissions.txt"
total_syscall_path = "/home/venkatesh/fyp/github/final_year_project/"    
total_syscall_file = "list_of_syscalls.txt"


#number of application in benignware
files_count = len(os.listdir(Appln_Path))
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
#total_vector = np.zeros((0,(permissions_list_length)),dtype = int)

# read the entries
with os.scandir(Appln_Path) as listOfEntries:  
    for appln_num,entry in enumerate(listOfEntries):
        # Application Number
        print (appln_num)
        if entry.is_file():
            #application file name
            print(entry.name)
            current_APK = Appln_Path + entry.name

            current_static_vector = st.static_feature_vector(permissions_list,permissions_list_length,current_APK)
            current_dynamic_vector = dy.dynamic_feature_vector(total_syscall_list,total_syscall_list_length,current_APK,Appln_Path,entry.name)
            #current_dynamic_vector = current_static_vector
            print("Current Static vector : ")
            print(current_static_vector[0])
            print("Current Dynamic vector : ")
            print(current_dynamic_vector[0])

            current_total_vector = np.append(current_static_vector,current_dynamic_vector)
            
            print("Current total vector : ")
            print(current_total_vector)
            current_total_vector.shape
            total_vector = np.vstack((current_total_vector,total_vector))
            #total_vector = np.vstack((current_static_vector,total_vector))
            print("Final Vector : ")
            print(total_vector)



    
binary_class = np.zeros((1,files_count),dtype = int)
print("Binary Class : ")
print(binary_class)

mal_total_vector = np.zeros((0,(permissions_list_length + total_syscall_list_length)),dtype = int)
#mal_total_vector = np.zeros((0,(permissions_list_length)),dtype = int)

mal_files_count = len(os.listdir(mal_Appln_Path))
with os.scandir(mal_Appln_Path) as listOfEntries:  
    for appln_num,entry in enumerate(listOfEntries):
        # Application Number
        print (appln_num)
        if entry.is_file():
            #application file name
            print(entry.name)
            current_APK = mal_Appln_Path + entry.name

            current_static_vector = st.static_feature_vector(permissions_list,permissions_list_length,current_APK)
            current_dynamic_vector = dy.dynamic_feature_vector(total_syscall_list,total_syscall_list_length,current_APK,mal_Appln_Path,entry.name)
            #current_dynamic_vector = current_static_vector
            print("Current Static vector : ")
            print(current_static_vector[0])
            print("Current Dynamic vector : ")
            print(current_dynamic_vector[0])

            current_total_vector = np.append(current_static_vector,current_dynamic_vector)
            
            print("Current total vector : ")
            print(current_total_vector)
            current_total_vector.shape
            mal_total_vector = np.vstack((current_total_vector,mal_total_vector))
            #mal_total_vector = np.vstack((current_static_vector,mal_total_vector))
            print("mal_Final Vector : ")
            print(mal_total_vector)



    
mal_binary_class = np.ones((1,mal_files_count),dtype = int)

print("Binary Class : ")
print(binary_class)


print("mal_Binary Class : ")
print(mal_binary_class)


final_perm_vector = np.vstack((total_vector,mal_total_vector))
print(final_perm_vector)
final_binary_class_vector = np.append(binary_class,mal_binary_class)
print(final_binary_class_vector)

np.savetxt('binary_class_vector.csv',(final_binary_class_vector))
np.savetxt('permission_vector.csv',(final_perm_vector))
print("Done")