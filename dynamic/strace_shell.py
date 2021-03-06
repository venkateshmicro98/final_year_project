import pandas as pd
import subprocess
from subprocess import STDOUT, check_output
import os
import psutil

#1 Extracting process ID from process_ID.txt
f = open("/home/venkatesh/fyp/github/final_year_project/dynamic/process_ID.txt", "r")
proc_id = f.read().split()
print(proc_id)
proc_id = proc_id[0]
print("Process ID " + str(proc_id))
#end 1

#2 Logging Events
logger_cmd = "adb shell strace -p "+  str(proc_id) +" -c  > /home/venkatesh/fyp/github/final_year_project/dynamic/log.csv"
print("Logger Command " + logger_cmd)
proc = subprocess.call(logger_cmd,timeout=5,shell=True)
#end 2

print(proc)
