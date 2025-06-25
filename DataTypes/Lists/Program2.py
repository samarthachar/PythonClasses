lst = [2,3,6,34,7,35,3,4,5]


# Brute Force
def getSecondLargest_BruteForce(lst):
    lst.sort()
    for i in range((len(lst))-2,-1,-1):
        if lst[i] != lst[-1]:
            return lst[i]
    return -1

print(getSecondLargest_BruteForce(lst))

def getSecondLargest_TwoPass(lst):
    n = len(lst)
    largest = -1
    secondLargest = -1
    for i in range(n):
        if lst[i] > largest:
            largest = lst[i]
    for i in range(n):
        if lst[i] > secondLargest and lst[i] < largest:
            secondLargest = lst[i]
    return secondLargest
print(getSecondLargest_TwoPass(lst))

def getSecondLargest_OnePass(lst):
    n = len(lst)
    largest = -1
    secondLargest = -1
    for i in range(n):
        if lst[i] > largest:
            secondLargest = largest
            largest = lst[i]
        elif lst[i] > secondLargest and lst[i] < largest:
            secondLargest = lst[i]
    return secondLargest
print(getSecondLargest_OnePass(lst))