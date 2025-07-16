inp = input("Enter word: ").lower()

lst = []
for i in inp:
    if i != " ":
                lst.append(i)
string_no_space = ''.join(lst)
reversed_string = ''.join(reversed(lst))
if  reversed_string == string_no_space:
    print("Yes, it's a palidrome")
else:
    print("No, not a palidrome")
    