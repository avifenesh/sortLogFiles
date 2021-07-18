# Made by Avi Fenesh
# 15.07.2021
# main program
# get input of path to the file of log files
# create logFile object for every file
# create min heap and inserting the logFile objects
# returning the minimum one by one and inserting to new log file

from minHeap import MinHeap
from logFile import LogFile
import os

# get the path from the user
path = input("please add the path to the directory of the log file")

# check if valid path
if not os.path.exists(path):
    print("path do not exist, please try again with exist file")

# use os to get list of directory in this file
files = os.listdir(path)

# find the log file and add the path, than add it to new list
list_of_file = []
for file in files:
    if ".log" in file:
        file = path + "/" + file
        list_of_file.append(file)

# creating min heap with the num of file size
logMinHeap = MinHeap(len(list_of_file))

# creating from the file logFile objects and inserting to the min heap
for file in list_of_file:
    f = LogFile(file)
    logMinHeap.insert(f)

# get the min value one by one from the min heap and write it to the file
with open('newLogFile.log', 'w') as new_log_file:
    while logMinHeap.size > 0:
        line = logMinHeap.remove()
        new_log_file.write(line)
    new_log_file.close()
