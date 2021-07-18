# Made by Avi Fenesh
# 15.07.2021
# class of log file

import re
from datetime import datetime
import linecache


# class for log files -
# contain path to the file, line for the next line we want to compare, and time_stamp for the value
class LogFile:
    def __init__(self, path):
        self.path = path  # save the path of the log file
        self.line = 0  # for knowing in which line are we compare
        with open(path) as f:  # get the time stamp of the current line and the last line of the file
            first_line = f.readline()
            # search the time stamp pattern
            self.time_stamp = datetime.strptime(
                re.search("(?P<date>\d{4}[-]?\d{1,2}[-]?\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}[,]?\d{1,3})",
                          first_line).group(), "%Y-%m-%d %H:%M:%S")
            f.close()

    def get_line(self):  # returning the line and get the next one
        ret_line = linecache.getline(self.path, self.line)
        self.line += 1
        current_line = linecache.getline(self.path, self.line)

        if current_line:  # check this is not the last line
            while True:  # if there few lines for the same log, connect them to one
                try:  # search the time stamp pattern, if there no time stamp the line is part of the previous log
                    self.time_stamp = datetime.strptime(
                        re.search("(?P<date>\d{4}[-]?\d{1,2}[-]?\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}[,]?\d{1,3})",
                                  current_line).group(), "%Y-%m-%d %H:%M:%S")
                    break
                except:  # connect between lines of the same log and check the next
                    ret_line += current_line
                    self.line += 1
                    current_line = linecache.getline(self.path, self.line)

            return ret_line, 1  # return the line and 1 if it isn't the last line
        else:
            return ret_line, 0  # return the line and 0 if the last line of the file

    def get_time_stamp(self):
        return self.time_stamp
