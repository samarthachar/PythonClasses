lst = [1,2,3]


# Brute Force - Time Complexity: O(n^3), Space Complexity: O(n^3)
"""
def get_sub_array(lst):
    n = len(lst)
    new_list = []
    for i in range(0,n):
        for x in range(i,n):
            new_list_2 = []
            for y in range(i,x+1):
                new_list_2.append(lst[y])
            new_list.append(new_list_2)
            
    return new_list
print(get_sub_array(lst))
"""


# Improved Approach - Time Complexity: O(n^3), Space Complexity: O(n)
'''
def get_sub_array(lst, counter_1, counter_2):
    if counter_2 == len(lst):
        return
    elif counter_1 > counter_2:
        return get_sub_array(lst, 0, counter_2=+1)
    else:
        print(lst[counter_1:counter_2 + 1])
        return get_sub_array(lst, counter_1 + 1, counter_2)

print(get_sub_array(lst,0,0))
'''

# Optised Approach - Time Complexity: O(n^2), Space Complexity: O(1)
def get_subarrays(lst):
    result = []
    for start in range(len(lst)):
        for end in range(start, len(lst)):
            result.append(lst[start:end+1])
    print(result)

get_subarrays(lst)
