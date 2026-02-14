"""
Eric Jordan
TP Algorithmes & Programmation - Dictionnaires, tri, recherche
25-26

You must:
1. Implement insertion sort (by year)
2. Implement bubble sort (by rating, descending)
3. Implement binary search (by title)
"""

import argparse


# =========================
# Part 1 — Un jeu de données
# =========================

library = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "rating": 4.8},
    {"title": "1984", "author": "George Orwell", "year": 1949, "rating": 4.7},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "rating": 4.8},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951, "rating": 4.6},
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "rating": 4.5,
    },
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "rating": 4.4},
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "rating": 4.0,
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "year": 1954,
        "rating": 4.9,
    },
]


# =========================
# Print functions
# =========================


def print_book(book: dict):
    # Print all info for a single book in a nice format
    # TODO Change the print below to something plus jolie
    print(
        f"titre : {book['title']}, auteur : {book['author']}, année : {book['year']}, note : {book['rating']}"
    )  # This is ugly


def print_library(library: list):
    """Print all books nicely formatted."""
    for book in library:
        print_book(book)
    print()


# =========================
# Part 2 — Sorting
# =========================


def insertion_sort_by_year(library):
    """
    Sort the books by year (ascending)
    using INSERTION SORT.

    Modify the list in place.
    """

    for i in range(1, len(library)):
        # On sauvegarde l'élément actuel (le livre) à insérer
        key_book = library[i]

        # On initialise j pour comparer avec les éléments à gauche de i
        j = i - 1

        # On déplace les éléments de library[0..i-1] qui sont plus récents
        # que l'année du livre actuel, vers une position en avant
        while j >= 0 and library[j]["year"] > key_book["year"]:
            library[j + 1] = library[j]
            j -= 1

        # On place enfin le livre à sa position correcte
        library[j + 1] = key_book


def bubble_sort_by_rating(library):
    """
    Sort the books by rating (descending)
    using BUBBLE SORT.

    Modify the list in place.
    """
    # TODO: Implement bubble sort
    while True:
        perm = 0
        i = 0
        while i < len(library) - 1:
            year = library[i]["year"]
            year1 = library[i + 1]["year"]

            if year > year1:
                library[i] = year1
                library[i + 1] = year
                perm += 1

            i += 1

        if perm == 0:
            break

    return library


def bubble_sort_by_key(library, key):
    """
    Sort using the algorithm of your choice, by the specified key.
    Modify the list in place.
    """
    for book in library:
        if not key in book:
            return

    for i in range(1, len(library)):
        # On sauvegarde l'élément actuel (le livre) à insérer
        key_book = library[i]

        # On initialise j pour comparer avec les éléments à gauche de i
        j = i - 1

        # On déplace les éléments de library[0..i-1] qui sont plus récents
        # que l'année du livre actuel, vers une position en avant
        while j >= 0 and library[j][key] > key_book[key]:
            library[j + 1] = library[j]
            j -= 1

        # On place enfin le livre à sa position correcte
        library[j + 1] = key_book


# =========================
# Part 3 — Searching
# =========================


def binary_search_by_title(library, target_title):
    """
    Perform binary search to find a book by title.

    IMPORTANT:
    - The library MUST be sorted by title first.
    - Return the book dictionary if found.
    - Return None if not found.

    - What happens if the case of the title is different ? e.g. Dune vs dune
    """
    min_i = 0
    max_i = len(library) - 1

    while min_i < max_i - 1:
        mid = (min_i + max_i) // 2
        library[mid]["title"]
        if target_title.lower() < library[mid]["title"].lower():
            max_i = mid
        if target_title.lower() > library[mid]["title"].lower():
            min_i = mid
        if target_title.lower() == library[mid]["title"].lower():
            return library[mid]

    return None


# =========================
# Bonus — Dictionary Practice
# =========================


def count_books_by_author(library):
    """
    Create and return a dictionary:
    {
        author_name: number_of_books
    }
    """
    # TODO: Implement using a dictionary
    dict_authors = {}

    for book in library:
        auteur = book["author"]
        if auteur not in dict_authors:
            dict_authors[auteur] = 0
        dict_authors[auteur] += 1

    return dict_authors


# =========================
# Main Program
# =========================


def main():
    print("Original library:")
    print_library(library)

    # ---- Test Insertion Sort ----
    print("Sorting by year (Insertion Sort)...")
    insertion_sort_by_year(library)
    print_library(library)

    # ---- Test Bubble Sort ----
    print("Sorting by rating (Bubble Sort)...")
    bubble_sort_by_rating(library)
    print_library(library)

    # ---- Test Binary Search ----
    print("Binary search by title")
    # Make sure library is sorted by title before calling this!
    bubble_sort_by_key(library, "title")
    result = binary_search_by_title(library, "Dune")

    if result:
        print("Book found:", result)
    else:
        print("Book not found.")

    # ---- Bonus ----
    print()
    print("Counting books by author...")
    author_counts = count_books_by_author(library)

    for auteur, nb in author_counts.items():
        print(auteur, nb, sep="\t")

    # ---- Bonus++ ----
    # Utiliser la librairie argparse pour lire les livres d'un fichier .csv


if __name__ == "__main__":
    main()
