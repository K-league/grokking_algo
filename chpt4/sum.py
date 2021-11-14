def sum(arr):
    #base case
    if len(arr) == 1:
        return arr[0]
    else:
        n = arr[0]
        return n + sum(arr[1:])


print(sum([2,4,6]))