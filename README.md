# SELinux Benchmark Scrips

A collection of scripts to test SELinux performance when transferring data.

## Usage

### copymachine.py
Compares the difference in time when a file is copied when SELinux is enforcing vs. when SELinux is permissive.

Takes two arguments:

1. file size
2. number of copies to be created

Example:

copymachine.py 4k 200 - creates 4KB file to be copied 200 times


