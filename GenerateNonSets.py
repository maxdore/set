from random import randint
import itertools
import sys
from CreateGameImage import save_game_image

def random_game():
    return [(randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2)) for i in range(9)]

def check_game(game):
    for combination in itertools.combinations(game, 3):
        if check_set(combination):
            return combination

    return False

def check_set(c):
    return all([(c[0][i] == c[1][i] and c[0][i] == c[2][i]) or (c[0][i] != c[1][i] and c[0][i] != c[2][i] and c[1][i] != c[2][i]) for i in range(4) ])


num = 1 if len(sys.argv) == 1 else int(sys.argv[1])
print(num)
i = 0
while i < num:

    game = random_game()
    print(game)
    res = check_game(game)
    if not res:
        print("Game without a set!")
        save_game_image(game)
        i += 1
    else:
        print("Game contains a set:")
        for c in res:
            print(c)
