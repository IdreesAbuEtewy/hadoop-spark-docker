#!/usr/bin/python3
import sys

# Initialize variables to keep track of the current node and its contributions
current_node = None
contributions = []

# Obtain the input directory from the command line arguments
input_dir = sys.argv[1]
with open(input_dir, "r") as f:
    # calculate the number of lines in dataset.
    num_lines = sum(1 for _ in f)

# Open the input file and count the number of lines
for line in sys.stdin:
    # Split the input line into node and value using the tab ('\t') as a delimiter
    node, value = line.strip().split("\t")
    # Convert the value to a floating-point number
    value = float(value)
    
    # Check if the current node is the same as the previous one
    if current_node == node:
        # If the same node, add the contribution to the list
        contributions.append(value)
    else:
        # If a new node is encountered or it's the first node
        if current_node:
            # Calculate the new rank for the current node based on contributions
            new_rank = 0.85 * sum(contributions) + 0.15
            # Normalize the rank by dividing it by the total number of lines
            r = new_rank/num_lines
            # Print the node and its normalized rank
            print(f"{current_node}\t{r}")
        # Update the current node and contributions for the new node
        current_node = node
        contributions = []
        contributions.append(value)

# After processing all lines, print the last node and its normalized rank       
if current_node:
    new_rank = 0.85 * sum(contributions) + 0.15
    r = new_rank/num_lines
    print(f"{current_node}\t{r}")

    
    
