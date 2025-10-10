# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({"name" : name, "director" : director, "year" : year, "runtime" : runtime})


def find_movies(database: list, search_term: str):
    result_list = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            result_list.append(movie)
    return result_list

def main():
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)


if __name__ == "__main__":
    main()
