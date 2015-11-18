#!/usr/bin/python
#Author: Tyler Fornes
#Filename: pipemaster.py
#Function: Control program to send increasing integer between processes
import os
import sys
import time

def enforcing(switch):
	os.system("setenforce " + str(switch))

def party(runtime):
	#initial value to write to pipe
	value = 1
	while time.time() < runtime:
		os.system("python pipepartya.py " + str(value) + "&")
		value+=1
		os.system("python pipepartyb.py " + str(value))
		value+=1
	return value

def getRunTime(sec):
	timer = time.time() + int(sec)
	return timer

def printResults(results):
	print "Number of times executed: " + str(results - 1)

def main():	
	#time from user input
	seconds = sys.argv[1]

	#set timer in seconds based on parameter input
	timeout = getRunTime(seconds)
	#set SELinux to enforcing
	enforcing(1)
	#exchange increasing integer between processes
	total = party(timeout)
	#print number of times executed
	printResults(total)

	#set timer in seconds based on parameter input
	timeout = getRunTime(seconds)
	#set SELinux to permissive
	enforcing(0)
	#exchange increasing integer between processes
	total = party(timeout)
	#print number of times executed
	printResults(total)

if __name__ == "__main__":
	main()