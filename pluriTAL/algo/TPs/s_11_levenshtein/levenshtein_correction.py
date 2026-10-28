"""
Eric Jordan
Algorithmique et Programmation
2025-2026

This file contains an implementation of the levenshtein (edit) distance.

Some relevant resources :
Edit-distance https://en.wikipedia.org/wiki/Edit_distance - methods for calculating string similarity
Levenshtein distance https://en.wikipedia.org/wiki/Levenshtein_distance
Dynamic Programming https://en.wikipedia.org/wiki/Dynamic_programming - The paradigm this algorithm belongs to

This algorithm is commonly used in ASR for measuring word error rate and character error rate :
https://en.wikipedia.org/wiki/Word_error_rate
"""
import argparse


def verbose_levenshtein(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein (edit) distance between two strings.
    Args:
        s1: source string (reference)
        s2: target string (hypothesis)
    Returns:
        Integer edit distance
    """
    m, n = len(s1), len(s2)

    # Initialize DP table with zeros
    t = [[0] * (n + 1) for _ in range(m + 1)]

    print("Initialised table:")
    _print_table(t, s1, s2)

    # Cost of transforming to/from empty string
    for i in range(m + 1):
        t[i][0] = i

    for j in range(n + 1):
        t[0][j] = j

    print("To / from empty string:")
    _print_table(t, s1, s2)

    # Fill the table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            step = (i - 1) * n + j

            print(f"Step {step} - comparing {s1[:i]} vs {s2[:j]}")
            if s1[i - 1] == s2[j - 1]:
                t[i][j] = t[i - 1][j - 1]
                print(f"Step {step} — Match: '{s1[i-1]}' == '{s2[j-1]}', "
                      f"t[{i}][{j}] = {t[i][j]}")
                _print_table(t, s1, s2)

            else:
                sub  = t[i - 1][j - 1]  # substitute
                dele = t[i - 1][j]       # delete
                ins  = t[i][j - 1]       # insert

                best = min(sub, dele, ins)
                t[i][j] = 1 + best

                # Determine which operation was chosen.
                # N.B. In the case of a tie, substitution is chosen since it comes first here.
                # This may not always correspond to the actual operation performed, but from an
                # algorithmic perspective this is not important. Prenez cette indication avec prudence !
                if best == sub:
                    op = f"Substitute '{s1[i-1]}' → '{s2[j-1]}'"
                elif best == dele:
                    op = f"Delete '{s1[i-1]}'"
                else:
                    op = f"Insert '{s2[j-1]}' into {s2[:j]}"

                print(f"Step {step} — {op}: "
                      f"t[{i}][{j}] = 1 + {best} = {t[i][j]}")
                _print_table(t, s1, s2)

    print("Final table:")
    _print_table(t, s1, s2)  # FIX: removed stray "DP" suffix

    return t[m][n]


def levenshtein(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein (edit) distance between two strings.
    Args:
        s1: source string
        s2: target string
    Returns:
        Integer edit distance
    """
    m, n = len(s1), len(s2)

    t = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        t[i][0] = i
    for j in range(n + 1):
        t[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                t[i][j] = t[i - 1][j - 1]
            else:
                t[i][j] = 1 + min(
                    t[i - 1][j - 1],  # substitute
                    t[i - 1][j],      # delete
                    t[i][j - 1]       # insert
                )

    print("Final table:")
    _print_table(t, s1, s2)

    return t[m][n]


def _print_table(t, s1, s2):
    """Print the DP table in a readable format for demonstration purposes."""
    col_header = "       " + "   ".join(["''"] + list(s2))
    print(col_header)
    print("    " + "-" * (len(col_header) - 2))
    for i, row in enumerate(t):
        label = f"'{s1[i - 1]}'" if i > 0 else "''"
        print(f"{label:4} | " + "  ".join(f"{v:2}" for v in row))
    print()


def run(s1, s2, verbose):
    fn = verbose_levenshtein if verbose else levenshtein
    print("=" * 50)
    print(f"'{s1}' → '{s2}'" + (" (verbose)" if verbose else ""))
    print("=" * 50)
    d = fn(s1, s2)
    print(f"Levenshtein distance: {d}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute Levenshtein distance between two strings."
    )
    parser.add_argument("s1", nargs="?", default="chat", help="Source string")
    parser.add_argument("s2", nargs="?", default="chut", help="Target string")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print step-by-step DP table construction"
    )
    args = parser.parse_args()

    run(args.s1, args.s2, args.verbose)