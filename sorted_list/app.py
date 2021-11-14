def findSmallest (arr):
    smallest = arr[0] # stores smallest value
    smallest_index = 0 # store the index of the smallest value
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
    return smallest_index

    # use this function to write the selection sort
def slectionSort(arr): # sorts the an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # finds the smallest element in the array, and add to the new array
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == "__main__":
    print(slectionSort([5, 3, 6, 2, 10]))