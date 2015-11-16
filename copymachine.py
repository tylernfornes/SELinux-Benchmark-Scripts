#!/usr/bin/env python
#Author: Tyler Fornes
#Filename: copymachine.py
#Function: Compares time taken to copy file when SELinux is enforcing/disabled

import os
import sys
import time

def createFile(size):
	os.system("dd" + " if=/dev/zero" + " of=test.txt" + " bs=" + str(size) + " count=1") 

def dragRace(copies):
	start = time.time()
	for x in xrange(0,int(copies)):
		os.system("cp" + " test.txt" + " copy" + str(x) + ".txt")
	end = time.time()
	os.system("rm copy*.txt")
	return end - start

def enforcing(switch):
	os.system("setenforce " + str(switch))

def main():
	#get file size, create test file of size
	file_size=sys.argv[1]
	createFile(file_size)
	
	#ensures SELinux is enforcing
	enforcing(1)
	
	#determines how many copies user requires
	num_copies=sys.argv[2]
	num_copies = int(num_copies)
	
	#copies file, times how long it takes
	time = dragRace(num_copies)
	avg_time = time/num_copies
	print "Total time to copy while SELinux enforcing:" + str(time) + " seconds"
	print "Average time for a file to copy:" + str(avg_time) + " seconds"

	#ensures SELinux is disabled
	enforcing(0)

	#copies file, times how long it takes
	time = dragRace(num_copies)
	avg_time = time/num_copies
	os.system("rm test.txt")
	print "Total time to copy while SELinux disabled:" + str(time) + " seconds"
	print "Average time for a file to copy:" + str(avg_time) + " seconds"

if __name__ == "__main__":
	main()
