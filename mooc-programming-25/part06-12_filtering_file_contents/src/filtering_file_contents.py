# Write your solution here
def filter_solutions():

    with open("correct.csv", "w") as my_file:
        pass             
    with open("incorrect.csv", "w") as my_file:
        pass
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            maths = (parts[1], parts[2])
            response = int(maths[1])
            if "+" in maths[0]:
                calcul = maths[0].split("+")
                left = int(calcul[0])
                right = int(calcul[1])
                if left + right == response:
                    with open("correct.csv", "a") as my_file:       
                        my_file.write(f"{name};{maths[0]};{maths[1]}\n")   
                else:
                    with open("incorrect.csv", "a") as my_file: 
                        my_file.write(f"{name};{maths[0]};{maths[1]}\n") 
            else:                
                calcul = maths[0].split("-")
                left = int(calcul[0])
                right = int(calcul[1])
                if left - right == response:
                    with open("correct.csv", "a") as my_file:    
                        my_file.write(f"{name};{maths[0]};{maths[1]}\n")    
                else:
                    with open("incorrect.csv", "a") as my_file:       
                        my_file.write(f"{name};{maths[0]};{maths[1]}\n")  


def main():
    filter_solutions()

if __name__ == "__main__":
    main()
