def binary_search(list, item) :
    low = 0
    high = len(list)-1
    #low and high keep track of which part of the list you'll search in
    while low <= high:
        #while there is more than one element
        mid = int((low + high) / 2)
        #check middle element
        guess = list[mid]
        if guess == item:
            #item found
            return mid
        if guess > item:
            #guess too high
            high = mid -1
        else:
            #guess too low
            low = mid + 1
    return None
    #item does not exist

my_list = [1, 3, 5, 7, 9]

if __name__ == "__main__": # this runs only if the file isn't imported i.e. python3 index.py
    print(binary_search(my_list, 5))
    print(binary_search(my_list, 7))
    print(binary_search(my_list, 20))