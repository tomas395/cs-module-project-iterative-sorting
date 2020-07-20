# Runtime O(n)
def linear_search(arr, target):
    for i in range(len(arr)):  # loop through all the items in the list
        if arr[i] == target:  # if the target is found early, return it
            return i
    return -1  # or you can wait until the for loop finishes before returning a value or not found
    # we return -1 as not found instead of False to avoid type errors
    # if we're going to use a Binary search, we need to make sure the data is sorted first otherwise it won't work


# Write an iterative implementation of Binary Search
# Runtime: O(log(n))
def binary_search(arr, target):
    left = 0  # low is the pointer to the first index in the list
    right = len(arr) - 1  # high is the pointer to the last index in the list
    while left <= right:
        # find the midpoint and continue
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # check to see if the element should be on the left or right side
        # of our midpoint
        elif arr[mid] < target:
            # toss out the left side of the arr
            # update our `left` index
            left = mid + 1
        # otherwise, arr[mid] > target
        else:
            # toss out the right side of the arr because the element has to be on the left side
            right = mid - 1
    return -1  # not found
