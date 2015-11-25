# SELinux Benchmark Scripts

A collection of scripts to test SELinux performance when transferring data.

## Usage

### copymachine.py
Compares the difference in time when a file is copied when SELinux is enforcing vs. when SELinux is permissive.

Takes two arguments:

1. file size
2. number of copies to be created

Example:

python copymachine.py 4k 200 - creates 4KB file to be copied 200 times

### plumbing.py
Monitors the average throughput of reading/writing data through a pipe when SELinux is enforcing vs. 
when SELinux is permissive. Requires *pv* utility to monitor data flow through pipe. 

Takes one argument:

1. amount of data to be transferred

Example:

python plumbing.py 512 - sends 512 bytes through the pipe

### pipepartymaster.py
Control script for pipepartya.py and pipepartyb.py (must be in same directory at runtime).

Controls two processes exchanging an increasing integer within a file, via a named pipe. Will run until
timer expires. Compares both when SELinux is enforcing vs. when SELinux is permissive.

Takes one argument:

1. number of seconds to set timer

Example:

python pipepartymaster.py 10 - will display how many times increasing integer was exchanged in 10 seconds

### silverware.py
Determines how many times a process can fork and exit in a given amount of time. Compares both times when
SELinux is enforcing vs. when SELinux is permissive.

Takes one argument:

1. number of seconds to set timer

Example:

python silverware.py 1 - will fork and exit as many times as possible in one second 
