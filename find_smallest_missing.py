# can binary search help us in this case?
# binary search requires us to know our target
# improved the runtime from O(n) to O(log n)
def find_smallest_missing(arr):
    if arr[0] != 0:
        return 0

    # add another check here to see if arr[-1] == len(arr) - 1
    if arr[-1] == len(arr) - 1:
        # no elements are missing 
        return len(arr)

    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            # toss out the left side
            # don't include the midpoint since we know 
            # it matches its index 
            start = mid + 1

        else:
            # toss out the right 
            # but do keep the midpoint, since we can't 
            # rule out that it might be the smallest missing
            end = mid 
    
    # we've narrowed it down to one element 
    # at this point start == end, so return either 
    return start
    
    # O(n) traversal through the entire array 
    # realizing that we're not taking advantage of the fact that 
    # the input is sorted, we can ask ourselves how to leverage 
    # that fact 
#    for i in range(len(arr) - 1):
#        if arr[i+1] != arr[i] + 1:
#            return arr[i] + 1
#
#    return arr[-1] + 1

A1 = [0,1,2,6,9,11,15]
A2 = [1,2,3,4,6,9,11,15]
A3 = [0,1,2,3,4,5,6]
A4 = [3,6,9,15,18]
A5 = [0,1,3,6,9,11,15]
A6 = [0,1,2,3,4,5,7,8]

print(find_smallest_missing(A1))
print(find_smallest_missing(A2))
print(find_smallest_missing(A3))
print(find_smallest_missing(A4))
print(find_smallest_missing(A5))
print(find_smallest_missing(A6))