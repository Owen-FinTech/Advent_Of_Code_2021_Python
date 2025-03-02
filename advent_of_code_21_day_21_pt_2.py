from __future__ import annotations
import functools
import itertools

input_string = '''''' # Insert your puzzle input between the triple quotes

p1: int
p2: int
splitString = input_string.split("\n")

for i in range(len(splitString)):
    for j in range(len(splitString[i]) - 1, -1, -1):
        if splitString[i][j] == " ":
            if i == 0:
                p1 = int(splitString[i][j + 1:])
                break
            else:
                p2 = int(splitString[i][j + 1:])
                break

def weird_mod(n: int) -> int:
    while n > 10:
        n -= 10
    return n

p1_score = p2_score = 0

@functools.lru_cache(maxsize=None)
def compute_wins(
    p1: int,
    p1_score: int,
    p2: int,
    p2_score: int,
) -> tuple[int, int]:
    p1_wins = p2_wins = 0
    for i, j, k in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        new_p1 = weird_mod(p1 + i + j + k)
        new_p1_score = p1_score + new_p1

        if new_p1_score >= 21:
            p1_wins += 1
        else:
            tmp_p2_wins, tmp_p1_wins = compute_wins(
                p2, 
                p2_score,
                new_p1,
                new_p1_score
            )
            p1_wins += tmp_p1_wins
            p2_wins += tmp_p2_wins
    return p1_wins, p2_wins

print(f'part 2: {compute_wins(p1, 0, p2, 0)}')