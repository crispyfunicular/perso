# Write your solution here

def find_words(search_term: str):
    search_results = []
    with open("words.txt") as new_file:
        for line in new_file:
            entry = line.strip()
            if search_term == entry:
                search_results.append(entry)
            elif search_term[0] == "*":
                if entry.endswith(search_term[1:]):
                    search_results.append(entry)
            elif search_term[-1] == "*":
                if entry.startswith(search_term[:-1]):
                    search_results.append(entry)
            elif "." in search_term:
                if len(search_term) == len(entry):
                    #print(len(search_term))
                    i = 0
                    while i < len(search_term):
                        #print(search_term[i])
                        if search_term[i] != "." and search_term[i] != entry[i]:
                            break
                        if i == len(search_term) - 1:
                            search_results.append(entry)
                            break
                        else:
                            i += 1
                                                
    return search_results


def main():
    if True:
        search_term = input("Search term: ").lower()
    else:
        search_term = "cat"
        #search_term = "*vokes"
    print(find_words(search_term))

if __name__ == "__main__":
    main()
