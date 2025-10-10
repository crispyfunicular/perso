# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def items_by_season(series: dict):
        return series["rating"]
    return sorted(items, key=items_by_season, reverse=True)


def main():
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")


if __name__ == "__main__":
    main()
