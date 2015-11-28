#!/usr/bin/env python
#Author: Tyler Fornes
#Filename: ochomaster.py
#Function: Grabs and gets specified URL Calls the ocho eight times repeadedly until timer expires, counts times completed

import os
import sys
import time
import urllib2

def enforcing(switch):
	os.system("setenforce " + str(switch))

def getRunTime(sec):
	timer = time.time() + int(sec)
	return timer

def getter():
	response = urllib2.urlopen(sys.argv[2])
	html = response.read()
	return html

def reader():
	file = open('lol.html', 'r')
	read_html = file.read()
	file.close()
	return read_html

def replacer(html):
	new_html=html.replace(sys.argv[3], sys.argv[4])
	return new_html

def run(seconds):
	run_count = 0
	while time.time() < seconds:
		for x in range(0, 8):
			os.system("sh ./theocho.sh " + sys.argv[4] +"&")
		run_count += 1
	return run_count

def writer(text):
	file = open("lol.html", "w")
	file.write(text)
	file.close()

def main():

	#grabs copy of webpage specified by user
	html_text = getter()
	#writes html text to file lol.html
	writer(html_text)
	#reads in text from lol.html
	copy_html = reader()
	#sends text to be processed for word replacement
	lol_html = replacer(copy_html)
	#writes replaced text to lol.html 
	writer(lol_html)

	#grabs time to run from argument
	timer = sys.argv[1]
	
	#ensures SELinux is enforcing, gets timer, runs shell scripts
	enforcing(1)
	run_time = getRunTime(timer)
	count = run(run_time)
	print "Number of times executed when SELinux is enforcing: " + str(count)

	#ensures SELinux is permissive, gets timer, runs shell scripts
	enforcing(0)
	run_time = getRunTime(timer)
	count = run(run_time)
	print "Number of times executed when SELinux is permissive: " + str(count)
	
if __name__ == "__main__":
	main()
