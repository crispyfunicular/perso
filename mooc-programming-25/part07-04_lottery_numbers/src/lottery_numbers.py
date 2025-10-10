# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    lst = []
    nb = list(range(lower, upper))
    nb_sample = sample(nb, amount)
    #print(nb_sample)

    while nb_sample != []:
        minimun = min(nb_sample)
        lst.append(minimun)
        nb_sample.remove(minimun)

    return lst


def main():
    print(lottery_numbers(3, 2, 9))
    

if __name__ == "__main__":
    main()
