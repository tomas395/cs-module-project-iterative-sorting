# TO-DO: Complete the selection_sort() function below
# Runtime O(n^2)
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):  # makes it so that we iterate over each item one at a time
        cur_index = i
        lowest_index = cur_index
        # we need it to evaluate each index and compare it with to the lowest value.

        # iterate over each item in the list to find the lowest value
        for j in range(cur_index, len(arr)):

            # once the lowest is found, move to the left and swap the larger value in it's old place
            if arr[j] < arr[lowest_index]:
                lowest_index = j

        # repeat swaps until there is nothing left to swap, then return the list
        arr[lowest_index], arr[cur_index] = arr[cur_index], arr[lowest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
# Runtime O(n^2)
def bubble_sort(arr):
    # Your code here
    swapped = True  # set a boolean check for if there have been any swaps
    while swapped:
        swapped = False
        # makes it so that we iterate over each item one at a time
        for i in range(len(arr) - 1):
            print(arr)  # without this it fails the test for whatever reason
            # check the neigboring index and only if it's smaller you...
            if arr[i] > arr[i + 1]:
                #  swap indexes so the lesser value is on the left and greater is on the right and keep checking if a swap was made
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True  # once the final pass has been made and there have been no swaps, switch the bool to end the loop and return sorted
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
