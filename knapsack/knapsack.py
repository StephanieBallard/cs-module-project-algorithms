#!/usr/bin/python

# item one in bag weighs 10 pounds and value 15 1.5
# item two in bag weights 18 pounds and value 25 1.38


# 4. Here's another way we might consider tackling this problem: what if we iterated through every single element in our pile and 
# assign each one a value given by its value/weight ratio. Then we can sort all of the items based on this assigned 
# value such that those items with a higher value/weight ratio are at the top of our sorted list of items. 
# From there, we can just grab off the items at the top of our list until our bag is full. 
# What would be the runtime complexity of this scheme? Would it work in every single scenario for any pile of items?

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    # backpack_size = capacity
    data = {}

    
    for item in items:
      # value / size 
      item_number = item[0]
      ratio = item[2] / item[1]
      # key would be the item number : ratio
      # need to add 1 to the item number after each iteration
      data[ratio] = item_number
      
    print(data)

# need to sort the items and push the ones w/ the 
# highest value to the top so they get a priorty spot in the bag


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')