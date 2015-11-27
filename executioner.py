#!/usr/bin/env python

import os
import sys
import time

def enforcing(switch):
	os.system("setenforce " + str(switch))

def getRunTime(sec):
	timer = time.time() + int(sec)
	return timer

def executioner(seconds):
	proc_count = 0
	while time.time() < seconds:
		forkpid = os.fork()
		if forkpid == 0:
			os.system("exec ls /tmp > /dev/null")
			sys.exit()
		else:
			proc_count += 1
	return proc_count

def main():
	#grabs time to run from argument
	timer = sys.argv[1]
	
	#ensures SELinux is enforcing, gets timer, begins forking, runs exec statement
	enforcing(1)
	runtime = getRunTime(timer)
	enforce_count = executioner(runtime)
	print "Number of executions when SELinux is enforcing: " + str(enforce_count)

	#ensures SELinux is permissive, gets timer, begins forking, runs exec statement
	enforcing(0)
	runtime = getRunTime(timer)
	permissive_count = executioner(runtime)
	print "Number of executions when SELinux is permissive: " + str(permissive_count)

if __name__ == "__main__":
	main()