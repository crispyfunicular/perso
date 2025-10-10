# Write your solution here
def factorials(n: int):
    factorials = {}
    value = 1
    for i in range(1, n+1):
        value *= i
        factorials[i] = value
    return factorials


def main():
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])


if __name__ == "__main__":
    main()
