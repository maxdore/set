from random import randint
import itertools
import sys
import argparse
from CreateGameImage import save_game_image

def random_game():
    game = False
    while game == False or len(game) != len(set(game)):
        game = [(randint(0, 2), randint(0, 2), randint(0, 2), randint(0, 2)) for i in range(9)]
    return game

def sets_in_game(game):
    res = []
    for combination in itertools.combinations(game, 3):
        if is_set(combination):
            res.append(combination)
    return res

def is_set(c):
    return all([(c[0][i] == c[1][i] and c[0][i] == c[2][i]) or (c[0][i] != c[1][i] and c[0][i] != c[2][i] and c[1][i] != c[2][i]) for i in range(4) ])

def is_type1(s):
    eqs = list(filter(lambda i: s[0][i] == s[1][i] and s[1][i] == s[2][i], range(4)))
    return len(eqs) == 3

def is_type3(s):
    eqs = list(filter(lambda i: s[0][i] == s[1][i] and s[1][i] == s[2][i], range(4)))
    return len(eqs) == 1

parser = argparse.ArgumentParser()
parser.add_argument('type', action="store", type=int, default=0)
parser.add_argument('num', action="store", type=int, default=1)

args = parser.parse_args()
print(args)

i = 0
while i < args.num:
    game = random_game()
    print("NEW GAME")
    print(game)
    sets = sets_in_game(game)
    print(sets)
    if args.type == 0:
        if len(sets) == 0:
            print("Game without a set")
            save_game_image(game)
            i += 1
    elif args.type == 1:
        if len(list(filter(is_type1, sets))) == 1 and len(sets) == 1:
            print("Game contains one set of type 1")
            save_game_image(game)
            i += 1
    elif args.type == 3:
        if len(list(filter(is_type1, sets))) == 0 and len(sets) == 1:
            print("Game contains one set of type 3")
            save_game_image(game)
            i += 1
