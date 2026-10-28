"""
Eric Jordan
TP Algorithmes & Programmation - Dictionnaires, tri, recherche, lectures de fichiers
25-26

You must:
1. Implement insertion sort (by year)
2. Implement bubble sort (by rating, descending)
3. Implement any sort by a key of choice
4. Implement binary search (by title)

BONUS:
5. Load a large library from a CSV file using argparse
"""

import argparse
import csv


# =========================
# Part 1 — Default Data
# =========================

default_library = [
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
# Utility Function
# =========================

def print_book(book):
    # Print all info for a single book in a nice format
    # TODO Change the print below to something plus jolie
    print(f"{book['title']} | {book['author']} | {book['year']} | Rating: {book['rating']}") # This is pretty

def print_library(library, limit=10):
    """Print all books nicely formatted."""
    for book in library[:limit]:
        print_book(book)
    print()


# =========================
# Part 2 — Sorting
# =========================

def insertion_sort_by_key(library, key):
    """
    Sort books by year (ascending) using insertion sort.
    Modifies the list in place.
    """
    for i in range(1, len(library)):
        current_book = library[i]
        j = i - 1

        # Move elements that are greater than current_book['year']
        # one position to the right
        while j >= 0 and library[j][key] > current_book[key]:
            library[j + 1] = library[j]
            j -= 1

        # Put current_book in its correct place
        library[j + 1] = current_book


def insertion_sort_by_year(library):
    """
    Sort books by year (ascending) using insertion sort.
    Modifies the list in place.
    """
    for i in range(1, len(library)):
        current_book = library[i]
        j = i - 1

        # Move elements that are greater than current_book['year']
        # one position to the right
        while j >= 0 and library[j]["year"] > current_book["year"]:
            library[j + 1] = library[j]
            j -= 1

        library[j + 1] = current_book


def bubble_sort_by_rating(library):
    """
    Sort books by rating (descending) using bubble sort.
    Modifies the list in place.
    """
    n = len(library)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if library[j]["rating"] < library[j + 1]["rating"]:
                library[j], library[j + 1] = library[j + 1], library[j]
                swapped = True

        # Optimization: stop if already sorted
        if not swapped:
            break


# =========================
# Part 3 — Searching
# =========================

def binary_search_by_title(library, target_title):
    """
    Perform binary search to find a book by title.
    Library MUST be sorted by title first.
    Return the book dictionary if found, else None.
    """
    left = 0 # Frontière gauche de notre recherche (commence au début de la liste)
    right = len(library) - 1 # Frontière droite de notre recherche (commence à la fin de la liste)
    target_title = target_title.lower()

    while left <= right: # Si nos frontières se sont dépassées, le livre n'est pas présent
        mid = (left + right) // 2
        mid_title = library[mid]["title"].lower()
        print(mid_title)

        if mid_title == target_title:
            return library[mid] # C'est bon, on a trouvé

        elif mid_title < target_title:
            left = mid + 1 # Le livre qu'on cherche devrait être après le mid, on décale la fronière gauche à sa droite

        else:
            right = mid - 1 # Le livre qu'on cherche devrait être avant le mid, on décale la fronière droite à la position avant mid

    return None

# =========================
# Bonus — Dictionary Practice
# =========================

def count_books_by_author(library):
    """
    Return a dictionary:
    {
        author_name: number_of_books
    }
    """
    author_counts = {}

    for book in library:
        author = book["author"]

        if author in author_counts:
            author_counts[author] += 1
        else:
            author_counts[author] = 1

    return author_counts

# =========================
# BONUS — CSV Loading
# =========================

def load_library_from_csv(filename):
    """
    Load books from a CSV file.

    The CSV file must contain columns:
    title,author,year,rating

    Return:
        A list of dictionaries in the same format as default_library.

    IMPORTANT:
    - Convert year to int
    - Convert rating to float
    """
    library = []

    # 1. Open the file
    with open(filename, 'r', encoding='utf-8') as file:
        # 2. Use csv.DictReader
        reader = csv.DictReader(file)
        
        for row in reader:
            # 3. Convert year and rating
            book = {
                "title": row["title"],
                "author": row["author"],
                "year": int(row["year"]),
                "rating": float(row["rating"])
            }
            # 4. Append dictionaries to library list
            library.append(book)

    return library


# =========================
# BONUS — Argparse
# =========================

def parse_arguments():
    """
    Parse command-line arguments.

    Optional arguments:
    --file   Path to CSV file
    --search Title to search for
    """
    parser = argparse.ArgumentParser(description="Mini Library Search Engine")

    parser.add_argument(
        "--file",
        type=str,
        help="Path to CSV file containing book data"
    )

    parser.add_argument(
        "--search",
        type=str,
        help="Title of book to search for"
    )

    return parser.parse_args()


# =========================
# Main Program
# =========================

def main():

    args = parse_arguments()

    # Load data
    if args.file:
        print(f"Loading library from {args.file}...")
        library = load_library_from_csv(args.file)
    else:
        print("Using default small library.")
        library = default_library.copy()

    print(f"Number of books loaded: {len(library)}\n")

    print("First books in library:")
    print_library(library)

    # Sort by year
    print("Sorting by year (Insertion Sort)...")
    insertion_sort_by_year(library)
    print_library(library)

    # Search
    if args.search:

        # IMPORTANT: Must sort by title first!
        print("Sorting by title (Insertion Sort)...")
        insertion_sort_by_key(library, "title")
        print_library(library)
        print(f"Searching for '{args.search}'...")
        result = binary_search_by_title(library, args.search)

        if result:
            print("Book found:")
            print_book(result)
        else:
            print("Book not found.")


if __name__ == "__main__":
    main()
