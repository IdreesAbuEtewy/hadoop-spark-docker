#!/usr/bin/python3
import sys

# Initialize variables to keep track of the current word and its count
current_word = None
current_count = 0

# Iterate through the lines of input received from standard input (stdin) streaming
for line in sys.stdin:
   # Split the input line into word and count using the tab ('\t') as a delimiter
   word, count = line.strip().split("\t")
   
   # Check if the current word is the same as the previous one
   if current_word == word:
      current_count += int(count)  # If the same word, increment the count
   else:
      # If a new word is encountered or it's the first word
      if current_word:
         print(current_word + "\t" + str(current_count)) # Print the word and its accumulated count
      # Update the current word and count for the new word
      current_word = word
      current_count = int(count)

# After processing all lines, print the last word and its count
if current_word:
   print(current_word + "\t" + str(current_count))

