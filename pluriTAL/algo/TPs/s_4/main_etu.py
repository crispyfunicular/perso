"""
Eric Jordan
TP Algorithmes & Programmation - Dictionnaires, tri, recherche
25-26

You must:
1. Implement insertion sort (by year)
2. Implement bubble sort (by rating, descending)
3. Implement binary search (by title)
"""


# =========================
# Part 1 — Un jeu de données
# =========================

library = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "rating": 4.8},
    {"title": "1984", "author": "George Orwell", "year": 1949, "rating": 4.7},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "rating": 4.8},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951, "rating": 4.6},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "rating": 4.5},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "rating": 4.4},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "rating": 4.0},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "rating": 4.9},
]


# =========================
# Print functions
# =========================

def print_book(book):
    # Print all info for a single book in a nice format
    # TODO Change the print below to something plus jolie
    print(f"{book}") # This is ugly

def print_library(library):
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
    # TODO: Implement insertion sort
    pass


def bubble_sort_by_rating(library):
    """
    Sort the books by rating (descending)
    using BUBBLE SORT.

    Modify the list in place.
    """
    # TODO: Implement bubble sort
    pass


def bubble_sort_by_key(library, key):
    """
    Sort using the algorithm of your choice, by the specified key.

    Modify the list in place.
    """
    # TODO: Implement the sort of your choosing
    pass




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
    # TODO: Implement binary search
    pass


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
    pass


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
    result = binary_search_by_title(library, "Dune")

    if result:
        print("Book found:", result)
    else:
        print("Book not found.")

    # ---- Bonus ----
    print("Counting books by author...")
    author_counts = count_books_by_author(library)
    print(author_counts)

    # ---- Bonus++ ----
    # Utiliser la librairie argparse pour lire les livres d'un fichier .csv


if __name__ == "__main__":
    main()
