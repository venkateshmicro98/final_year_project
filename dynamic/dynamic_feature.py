import time
import pandas as pd
import os
import subprocess
from adb.client import Client as AdbClient
import numpy as np

#1. Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")
#end 1

def dynamic_feature_vector(total_syscall_list,total_syscall_list_length,current_APK,APK_path,APK_name):
    
    #3 extracting package name of APK file and writing to package_name.txt
    os.system('/home/venkatesh/fyp/github/final_year_project/dynamic/package_name.sh ' + current_APK)
    #end 3


    #4 extracting package name of APK file from package_name.txt
    f = open("/home/venkatesh/fyp/github/final_year_project/dynamic/package_name.txt", "r")
    word = f.read().split()
    package_name = word[0]
    print("Package Name : " + package_name)
    f.close()
    #end 4

    if(device.is_installed(package_name)):
        status = device.uninstall(package_name)
        print("Uninstalled")
    
    try:
        status = device.install(current_APK)
        print(status)
        print("Installed")
    except :
        
        APK_path_name = APK_path + APK_name
        print("Printing Error for " + APK_path_name)
     #   deleter = "rm " + APK_path_name
      #  deleter_log = os.popen(deleter).read()    
       # print(deleter_log)
        #os.system('/home/venkatesh/fyp/github/final_year_project/dynamic/remove_apk.sh ' + APK_path_name)

    #5 Initializing application 
    random_events_cmd = "adb shell monkey -p " + package_name + " -v 1"
    print("Initialising Command " + random_events_cmd)
    random_events_log = os.popen(random_events_cmd).read()
    print(random_events_log)
    #end 5

    time.sleep(1)
    #6 Extracting Process ID
    grep_cmd = "adb shell ps | grep " + "'"+ package_name +"'"
    print("Process ID Extraction Command " + grep_cmd)
    proc_id = os.popen(grep_cmd).read()
    if(proc_id == ""):
        print("Error!!!")
    print("Returned Process ID /" + proc_id + "/")
    proc_id = (proc_id.split(' ')) 
    print("Underprocessing Processing Process ID :")
    print(proc_id)
    if(proc_id[3] != ''):
        proc_id = int(proc_id[3])
    else:
        proc_id = int(proc_id[4])
    print("Process ID :" + str(proc_id))
    #end 6

    #7 exporting Process to process_ID.txt
    f = open("/home/venkatesh/fyp/github/final_year_project/dynamic/process_ID.txt", "w")
    f.write(str(proc_id)) 
    f.close()
    #end 7

    #8.1 
    #strace_function = subprocess.call('python3 strace_shell.py',shell=True)
    strace_function = subprocess.Popen(["python3","/home/venkatesh/fyp/github/final_year_project/dynamic/strace_shell.py"])
    #end 8.1

    #8.2 generating random events
    random_event_count = 1000
    random_events_cmd = "adb shell monkey -p "+package_name + " -v " + str(random_event_count)
    print("Random Events Command " + random_events_cmd)
    random_events_log = os.popen(random_events_cmd).read()
    #end 8.2  

    #9 killing application process
    kill_cmd ="adb shell kill -SIGKILL " + str(proc_id)
    os.system(kill_cmd)
    #end 9

    #10 Time to write to file by strace_shell.py 
    time.sleep(2)
    #end 10

    #print(random_events_log)
    
    #11 extracting system calls from log.csv
    log_csv = pd.read_fwf('/home/venkatesh/fyp/github/final_year_project/dynamic/log.csv')
    log_csv.columns = ["usecs_col","calls_col","errors_col","syscall_col"] 
    print(log_csv)
    log_csv = log_csv['syscall_col']
    log_csv = log_csv.drop(log_csv.index[0])
    log_csv = log_csv.drop(log_csv.index[0])
    log_csv = log_csv[:-2]
        #print(log_csv)
    #end 11


    #12 Exporting to extracted_syscall.csv  
    log_csv.to_csv("/home/venkatesh/fyp/github/final_year_project/dynamic/extracted_syscall.csv", sep='\t', index=False)
    #end 12

    files_count = 1
    #initialising permission vector
    syscall_vector = np.zeros((1,total_syscall_list_length),dtype = int)
    #print(permissions_vector)


    extracted_syscall_path = "/home/venkatesh/fyp/github/final_year_project/dynamic/"
        
    extracted_syscall_file = "extracted_syscall.csv"

    #converting text extracted_syscall to list
    with open(extracted_syscall_path + extracted_syscall_file) as f:
        extracted_syscall_list = f.read().splitlines()

    #number of extracted_syscall in extracted_syscall list
    extracted_syscall_list_length = len(extracted_syscall_list)

    print(" List : " + str(extracted_syscall_list))
    print("Length of extracted_syscall list : " + str(extracted_syscall_list_length))

    #sorting list to optimise the matching 
    extracted_syscall_list.sort()


    cur_index = 0

    for syscall in extracted_syscall_list:
                    print (syscall)
                    for index,current_syscall in enumerate(total_syscall_list):
                        if(current_syscall == syscall):
                            print(index,current_syscall)
                            syscall_vector[0,index] = 1

    print(syscall_vector)
    

    status = device.uninstall(package_name)
    print("Uninstalled")
    
    
    return syscall_vector