#!/usr/bin/python3
import sys

# Iterate through the lines of input received from standard input (stdin) streaming
for line in sys.stdin:
    # Remove leading and trailing whitespaces from the input line
    line = line.strip()
    # Split the input line into key and value1 using the tab ('\t') as a delimiter
    key, value1 = line.split('\t', 1)
    # Print the key and value1, separated by a tab
    print(f'{key}\t{value1}')
    
    
