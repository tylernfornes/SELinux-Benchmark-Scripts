#!/usr/bin/python
#Author: Tyler Fornes
#Filename: pipeparty.py
#Adpated from: http://timmurphy.org/2013/11/11/using-fifos-in-python/
#Function: Process B to exhange integer in file
import os
import sys

#path to integer file
path = "test.txt"
#open file for reading, read increasing integer
reader = open(path, "r")
for num in reader:
    print "Received: " + num,
reader.close()
#open file for writing, write increasing integer
writer = open(path, "w")
writer.write(sys.argv[1])
writer.close()