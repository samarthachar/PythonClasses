lst = [10,10,10,10,10]


# Brute Force
def getSecondLargest(lst):
    lst.sort()
    n = len(lst)
    for i in range(n-2,-1,-1):
        if lst[i] != lst[-1]:
            return lst[i]
    return -1

print(getSecondLargest(lst))

