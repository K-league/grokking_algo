def count(arr): #first call to count(); arr is [1,2,3,4,5,6]
    # first call in the stack array length is 6, so it will fall on else
    if len(arr) == 1: #second call to count(); is array's lenght equal to 1? if not move on to else
        return 1
    else: # arr[1:] cuts the array from index 1 forwards
        return 1 + count(arr[1:]) # count() recursive call; count array 1 to length


print(count([1,2,3,4,5,6]))