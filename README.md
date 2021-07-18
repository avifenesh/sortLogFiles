# sortLogFiles
## Algorithm for sort multiple sorted log-files into one sorted log-file base on time-stamp

The main idea behind the algorithm: 
create objects from every file, every object contain the index of the current comparing line, time-stamp of the the line and path to the file 
create min heape base on time-stamp value and insert all the log-file objects 
then pop the min and insert it to a new file
after popping a line to the new file, get the next line of the file object and heapify the object to the right place base on the new time-stamp value.
