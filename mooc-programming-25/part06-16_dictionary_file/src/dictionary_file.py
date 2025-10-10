# Write your solution here
function = "0"

while function != "3":    
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")

    if function == "1":
        finnish = input("The word in Finnish: ").lower()
        english = input("The word in English: ").lower()
        with open("dictionary.txt", "a") as my_file:       
            my_file.write(f"{finnish} - {english}\n") 
        print("Dictionary entry added")

    elif function == "2":
        search_term = input("Search term: ").lower()
        with open("dictionary.txt") as new_file:
            for line in new_file:
                entry = line.strip()
                if search_term in entry:
                    print(entry)    
    
    elif function == "3":
        print("Bye!")