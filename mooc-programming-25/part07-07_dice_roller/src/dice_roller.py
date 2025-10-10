# Write your solution here
from random import choice

def roll(die: str):
    if die == "A":
        faces = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        faces = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        faces = [1, 4, 4, 4, 4, 4]
    
    return choice(faces)


def play(die1: str, die2: str, times: int):
    die1_score = 0
    die2_score = 0
    ties = 0
    for i in range(times):
        die1_roll = roll(die1)
        die2_roll = roll(die2)
        if die1_roll > die2_roll:
            die1_score += 1
        elif die1_roll < die2_roll:
            die2_score += 1
        elif die1_roll == die2_roll:
            ties += 1
    
    return (die1_score, die2_score, ties)


def main():
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)


if __name__ == "__main__":
    main()
