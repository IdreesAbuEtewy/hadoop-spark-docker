#!/usr/bin/python3
import sys

# Get values from input dataset using streaming.
for line in sys.stdin:
    # split the line by each word
    words=line.strip().split()
    for word in words:
       #print(f'{word}\t1')
       print(word + "\t1")  # display every word and initial count as 1

