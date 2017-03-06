import random
import bisect

lst = list()
for item in range(20):
    bisect.insort(lst, random.randrange(1, 1000))

target = lst[5]

"""
    Bucket size = 1000
    target = random
    
"""

def binary_search(lst, target):
    lst.sort()

    min = 0
    max = len(lst) - 1


    for index in range(0, max):
        mid = ((max + min) // 2)

        if target == lst[mid]:
            return mid

        elif target < lst[mid]:
            max = mid - 1 

        else:
            min = mid + 1


    return -1 


print binary_search(lst, target)

        





