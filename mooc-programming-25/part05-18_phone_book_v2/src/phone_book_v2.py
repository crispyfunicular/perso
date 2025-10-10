# Write your solution here
contacts = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
        
    #search
    if command == 1:
        name = input("name: ")
        if name in contacts:
            for number in contacts[name]:
                print(number)
        else:
            print("no number")        
    
    #add
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in contacts:
            contacts[name] = []
        contacts[name].append(number)
        print("ok!")

    #quit
    elif command == 3:
        print("quitting...")
        break
