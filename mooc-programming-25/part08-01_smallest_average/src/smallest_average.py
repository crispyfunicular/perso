# Write your solution here

def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    average1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    min = average1
    returned_dict = person1

    average2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    if average2 < min:
        min = average2     
        returned_dict = person2

    average3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3
    if average3 < min:
        min = average3
        returned_dict = person3
    
    return returned_dict


def main():
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
    #{'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}

if __name__ == "__main__":
    main()

