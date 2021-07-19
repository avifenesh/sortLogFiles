# Made by Avi Fenesh
# 15.07.2021
# class of log file


import re
from datetime import datetime
import linecache


# log contain path to the file of the log, line for the line un the file contain the log, and time_stamp for the value
class Log:
    def __init__(self, path):
        self.path = path
        self.line = 0
        self.time_stamp = get_time_stamp(self.path)

    # return line and and update to next lin
    def get_line(self):
        return_line = linecache.getline(self.path, self.line)
        self.line += 1
        current_line = linecache.getline(self.path, self.line)
        # check if last line, then check if has time-stamp, if not the line is part of the previews
        if current_line:
            while True:
                try:
                    self.time_stamp = datetime.strptime(
                        re.search("(?P<date>\d{4}[-]?\d{1,2}[-]?\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}[,]?\d{1,3})",
                                  current_line).group(), "%Y-%m-%d %H:%M:%S")
                    break
                except AttributeError:
                    return_line += current_line
                    self.line += 1
                    current_line = linecache.getline(self.path, self.line)

            return return_line, False  # return false if it isn't the last line, true if it is
        else:
            return return_line, True


def get_time_stamp(path):
    with open(path) as f:  # get the time stamp of the current line and the last line of the file
        first_line = f.readline()
        # search the time stamp pattern
        time_stamp = datetime.strptime(
            re.search("(?P<date>\d{4}[-]?\d{1,2}[-]?\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}[,]?\d{1,3})",
                      first_line).group(), "%Y-%m-%d %H:%M:%S")
        f.close()
    return time_stamp