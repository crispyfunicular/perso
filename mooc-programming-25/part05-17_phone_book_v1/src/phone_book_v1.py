# Write your solution here
contacts = {}
while True:
    
    command = int(input("command (1 search, 2 add, 3 quit): "))
        
    #search
    if command == 1:
        name = input("name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("no number")        
    
    #add
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        contacts[name] = number
        print("ok!")

    #quit
    elif command == 3:
        print("quitting...")
        break
