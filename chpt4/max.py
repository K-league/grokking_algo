# Find max number in a list
# base case [] 0 elements = max is null
#           [7,8] 2 elements = max is 8 when compared to 7
# get a list 
# if list is empty return null
# Otherwise the max number of the list is the first number compared to the second number in the list, if second is greater max becomes the second number and so on


# compare first number with everything else 
# compare two elements
# if there is more: 
    # compare two
# else:
# found it

def my_max(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        candidate = arr[0]
        rest = my_max(arr[1:])
        if candidate > my_max(arr[1:]):
            return candidate
        else:
            return rest

def popper(arr, prev_max=None):
    if not arr:
        return prev_max
    if prev_max is None:
        prev_max = arr.pop(0)
    else:
        if prev_max < arr[0]:
            prev_max = arr.pop(0)
        else:
            arr.pop(0)
    return popper(arr, prev_max)
    
print(my_max([1,21,3, 22, 8]))
print(popper([1,21,3, 22, 8]))

    # #base case, no elements in array
    # if len(arr) == 0:
    #     return null
    # if num1 <= num2:
    #     #
    # else: 