# Write your solution here

def txt_to_dict(filename: str):
    dict_recipes = {}
    with open(filename) as new_file:
        recipe_name = None
        preparation_time = None
        ingredients = []

        for line in new_file:
            line = line.strip()
            if line != "" and line[0].isupper():
                recipe_name = line
            elif line.isnumeric():
                preparation_time = int(line)
            elif line == "":
                dict_recipes[recipe_name] = (preparation_time, ingredients)
                recipe_name = None
                preparation_time = None
                ingredients = []
            else:
                ingredients.append(line)
        
        if recipe_name != None:
            dict_recipes[recipe_name] = (preparation_time, ingredients)

    return dict_recipes


def search_by_name(filename: str, word: str):
    dict_recipes = txt_to_dict(filename)
    search_result = []

    for element in dict_recipes:       
        if word.lower() in element.lower():
            search_result.append(element.capitalize())
    return search_result


def search_by_time(filename: str, prep_time: int):
    dict_recipes = txt_to_dict(filename)
    search_result = []
    for recipe in dict_recipes:
        if  dict_recipes[recipe][0] <= prep_time:
            search_result.append(f"{recipe}, preparation time {dict_recipes[recipe][0]} min")
    return search_result


def search_by_ingredient(filename: str, ingredient: str):
    dict_recipes = txt_to_dict(filename)
    search_result = []
    for recipe in dict_recipes:
        if  ingredient in dict_recipes[recipe][1]:
            search_result.append(f"{recipe}, preparation time {dict_recipes[recipe][0]} min")
    return search_result


def main():
    #filename = "recipes1.txt"
    #word = ""
    #prep_time = "15"
    #ingredient = ""
    filename = input("Filename: ")
    word = input("Word: ")
    prep_time = input("Prep time: ")
    ingredient = input("Ingredient: ")
    if word != "":
        result = search_by_name(filename, word)
    elif prep_time != "":
        result = search_by_time(filename, int(prep_time))
    elif ingredient != "":
        search_by_ingredient(filename, ingredient)
    
    print(result)


if __name__ == "__main__":
    main()