# Write your solution here
import string

def run(program: list[str]) -> list:
    values_dict = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
        "G" : 0,
        "I" : 0,
        "J" : 0,
        "K" : 0,
        "L" : 0,
        "M" : 0,
        "N" : 0,
        "O" : 0,
        "P" : 0,
        "Q" : 0,
        "R" : 0,
        "S" : 0,
        "T" : 0,
        "U" : 0,
        "V" : 0,
        "W" : 0,
        "X" : 0,
        "Y" : 0,
        "Z" : 0
    }
    result = []
    anchors_dict = {}
    
    i = 0
    for line in program:
        if ":" in line:
            anchor_name = line[:-1]
            anchors_dict[anchor_name] = i
        i += 1
    #print(anchors_dict)

    i = 0
    while i < len(program):
        line = program[i]
        line_lst = line.split(" ")
        command = line_lst[0]
        
        #print(i)
        #print(line)    

        if command in ["MOV", "ADD", "SUB", "MUL"]:
            value_right = get_value(line_lst[2], values_dict)

        if command == "PRINT":
            result.append(get_value(line_lst[1], values_dict))  
        if command == "MOV":
            values_dict[line_lst[1]] = value_right
        if command == "ADD":
            values_dict[line_lst[1]] += value_right
        if command == "SUB":
            values_dict[line_lst[1]] -= value_right
        if command == "MUL":
            values_dict[line_lst[1]] *= value_right
        if command == "END":
            break

        if command == "JUMP":
            i = anchors_dict[line_lst[1]] - 1
        if command == "IF":
            value_left = get_value(line_lst[1], values_dict)
            value_right = get_value(line_lst[3], values_dict)
            if line_lst[2] == ">":
                if value_left > value_right:
                    i = anchors_dict[line_lst[5]] - 1
            if line_lst[2] == ">=":
                if value_left >= value_right:
                    i = anchors_dict[line_lst[5]] - 1
            if line_lst[2] == "<":
                if value_left < value_right:
                    i = anchors_dict[line_lst[5]] - 1
            if line_lst[2] == "<=":
                if value_left <= value_right:
                    i = anchors_dict[line_lst[5]] - 1
            if line_lst[2] == "==":
                if value_left == value_right:
                    i = anchors_dict[line_lst[5]] - 1
            if line_lst[2] == "!=":
                if value_left != value_right:
                    i = anchors_dict[line_lst[5]] - 1
                    
        i += 1

    return result


def get_value(variable: str, values_dict: dict) -> int:
    if variable.isnumeric():
        value = int(variable)
    else:
        value = values_dict[variable]
    return value


def main():
    choice = 3
    if choice == 1:
        program1 = []
        program1.append("MOV A 1")
        program1.append("MOV B 2")
        program1.append("PRINT A")
        program1.append("PRINT B")
        program1.append("ADD A B")
        program1.append("PRINT A")
        program1.append("END")
    elif choice == 1.5:
        program1 = ['MOV A 5', 'PRINT A']
    elif choice == 2:
        program2 = []
        program2.append("MOV A 1")
        program2.append("MOV B 10")
        program2.append("begin:")
        program2.append("IF A >= B JUMP quit")
        program2.append("PRINT A")
        program2.append("PRINT B")
        program2.append("ADD A 1")
        program2.append("SUB B 1")
        program2.append("JUMP begin")
        program2.append("quit:")
        program2.append("END")
    elif choice == 3:
        program3 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']
    elif choice == 26:
        program26 = []
        program26.append("MOV A 1")
        program26.append("MOV B 10")
        program26.append("JUMP end")
        program26.append("ADD A 1")
        program26.append("SUB B 1")
        program26.append("end:")        
        program26.append("PRINT A")
        program26.append("PRINT B")
        program26.append("END")

    
    result = run(program3)
    print(result)


if __name__ == "__main__":
    main()
