# Write your solution here

"""
Appelons les lettres L1, L2, ..., LN.
N vaut layers-1.
L'important c'est de réaliser les N+1 premiers mots.
Le premier est  LN répété N+1 fois.
Le deuxième est LN(suite)LN ou suite est L(N-1) répèté N fois.
Le troisième est LN L(N-1)(suite)L(N-1)LN ou suite est L(N-2) répèté N-1 fois,
ainsi de suite jusqu'à ce que (suite) soit égale à L1.
On peut faire une boucle.
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
 
def get_letter(row, col, size):
    """Compute the distance to the center and return the associated letter"""
    center_row = size - 1
    center_col = size - 1
    dist_row = abs(center_row - row)
    dist_col = abs(center_col - col)
    dist = max(dist_row, dist_col)
    return letters[dist]
 

def draw(size):
    """
    Draw patterns like this one for size = 4
    DDDDDDD
    DCCCCCD
    DCBBBCD
    DCBABCD
    DCBBBCD
    DCCCCCD
    DDDDDDD
    """
    
    if size <= 0 or size > len(letters):
        raise Exception(f"Max pattern size is {len(letters)}")
 
    pattern_size = size * 2 - 1
 
    for row in range(0, pattern_size):
        for col in range(0, pattern_size):
            print(get_letter(row, col, size), end="")
        print()

#for i in range(1, 10):
    #draw(i)
    #print() 

if True:
    layers = int(input("Layers: "))
else:
    layers = 3
    #layers = 4
draw(layers)