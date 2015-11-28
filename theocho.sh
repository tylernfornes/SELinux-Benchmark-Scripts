#!/bin/bash
#Author: Tyler Fornes
#Filename: theocho.sh
#Function: Shell script to control switcheroo.py and perform word count of replaced word
#Adpated from: http://unix.stackexchange.com/questions/2244/how-do-i-count-the-number-of-occurrences-of-a-word-in-a-text-file-with-the-comma
args=("$@")
x=1
#run python script with arguments	to grab website and replace words
`python switcheroo.py ${args[0]} ${args[1]} ${args[2]}`
#run eight times, in accordance to benchmark tests
while [ $x -le 8 ]
do
  #find replaced word, remove space and place on new line, count line
  echo `tr ' ' '\n' < lol.html | grep ${args[2]} | wc -l`
  x=$(( $x + 1 ))
done