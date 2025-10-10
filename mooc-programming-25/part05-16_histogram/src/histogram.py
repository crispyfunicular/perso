# Write your solution here

def histogram(word: str) -> dict:
    histogram = {}

    for i in range(len(word)):
        if word[i] not in histogram:
            histogram[word[i]] = 0
        histogram[word[i]] += 1

    for letter in histogram:
        print(letter, histogram[letter] * "*")


def main():
    histogram("abba")
    histogram("statistically")


if __name__ == "__main__":
    main()
