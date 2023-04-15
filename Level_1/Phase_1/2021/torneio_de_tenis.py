game = list()
for c in range(0, 6):
    game.append(input()) #game 1 to 6

V = game.count('V')

if V >= 5:
    group = 1
elif 3 <= V <= 4:
    group = 2
elif 1 <= V <= 2:
    group = 1
else:
    group = -1

print(group)
