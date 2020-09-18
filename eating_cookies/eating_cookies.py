'''
Input: an integer
Returns: an integer
'''

# what is the runtime of this implementation
# O(3^n)
def eating_cookies(n):
    # What are our base cases?
    # This represents a number of cookies where we can just take that many cookies
    
    if n < 0:
        return 0
    if n == 0:
        return 1

    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n -3)

# print(eating_cookies(5))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

    ###########################
    # From after hours video
    #use recursion
    # base case is n <= 2
    #These need to be hardcoded as our base cases
    # n = 0 = > 0
    # n = 1 = > 1
    # n = 2 = > 2
    #every other situation it can be broken down recursively
    ###########################