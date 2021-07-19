# sortLogFiles
## Algorithm for sort multiple sorted log-files into one sorted log-file base on time-stamp

The main idea behind the algorithm: <br />
create objects from every file, every object contain the index of the current comparing line, time-stamp of the the line and path to the file. <br />
create min heape base on time-stamp value and insert all the log-file objects. <br />
then pop the min and insert it to a new file.<br />
after popping a line to the new file, get the next line of the file object and heapify the object to the right place base on the new time-stamp value.<br />
<br />
## How to use:<br />
pull repo to your machine. <br />
open command line and navigate to the repo directory. <br />
write in the command line: python main.py -d [path-to-log-files]<br />
if the path containing white spaces encapsulate the path by quotation marks. <br />
