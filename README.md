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

### executioner.py
Determines the amount of execl statements that can be processed in a given amount of time. Compares both times when 
SELinux is enforcing vs. when SELinux is permissive.

Takes one argument:

1. number of seconds to set timer

Example:

python executioner.py 10 - runs execl statement as many times as possible for ten seconds

### ochomaster.py
Control script for theocho.sh. Grabs the html from a given website and performs the replacement of a given word with another. Word analytics 
are then performed to determine how many times replaced word exists in file (theocho.sh). This is performed in a series of 8 identical instances 
of theocho.sh running concurrently. Ochomaster.py determines how many times this can occur in a specified amount of time.

Takes four arguments:

1. Number of seconds to set timer
2. Website to curl
3. Word to search and replace
4. Word to replace searched word

Example:

python ochomaster.py 10 http://gentoocloud.com cloud smog - Curls http://gentoocloud.com, replaced all instances of "cloud" with "smog" and runs 
for 10 seconds   
