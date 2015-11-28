#!/usr/bin/env python
#Author: Tyler Fornes
#Filename: switcheroo.py
#Function: Clones specified webpage to local copy and replaces a specified word with a given replacement

import sys
import urllib2

def getter():
	response = urllib2.urlopen(sys.argv[1])
	html = response.read()
	return html

def reader():
	file = open('lol.html', 'r')
	read_html = file.read()
	file.close()
	return read_html

def replacer(html):
	new_html=html.replace(sys.argv[2], sys.argv[3])
	return new_html

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

if __name__ == "__main__":
	main()
