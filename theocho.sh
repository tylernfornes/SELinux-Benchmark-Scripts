#!/bin/bash
#Author: Tyler Fornes
#Filename: theocho.sh
#Function: Shell script to control switcheroo.py and perform word count of replaced word
#Adpated from: http://unix.stackexchange.com/questions/2244/how-do-i-count-the-number-of-occurrences-of-a-word-in-a-text-file-with-the-comma
args=("$@")

#find replaced word, remove space and place on new line, count line
tr ' ' '\n' < lol.html | grep ${args[0]} | wc -l > /dev/null
