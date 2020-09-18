You are climbing a staircase. It takes n steps to reach the top.

Each time, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Decide if we should use recursion to solve the problem by looking for clues in the problem description.
    What clues in the description are there that might lead us to use recursion in our solution? The important wording that jumps out immediately is:
    In how many ways can you climb to the top?
    Any time we are looking at combinations or permutations (ways of combining or ordering things), it’s an excellent opportunity to use recursion.

Find similar problems that we’ve already solved and analyze those problems to see if they help us solve this problem.

Draw a diagram for a small input and study the diagram to help understand any potential solutions.

If we use recursion, discover the base case or base cases.
    Examine the diagram we drew. What would be the base case? 
    The base case would be if the current step we are on is higher than the desired final step (n) or 
    is equal to the desired final step (n). What do we need to return when we hit one of the base cases? 
    Well, remember we are counting paths to get to n. So, if the current step equals n, 
    then we should return 1 to represent one valid path to the desired step. 
    If the current step is higher than n, we went too far, and we should not count that path by returning 0.

        So our base cases are:
            If the current step is equal to n, return 1.
            If the current step is greater than n, return 0.

If we use recursion, discover the recursive case.
    If we aren’t at a base case, what is the recursive case? 
    Again, looking at the diagram, we have two options: take two steps or take one step. 
    We represent this by a recursive call to our function, but with the current step incremented by one or two.

Write out our algorithm as pseudocode.
    input to function is current_step and desired_step (both integers):
    if current_step is greater than desired_step:
        return 0
    if current_step is equal to desired_step:
        return 1
    
    input to function is current_step and desired_step (both integers):
    if current_step is greater than desired_step:
        return 0
    if current_step is equal to desired_step:
        return 1
    return climb_stairs(current_step+1, desired_step) + climb_stairs(current_step+2, desired_step)

Change each line of pseudocode into actual code.
    One of the beautiful things about Python is that Python code reads almost like pseudocode. 
    In our case, we have very little to do to convert from pseudocode into actual Python code.
        def climb_stairs(current, desired):
    if current > desired:
        return 0
    if current == desired:
        return 1
    return climb_stairs(current+1, desired) + climb_stairs(current+2, desired)
Test out our code and see if it is returning the outputs that we would expect.