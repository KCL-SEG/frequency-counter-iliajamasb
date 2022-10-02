"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        if item not in items:
            items.item = 1
        else:
            items.item += 1
    
    # Your code goes here
    print(items)
    return frequencies


