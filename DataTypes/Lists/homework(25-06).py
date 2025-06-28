lst = [1,2,3,0,5,4,0]
output = [1,2,3,4,5,0,0]


# lst.sort()

# def getZero():
#     index = 0
#     if lst[index] == 0:
#         del lst[index]
#         lst.append(0)
#         index+= 1
#         getZero()

# getZero()
# print(lst)
index = 0
lst.sort()
for i in lst:
    if i == 0:
        del lst[index]
        lst.append(0)
    index += 1
