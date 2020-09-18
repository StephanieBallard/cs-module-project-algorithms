# The Knapsack Problem

# Understanding and planning in comments

Suppose you are Indiana Jones, and you have found the secret entrance to the Temple of Doom. Before you is a multitude of artifacts and treasures - pots, gemstones, works of art, and more. These belong in a museum! But there are soldiers hot on your heels, and you can only carry so much...

# *GOAL* - Need to pick what is most important and maximize the size to space ration with the value of the items.

You, brave explorer, are facing the knapsack problem - maximizing the value of a set of items you select that are constrained by total size/weight. The size and the value of an item need not be correlated - the most precious item may be a tiny gemstone. But it turns out it's pretty tricky to get a truly optimal solution, and that a bruteforce approach really doesn't scale.

# We need to sort the items into the bag and need to be within a certain total size/weight
# The size and value of the items do not need to have a correlation.
# The first solution typically wont work well if the size of the bag is increased exponentially.

A bit more motivation - this is a very general optimization problem that can be applied in a multitude of situations, from resource selection and allocation to stuffing stolen goods in knapsacks.

![xkcd "NP-Complete"](https://imgs.xkcd.com/comics/np_complete.png "General solutions get you a 50% tip.")

The specific goal of this exercise is to write a program that takes input files that look like this:

# The func will take in three parameters
   # Item Number of type Int
   # The space the item takes up in the back pack of type Int
   # The profit for saving that item of type Int
      # Three pieces of data need to be passed into our func and the amount of space left needs to be adjusted and the item number needs to change each time
      # an item is added into the bag.
      # The item needs to also be matched up with a profit value of the item added to the bag. Does that total need to be calculated as well?
         # Use an empty array to keep track of the item number. Add one to the position in the array which will start it at one. The needs to change the entire array making that a O(n) (i think.) 
            # Does this need to be an array of arrays? Over thinking it?
            
         # We need to keep track of the total space in the bag and how much each item is using and how much will be left after it is entered in the bag.
            # If the amount of the item is greater than the amount of space left in the bag then it cannot fit into the bag

            # What happens if there are no more items left to place in the bag?

          
          
          
# From the provided information in the other file     

def knapsack(size, value):
   item_number = arr index + 1
      after each item is in the bag do this to the item number
            
Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here

    pass

# We need to make an array of tuples. 
# using two functions we will handle our four pieces of data that we need to keep track of.


 ```
1 42 81
2 42 42
3 68 56
4 68 25
5 77 14
6 57 63
7 17 75
8 19 41
9 94 19
10 34 12
```

The first row number is just a row/observation number, to facilitate reading and referring to items. The second number is the size/cost of the item, i.e. the cost of putting it in your knapsack. The third number is the value, i.e. the utility/payoff you get for selecting that item. The program should also take as input a total size, which can just be a number passed from the command line. So execution may look like this: `python knapsack.py input.txt 100`.

The goal is to select a subset of the items to maximize the payoff such that the cost is below some threshold. That is, the output should be a set of items (identified by number) that solves the Knapsack problem. It's also worth outputting the total cost and value of these items. This can all just be printed and may look something like below.

This is *not* a solution, just an example:

```
Items to select: 2, 8, 10
Total cost: 98
Total value: 117
```

## Testing
For this problem, there are tests that test your implementation with small (10 items to consider), medium (200 items to consider), and large inputs (1000 items to consider).

You can run all of the tests with `python test_knapsack.py`, or run the tests individually with `python test_knapsack.py -k small`, `python test_knapsack.py -k medium`, or `python test_knapsack.py -k large`.

## Hints
1. Base cases you might want to consider for a naive recursive implementation of this problem are:
   * What if there are no items left to consider?
   * What if the item I'm considering is too large to fit in my bag's remaining capacity?
2. In order to move towards one of our base cases, we'll pick up an item from the pile to consider, and add it to a copy of our bag. Now we have two versions of our bag, one with the item we're considering, and one without. All we have to do now is pick the bag that yields us a higher value. 
3. As far as caching for this problem is concerned, a simple hash table or array is not going to suffice, because each solution now depends upon two parameters: the number of items in our pile to consider, as well as the capacity of our bag. So we'll need a 2x2 matrix in order to cache our answers adequately. 
4. Here's another way we might consider tackling this problem: what if we iterated through every single element in our pile and assign each one a value given by its value/weight ratio. Then we can sort all of the items based on this assigned value such that those items with a higher value/weight ratio are at the top of our sorted list of items. From there, we can just grab off the items at the top of our list until our bag is full. What would be the runtime complexity of this scheme? Would it work in every single scenario for any pile of items?
