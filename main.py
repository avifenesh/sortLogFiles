# Made by Avi Fenesh
# 15.07.2021
# main program
# get input of path to the file of log files
# create log object for every file
# create min heap and inserting the log objects
# returning the minimum one by one and inserting to new log file

from minHeap import MinHeap
from log import Log
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='Sort log files to one sorted log file.')
    parser.add_argument("-d", "--dmp", default=None, help='Path to log file, please encapsulate by quotation marks.')
    args = parser.parse_args()
    path = ''.join(args.dmp)
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")
    list_of_files = get_list_of_files(path)
    sort_list_log_file(list_of_files)


def get_list_of_files(path):
    files = os.listdir(path)
    # find the log file and add the path, than add it to new list
    list_of_file = []
    for file in files:
        if file.endswith(".log"):
            file_path = os.path.join(path, file)
            list_of_file.append(file_path)
    return list_of_file


def sort_list_log_file(list_of_files):
    # creating min heap with the num of file size
    log_min_heap = MinHeap(len(list_of_files))

    # creating from the file logFile objects and inserting to the min heap
    for file in list_of_files:
        f = Log(file)
        log_min_heap.insert(f)

    # get the min value one by one from the min heap and write it to the file
    with open('newLogFile.log', 'w') as new_log_file:
        while log_min_heap.size > 0:
            line = log_min_heap.remove()
            new_log_file.write(line)
        new_log_file.close()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


if __name__ == "__main__":
    main()
