def smallestValue(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    while len(arr) != 0: 
        smallest = smallestValue(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selection_sort([54,41,23,98,21,12]))
