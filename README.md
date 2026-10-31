# sortLogFiles
## Algorithm for sort multiple sorted log-files into one sorted log-file base on time-stamp

The main idea behind the algorithm: <br />
Create objects from every file, every object contain the index of the current comparing line, time-stamp of the the line and path to the file. <br />
Create min heape base on time-stamp value and insert all the log-file objects. <br />
Then pop the min and insert it to a new file.<br />
After popping a line to the new file, get the next line of the file object and heapify the object to the right place base on the new time-stamp value.<br />
<br />
## How to use:<br />
Pull repo to your machine. <br />
Open command line and navigate to the repo directory. <br />
Write in the command line: python main.py -d [path-to-log-files]<br />
If the path containing white spaces encapsulate the path by quotation marks. <br />
Only files ending in `.log` in that directory are read. <br />
Each log entry needs a time-stamp like `2021-07-15 13:45:10`. A line without one stays with the entry above it. <br />
The sorted output is written to `newLogFile.log` in the current directory. <br />
