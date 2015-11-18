#!/usr/bin/python
#Author: Tyler Fornes
#Filename: pipeparty.py
#Adpated from: http://timmurphy.org/2013/11/11/using-fifos-in-python/
#Function: Process A to exhange integer in file
import os
import sys

#path to integer file, excepts "file exists" error
path = "test.txt"
try:
    os.mkfifo(path)
except OSError, e:
    if e.errno != 17:
        raise   
    pass
#open file for writing, write increasing integer
writer = open(path, "w")
value = sys.argv[1]
writer.write(value)
writer.close()
#open file for reading, read increasing integer
reader = open(path, "r")
for num in reader:
    print "Received: " + num,
reader.close()