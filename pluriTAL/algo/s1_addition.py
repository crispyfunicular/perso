"""
Mathieu Dehouck
Algorithmique et Programmation
2024-2025

Multiplication by Addition
Base 2
"""

from argparse import ArgumentParser
from math import log2, log10


ap = ArgumentParser()
ap.add_argument("x", type=int, help="First argument to multiply")
ap.add_argument("y", type=int, help="Second argument to multiply")

args = ap.parse_args()
x = args.x
y = args.y

# 0. first we compute x*y the obvious way, to have a sanity check
prod = x * y

print("Arg", "Val_10", "Long_10", "log_10", "Val_2", "Long_2", "log_2", sep="\t")
print(
    "x :",
    x,
    len(str(x)),
    str(log10(x))[:6],
    bin(x)[2:],
    len(bin(x)) - 2,
    str(log2(x))[:6],
    sep="\t",
)
print(
    "y :",
    y,
    len(str(y)),
    str(log10(y))[:6],
    bin(y)[2:],
    len(bin(y)) - 2,
    str(log2(y))[:6],
    sep="\t",
)

print("x*y =", prod)

print()
print("Algo", "Res", "#Operations", sep="\t")


# 1. we compute x*y by iterated additions
count = 0  # we're gonna count the number of additions and comparisons

prod = 0
for _ in range(x):
    prod += y
    count += 1


print("1.", prod, count, sep="\t")


# 1.1. we compute x*y by iterated additions, on the smallest number
count = 0

if x < y:
    x, y = x, y
else:
    x, y = y, x
count += 1

prod = 0
for _ in range(x):
    prod += y
    count += 1


print("1.1.", prod, count, sep="\t")


# I make sure we have the original ordering of the variables
x = args.x
y = args.y

# 2. now with the binary representation
count = 0

bx = bin(x)[
    2:
]  # get the binary representation of x. the two first characters are a way to indicate that it's a number in binary.
# note that it's read in the usual BIG-ENDIAN direction, the first bit is the biggest one.
count += len(bx)  # we will learn how to do this efficiently once

prod = 0
exp = y
for i in reversed(bx):  # we reverse because of endianness
    if i == "1":
        prod += exp  # only add exp if the relevant bit is set to one
        count += 1

    exp += exp  # multiply exp by 2
    count += 1


print("2.", prod, count, sep="\t")
print()


# 3. Exercice on bases

# let's work with strings of characters to represent numbers :
# if s = '101'   and i do  s = s + '0'    i have  '1010'  it's simple concatenation

# let's first do base 2 representation by computing the "values of the columns" of the representations


"""def binary_1(x): # here you work
    columns = [1] # i'm nice, i prepare the columns for you
    while 2 * columns[-1] <= x: # as long as the 2 * last element in columns is smaller than x, we know we need it
        columns.append(2 * columns[-1])

    #print(columns)   # uncomment if you want to see the columns

    result = ''
    for col in reversed(columns): # we want to read the columns from biggest to smallest
        # now your turn
        # remember, you have to test if col fits in x and act accordingly


    return result"""

# now we test you function
print("3.1. Exercices")
for i in [0, 1, 2, 3, 4, 8, 16, 1347, 8521, 163245]:
    print(
        i, bin(i)[2:], binary_1(i), bin(i)[2:] == binary_1(i), sep="\t"
    )  # If your function works you should have True at the end of each line


def binary_2(
    x,
):  # now we do the same but in the other direction, without computing the columns
    safeguard = 10000  # let's avoid infinite loops for now

    if x == 0:
        return "0"

    result = ""
    while x != 0:
        safeguard -= 1  # this is just to make sure you wont break you computer
        if safeguard == 0:
            break

        # now your turn
        # think of the final representation and how you would go to test if it matches x

    result = result[::-1]  # let's flip the string
    return result


# now we test you function
print()
print("3.2. Exercices")
for i in [0, 1, 2, 3, 4, 8, 16, 1347, 8521, 163245]:
    print(
        i, bin(i)[2:], binary_2(i), bin(i)[2:] == binary_2(i), sep="\t"
    )  # If your function works you should have True at the end of each line


# extra challenge :
def base_5(x):
    result = ""

    # make a function that returns the representation of x in base 5, it's almost like base 2, you can do columns first, or not, up to you

    return result


# now we test you function
print()
print("4. Exercices")
print(
    0, "0", base_5(0), "0" == base_5(0), sep="\t"
)  # If your function works you should have True at the end of each line
print(1, "1", base_5(1), "1" == base_5(1), sep="\t")
print(2, "2", base_5(2), "2" == base_5(2), sep="\t")
print(5, "10", base_5(5), "10" == base_5(5), sep="\t")
print(10, "20", base_5(10), "20" == base_5(10), sep="\t")
print(25, "100", base_5(25), "100" == base_5(25), sep="\t")
print(53, "203", base_5(53), "203" == base_5(53), sep="\t")
