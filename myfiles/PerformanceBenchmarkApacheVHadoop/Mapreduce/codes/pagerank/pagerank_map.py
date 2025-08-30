#!/usr/bin/python3
import sys

# Iterate through the lines of input received from standard input (stdin) streaming
for line in sys.stdin:
   # Split the input line into node and neighbors using the tab ('\t') as a delimiter
   node, neighbors = line.strip().split("\t")
   # Split the neighbors into a list of neighbor nodes
   neighbors = neighbors.split(',')
   # Initialize the rank for the current node to 1.0
   rank = 1.0
   
   # Check if the current node has neighbors
   if neighbors:
      # Calculate the number of links from the current node
      num_links = len(neighbors)
      # Distribute the rank evenly among the neighbors and print the contributions
      for link in neighbors:
          contribution = rank/num_links
          print(f"{link}\t{contribution}")
