# Write your solution here
from difflib import get_close_matches
suggestions = {}

if True:
    text = input("write text: ")
else:
    #text = "We use ptython to make a spell checker"
    text = "this is acually a good and usefull program"
    #text = "This iis good"

text_parts = text.split()
corrected_text_lst = []
dico = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        dico.append(line)

for word in text_parts:
    if word.lower() in dico:
        corrected_text_lst.append(word)
    else:
        corrected_text_lst.append("*" + word + "*")    
        suggestions[word] = get_close_matches(word, dico)
    corrected_text = " ".join(corrected_text_lst)
    #print(corrected_text)

print(corrected_text)
print("suggestions:")
for word in suggestions:
    print(f"{word}: {suggestions[word][0]}, {suggestions[word][1]}, {suggestions[word][2]}")
    



