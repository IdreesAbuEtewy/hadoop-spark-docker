#!/usr/bin/python3
import sys

# Initialize an empty dictionary to store key-value pairs
dict = {}
# Iterate through the lines of input received from standard input (stdin) streaming
for line in sys.stdin:
    # Remove leading and trailing whitespaces from the input line
    line = line.strip()
    # Split the input line into key and value using the tab ('\t') as a delimiter
    key, value = line.split('\t', 1)
    
    # Check if the key is already present in the dictionary
    if key in dict.keys():
        # If the key exists, print the key, its stored value, and the new value - joining the 2 datasets. - key is the primary key connecting the tables.
        print(f"{key}\t{dict[key]}\t{value}")
    else:
        # If the key is not present, store the key-value pair in the dictionary
        dict[key] = value

