"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1
    
    # Your code goes here
    print(items)
    return frequencies


