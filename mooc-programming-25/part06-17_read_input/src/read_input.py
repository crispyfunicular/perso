# Write your solution here
def read_input(input_quote: str, nb1: int, nb2: int):
    while True:
        try:   
            number = int(input(input_quote))
            if nb1 <= number and number <= nb2:
                print("You typed in:", number)
                break
            else:
                print(f"You must type in an integer between {nb1} and {nb2}")
        except ValueError:
            print(f"You must type in an integer between {nb1} and {nb2}")

    return number


def main():
    input_quote = "Please type in a number: "
    nb1 = 5
    nb2 = 10
    read_input(input_quote, nb1, nb2)
        

if __name__ == "__main__":
    main()
