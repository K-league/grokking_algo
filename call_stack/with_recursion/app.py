def fact(x): #first call to fact; x is 3
    if x == 1: #second call to fact is 2
        return 1
    else:
        return x * fact(x-1) # fact is recursive call
if __name__ == "__main__":
    print(fact(3))