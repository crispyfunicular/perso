# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    count1 = 0

    while count1 < amount:
        count2 = 0
        lst = []
        while count2 < length:
            lst.append(random.choice(characters))
            count2 += 1
        yield "".join(lst)
        count1 += 1



def main():
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)


if __name__ == "__main__":
    main()
