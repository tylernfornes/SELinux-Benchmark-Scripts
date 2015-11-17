#!/usr/bin/env python

import os
import sys

def enforcing(switch):
	os.system("setenforce " + str(switch))

def plumber(b_size):
	os.system("dd if=/dev/urandom bs=" + b_size + " count=500000 | pv -a | dd of=flush.txt")
	os.system("rm flush.txt")

def main():
	#grab block size from argument
	block_size = file_size=sys.argv[1]
	#ensure SELinux is enforcing, write file, get avg. speed
	enforcing(1)
	plumber(block_size)
	#ensure SELinux is set to permissive, write file, get avg. speed
	enforcing(0)
	plumber(block_size)

if __name__ == "__main__":
	main()