"""
Mathieu Dehouck
Algorithmique et Programmation
2024-2025

recherche par dichotomie
"""

from random import randint, seed, choice

# feel free to add print everywhere to understand what's going on
# also feel free to change the code that's how we learn

K = 1000000

seed(
    0
)  # is used to initialized the pseudo random number generator, change it to have a different run

# 0. let's create a random list

l = [randint(0, K) for _ in range(1000)]

print("10 first elements of a random list", l[:10], sep="\t")


# 1. let's search for element in the unsorted list


def search(el, lst):
    comp = 0  # we count the number of comparison as usual

    for i in range(len(lst)):  # we count from 0 to len(lst) - 1
        current_el = lst[i]  # these two lines are the same as for current_el in lst:

        comp += 1
        if current_el == el:
            return True, comp

    return False, comp


print()
print("1. Basic Search")
for _ in range(10):
    r = randint(
        0, K
    )  # about 1/1000 chance that we pick an element in the list by random
    inside, comp = search(r, l)
    print(r, r in l, inside, comp, sep="\t")


def choux(lst):
    return lst[randint(0, len(lst) - 1)]


for _ in range(10):
    r = choux(l)  # we pick an element from l at random on purpose
    inside, comp = search(r, l)
    print(r, r in l, inside, comp, sep="\t")


# 2. now the clever search based on sorted list

print()
print("2. Dichotomy Search")


# note that I do not put elif, but just if often, this is because if the if condition is true we leave the function with return, so we reach the next if only if the first is false
def dichotomy(el, lst):
    # we need to keep track of the boundary of our search space
    low = 0
    high = len(lst) - 1

    comp = 0

    comp += 1
    if el < lst[low]:  # el smaller than the smallest
        return False, comp
    comp += 1
    if el == lst[low]:  # equal
        return True, comp

    comp += 1
    if el > lst[high]:  # bigger than the biggest
        return False, comp
    comp += 1
    if el == lst[high]:  # equal
        return True, comp

    # here we know lst[0] <= el <= lst[-1]
    # so we cut lst in the middle

    while (
        low < high - 1
    ):  # if low == high - 1, then we have reached two consecutive number and have rejected everything outside, so we are close to the end
        mid = (
            low + high
        ) // 2  # remember this means euclidean division, it's because if (low + high) is odd (5 for example), the middle is not a whole number : 2.5

        comp += 1
        if el == lst[mid]:
            return True, comp

        comp += 1
        if el < lst[mid]:  # el is smaller than the middle value
            # so we can ignore the bigger half and we reduce the search space to the lower half : mid is the new high
            high = mid

        else:  # here i keep the else, because it want to be here only if the above condition was false
            # we ignore the lower half
            low = mid

    return False, comp


l.sort()  # we sort l, so that dichotomy can kick in

for _ in range(10):
    r = randint(
        0, K
    )  # about 1/1000 chance that we pick an element in the list by random
    inside, comp = dichotomy(r, l)
    print(r, r in l, inside, comp, sep="\t")


for _ in range(10):
    r = choice(l)  # we pick an element from l at random on purpose
    inside, comp = dichotomy(r, l)
    print(r, r in l, inside, comp, sep="\t")


# 3. now we want to return the position of the number if it is in the list and False otherwise
# take inspiration from the code of dichotomy function and modify it to achieve this goal

print()
print("3. Position of el in the list")


def position(el, lst):
    comp = 0

    low = 0
    high = len(lst) - 1

    # Boundaries
    comp += 1
    if el < lst[low]:
        return -1, comp
    comp += 1
    if el == lst[low]:
        return low, comp

    comp += 1
    if el > lst[high]:
        return -1, comp
    comp += 1
    if el == lst[high]:
        return high, comp

    while low < high - 1:
        mid = (low + high) // 2
        comp += 1
        if el < lst[mid]:
            high = mid
            continue
        comp += 1
        if el > lst[mid]:
            low = mid
            continue
        comp += 1
        if el == lst[mid]:
            return mid, comp

    return -1, comp


for _ in range(10):
    r = randint(
        0, K
    )  # about 1/1000 chance that we pick an element in the list by random
    pos, comp = position(r, l)
    truth = l.index(r) if r in l else False
    print(r, truth, pos, truth == pos, comp, sep="\t")


for _ in range(10):
    r = choice(l)  # we pick an element from l at random on purpose
    pos, comp = position(r, l)
    truth = l.index(r) if r in l else False
    print(r, truth, pos, truth == pos, comp, sep="\t")
