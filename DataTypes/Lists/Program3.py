lst = [1,2,3,4,5,6]

inp = int(input("Number of time rotation:"))
# for i in range(inp):
#     x = lst[-1]
#     lst = [x] + lst
#     del lst[-1]
# print(lst)


# lst = [1,2,3,4,5,6]

# inp = int(input("Number of time rotation:"))
# def rotate_1(lst, inp):
#     if inp == 0:
#         return
#     temp = lst[-1]
#     for i in range(len(lst)-1,0,-1):
#         lst[i] = lst[i-1]
#     lst[0] = temp
#     rotate_1(lst, inp-1)
# rotate_1(lst, inp)

# print(lst)



#Reversal Technique - 
# Reverse the last k elements.
# Reverse the first n - k elements.
# Reverse the entire array.


lst = [1,2,3,4,5,6]

inp = int(input("Number of time rotation:"))
def rotate_2(lst,inp):
    if inp == 0:
        return
    n = len(lst)
    inp = inp % n
    lst[n-inp:] = reversed(lst[n-inp:])# You will get [1,2,3,4,6,5]  
    lst[:n-inp] = reversed(lst[:n-inp])# You will get [4,3,2,1,6,5]
    lst[:] = reversed(lst)# You will get [5,6,1,2,3,4,]

rotate_2(lst,inp)
print(lst)