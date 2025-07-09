# Strech - Write a program to convert from decimal to binary, and binary to decimal

def binary(inp):
    lst = []
    x = True
    while x:
        inp = inp % 2
        lst.append(inp)
        lst = reversed(lst)
        print(lst)
        if inp == 1 or inp == 0:
                x = 1
    word = ''.join(lst)
    return word
print(binary(2))
