"""
Made by Avi Fenesh
15.07.2021
class of log file
"""

import re
from datetime import datetime
import linecache


# log-file contain path to the file, line for the next line we want to compare, and time_stamp for the value
class LogFile:
    def __init__(self, path):
        self.path = path
        self.line = 0
        self.time_stamp = time_stamp(self.path)

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

            return return_line, 1  # return 1 if it isn't the last line, 0 if it is
        else:
            return return_line, 0


def time_stamp(path):
    with open(path) as f:  # get the time stamp of the current line and the last line of the file
        first_line = f.readline()
        # search the time stamp pattern
        time_stamp = datetime.strptime(
            re.search("(?P<date>\d{4}[-]?\d{1,2}[-]?\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}[,]?\d{1,3})",
                      first_line).group(), "%Y-%m-%d %H:%M:%S")
        f.close()
    return time_stamp
