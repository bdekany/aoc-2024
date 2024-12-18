#!/usr/bin/python3

def next_tile(x, y, dx, dy):
    x = max(min(x + dx, 9), 0)
    y = max(min(y + dy, 9), 0)
    return x, y

carte = list()
directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1]
]

resulat_puzzle_part1 = 0
x = 0
y = 0

# Ouvre le fichier en mode lecture
nom_fichier = 'puzzle-input.txt'
with open(nom_fichier, 'r') as fichier:
    # Lit chaque ligne du fichier
    for ligne in fichier:
        # Creation carte
        carte.append(ligne.strip())

x_max = len(carte)
y_max = len(carte[0])

while x < x_max:
    while y < y_max:
        if carte[x][y] == "X":
            for dx, dy in directions:
                tx = x + dx
                ty = y + dy
                
                if tx == -1 or tx == x_max or ty == -1 or ty == y_max:
                    continue 
                if carte[tx][ty] == "M":
                    tx = tx + dx
                    ty = ty + dy
                    if tx == -1 or tx == x_max or ty == -1 or ty == y_max:
                        continue 
                    if carte[tx][ty] == "A":
                        tx = tx + dx
                        ty = ty + dy
                        if tx == -1 or tx == x_max or ty == -1 or ty == y_max:
                            continue 
                        if carte[tx][ty] == "S":
                                #print("from:",x, y, "to", tx, ty)
                                resulat_puzzle_part1 += 1
        y += 1
    y = 0
    x += 1


print ("Day4 - Part1: ", resulat_puzzle_part1)

x = 1
y = 1

resulat_puzzle_part2 = 0

while x < x_max-1:
    while y < y_max-1:
        if carte[x][y] == "A":
            first = carte[x-1][y-1] + carte[x+1][y+1]
            second =  carte[x+1][y-1] + carte[x-1][y+1]
            if (first == "MS" or first == "SM") and (second == "MS" or second == "SM"):
                #print("x,y:", x,y)
                resulat_puzzle_part2 += 1

        y += 1
    y = 1
    x += 1

print ("Day4 - Part2: ", resulat_puzzle_part2)