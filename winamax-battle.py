#!/usr/bin/python3
# https://www.codingame.com/ide/puzzle/winamax-battle

import sys
import math

p1 = []
p2 = []


def rank(card):
    return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"].index(card[:-1])


n = int(input())  # the number of cards for player 1
for i in range(n):
    p1.append(input())  # the n cards of player 1

m = int(input())  # the number of cards for player 2
for i in range(m):
    p2.append(input())  # the m cards of player 2

# Write an answer using print
# print(p2, file=sys.stderr, flush=True)
result = "PAT"
p1_deck = []
p2_deck = []
game_rounds = [0, 0]
while True:
    if len(p1) == 0 or len(p2) == 0:
        if game_rounds[0] > game_rounds[1]:
            result = f"1 {game_rounds[0]}"
        else:
            result = f"2 {game_rounds[1]}"
        break

    p1_card = p1.pop(0)
    p2_card = p2.pop(0)

    if rank(p1_card) > rank(p2_card):
        game_rounds[0] += 1
    elif rank(p1_card) < rank(p2_card):
        game_rounds[1] += 1
    else:
        # WAR
        pass

print(result)
