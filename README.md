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

