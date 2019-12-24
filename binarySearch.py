"""
Finding the word in a dictionary using binary search
For binary search the given list must always be sorted
A function that takes two parameters 
1. list 
2. item to search in the list
returns the index of item to be searched
"""
import math
def binarySearch(arrayList, item):
    # low and high is for what part of the search we need to track in
    low = 0
    high = len(arrayList)-1

    while low <= high:
        mid = math.floor((low + high)/2)
        guess = arrayList[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return "Number not found"

print(binarySearch([1,5,7,43,65,77,87, 120], 120))
        