# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = 0
        self.count = 0

    def __str__(self):
        if self.count > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{self.count} ratings, average {(self.rating/self.count):.1f} points"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\nno ratings"

    def rate(self, rating: int):
        if -1 < rating < 6:
            self.count += 1
            self.rating += rating

def minimum_grade(rating: float, series_list: list):
    rating_lst = []
    for series in series_list:
        if series.rating >= rating:
            rating_lst.append(series)
    return rating_lst

def includes_genre(genre: str, series_list: list):
    genres_lst = []
    for series in series_list:
        if genre in series.genres:
            genres_lst.append(series)
    return genres_lst
    
