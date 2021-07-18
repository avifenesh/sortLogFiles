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


def main():
    # get the path from the user
    path = input("please add the path to the directory of the log file \n")

    # check if valid path
    while not os.path.exists(path):
        print("path do not exist, please try again with exist file ")
        path = input("please add the path to the directory of the log file\n")

    # use os to get list of directory in this file
    files = os.listdir(path)

    # find the log file and add the path, than add it to new list
    list_of_file = []
    for file in files:
        if file.endswith(".log"):
            file = os.path.join(path, file)
            list_of_file.append(file)

    # creating min heap with the num of file size
    log_min_heap = MinHeap(len(list_of_file))

    # creating from the file logFile objects and inserting to the min heap
    for file in list_of_file:
        f = LogFile(file)
        log_min_heap.insert(f)

    # get the min value one by one from the min heap and write it to the file
    with open('newLogFile.log', 'w') as new_log_file:
        while log_min_heap.size > 0:
            line = log_min_heap.remove()
            new_log_file.write(line)
        new_log_file.close()


if __name__ == '__main__':
    main()
