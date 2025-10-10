# write your solution here

text = input("Write text: ")
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

corrected_text = " ".join(corrected_text_lst)
print(corrected_text)