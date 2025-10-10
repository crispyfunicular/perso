# WRITE YOUR SOLUTION HERE:
def  most_common_words(filename: str, lower_limit: int) -> dict:
    dico = {}
    with open(filename) as my_file:
        for line in my_file:
            line = line.strip()
            parts = line.split(";")
                        
            clean_sentence = []
            for part in parts:
                sentence = part.split()
                for word in sentence:
                    word = word.strip(".,;:!?")
                    clean_sentence.append(word)            
    
            for word in clean_sentence:
                if word not in dico:
                    dico[word] = 1
                else:
                    dico[word] += 1    
    #print(dico)    
    
    return {letter: dico[letter] for letter in dico if dico[letter] >= lower_limit}


def main():
    print(most_common_words("comprehensions.txt", 3))


if __name__ == "__main__":
    main()
