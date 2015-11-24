#!/usr/bin/env python
#Author: Tyler Fornes
#Filename: silverware.py
#Function: Compares number of processes created when SELinux is enforcing/permissive
#Adapted from: http://www.python-course.eu/forking.php

import os
import sys
import time

def enforcing(switch):
	os.system("setenforce " + str(switch))


def getRunTime(sec):
	timer = time.time() + int(sec)
	return timer

def utensil(seconds):
	proc_count = 0
	while time.time() < seconds:
		forkpid = os.fork()
		if forkpid == 0:
			sys.exit()
		else:
			proc_count += 1
	return proc_count

def main():
	#grabs time to run from argument
	timer = sys.argv[1]
	
	#ensures SELinux is enforcing, gets timer, begins forking
	enforcing(1)
	runtime = getRunTime(timer)
	enforce_count = utensil(runtime)
	print "Number of processes created when SELinux is enforcing: " + str(enforce_count)

	#ensures SELinux is permissive, gets timer, begins forking
	enforcing(0)
	runtime = getRunTime(timer)
	permissive_count = utensil(timer)
	print "Number of processes created when SELinux is permissive: " + str(enforce_count)

if __name__ == "__main__":
	main()