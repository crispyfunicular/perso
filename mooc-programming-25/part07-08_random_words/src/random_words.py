# Write your solution here
from random import sample

def words(n: int, beginning: str) -> list:
    all_results = []

    with open("words.txt") as new_file:
        for line in new_file:
            entry = line.strip()
            if entry.startswith(beginning):
                all_results.append(entry) 

    #print(all_results)
    return sample(all_results, n)


def main():
    word_list = words(3, "aber")
    for word in word_list:
        print(word)
    

if __name__ == "__main__":
    main()
