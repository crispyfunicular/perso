"""
Mathieu Dehouck
Algorithmique et Programmation
2024-2025

Sorting algorithm
"""

from random import randint, seed

# feel free to add print everywhere to understand what's going on


seed(
    0
)  # is used to initialized the pseudo random number generator, change it to have a different run

# 0. let's create a random list

l = []
for _ in range(25):  # _ can be used to name a variable in a loop that we won't use
    l.append(randint(0, 100))  # a number at random between 0 and 100

print("A random list", l)


# 1. let make our first sorting algorithm
# corresponding property : in a sorted list the first element is always the smallest
# we will count the number of comparisons


def smallest_1(l, verbose=False):  # get the smallest element of a list
    count = 0

    m = l[0]  # take the first element of the list
    for i in range(
        len(l) - 1
    ):  # we iterate over the list but do not need to check the first element
        count += 1
        if l[i + 1] < m:  # if the ith element is actually smaller than m, remember it
            m = l[i + 1]

    if verbose:
        print(
            "smallest element :", m, "of", l, "number of comparisons :", count, sep="\t"
        )

    return m, count


print()
print("1.1. smallest element of a list")
m, ncomp = smallest_1(
    l.copy()
)  # copy l so that we keep our original list for other sorting theynanigans (it's inclusive)
print(m, ncomp)


# now that we can get the smallest element of a list, we can sort it by repeating the process


def sort_1(l, verbose=False):
    count = 0
    nl = []  # a new empty list to store the sorted results

    while l != []:
        m, ncomp = smallest_1(l, verbose)
        count += ncomp

        l.remove(m)  # remove the smallest element from l
        nl.append(m)  # put it in nl

        if verbose:
            print("Current list states:", nl, l, count, sep="\t")
    return nl, count


print()
print("1.2. sorting a list")
sorted_l, ncomp = sort_1(
    l.copy(), verbose=True
)  # copy l so that we keep our original list for other sorting shenanigans
print("Sorted", sorted_l, "in", ncomp, "comparisons", sep="\t")


# 2. your turn
# another property of a sorted list is that the last element is also the biggest


def biggest(l):
    # write a function that find the biggest element of a list
    count = 0
    max = l[0]

    for nb in l[1:]:
        count += 1
        if nb > max:
            max = nb

    return max, count

    # b = max(l) # this is cheating
    # b = 0
    # return b, count


# let's test it
print()
print("2.1")

for _ in range(10):
    random_list = [
        randint(0, 1000) for _ in range(randint(10, 30))
    ]  # a random list of random length
    b, ncomp = biggest(random_list)
    print(max(random_list), b, max(random_list) == b, sep="\t")


# now sort
def sort_2(l):
    count = 0
    nl = []  # a new empty list to store the sorted results

    while l:
        max, ncount = biggest(l)
        nl.insert(0, max)
        l.remove(max)
        count += ncount
    # nl = [x for x in sorted(l)]

    return nl, count


print()
print("2.2.")
for _ in range(10):
    random_list = [
        randint(0, 1000) for _ in range(randint(10, 30))
    ]  # a random list of random length
    sorted_l, ncomp = sort_2(random_list.copy())
    print(sorted_l, sorted_l == sorted(random_list), sep="\t")


# 3. go there : https://en.wikipedia.org/wiki/Bubble_sort
# implement a simple bubble sort
# what property lies behind the algorithm?
# you can use the testing code of 2.2 to make sure your algorithm works


def bubble_sort(lst: list):
    count = 0

    while True:
        perm = 0
        i = 0
        while i < len(lst) - 1:
            nb = lst[i]
            nb1 = lst[i + 1]

            if nb > nb1:
                lst[i] = nb1
                lst[i + 1] = nb
                perm += 1

            i += 1
            count += 1

        if perm == 0:
            break

    return lst, count


print()
print("3.")
for _ in range(10):
    random_list = [
        randint(0, 1000) for _ in range(randint(10, 30))
    ]  # a random list of random length
    sorted_l, ncomp = bubble_sort(random_list.copy())
    print(sorted_l, sorted_l == sorted(random_list), sep="\t")
