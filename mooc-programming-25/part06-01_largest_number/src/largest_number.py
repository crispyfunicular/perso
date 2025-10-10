# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        largest_number = 0
        for line in new_file:
            line = line.replace("\n", "")
            if int(line) > largest_number:
                largest_number = int(line)
        return largest_number

def main():
    largest_number = largest()
    print(largest_number)

if __name__ == "__main__":
    main()