# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    f = Fraction(1, amount)
    lst = []
    i = amount
    while i > 0:
        lst.append(f)
        i -= 1
    return lst


def main():
    amount = 3
    print(fractionate(amount))
    

if __name__ == "__main__":
    main()
