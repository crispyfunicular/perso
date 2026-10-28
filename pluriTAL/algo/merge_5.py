"""
Mathieu Dehouck
Algorithmique et Programmation
2025-2026

Merge Sort
"""
from random import randint, seed, choice



# how to sort a list recursively

def merge_sort(lst):

    # simple cases
    if lst == []:
        return lst

    if len(lst) == 1:
        return lst


    # more complex case
    # let's cut lst in 2
    l1 = lst[:len(lst)//2]
    l2 = lst[len(lst)//2:]

    l1_sorted = merge_sort(l1) # simpler case
    l2_sorted = merge_sort(l2) # simpler case

    # now we have two sorted half lists...
    # we need to merge them

    l12 = merge(l1_sorted, l2_sorted)

    return l12



def merge(l1, l2):
    # simple cases
    if l1 == []:
        return l2

    if l2 == []:
        return l1

    # more complex case
    if l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [    l2[0]]                   + merge(l2[1:], l1)

    

print(merge_sort([randint(0, 100) for _ in range(50)]))
print()

# or the imperative merge we saw in class


def merge(l1, l2):
    i = 0
    j = 0
    lst = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lst.append(l1[i])
            i += 1
        else:
            lst.append(l2[j])
            j += 1

    if i == len(l1):
        lst += l2[j:]
    else:
        lst += l1[i:]

    return lst

print(merge_sort([randint(0, 100) for _ in range(50)]))
print()



# your turn

# It is possible to split a list in two without knowing its length
# tip : do it recursively


def merge_sort_2(lst):

    # simple cases
    if lst == []:
        return lst

    if len(lst) == 1:
        return lst


    # more complex case
    # let's cur lst in 2
    l1, l2 = your_split(lst)

    l1_sorted = merge_sort(l1) # simpler case
    l2_sorted = merge_sort(l2) # simpler case

    # now we have two sorted half lists...
    # we need to fuse them

    l12 = merge(l1_sorted, l2_sorted)

    return l12


# write a function that can split a list into to half sized ones recursively
def your_split(lst):
    NotImplemented


try:
    print(merge_sort_2([randint(0, 100) for _ in range(30)]))
except:
    print('merge_sort_2 did not run properly. remove this try to get the actual bug message.')



print()

