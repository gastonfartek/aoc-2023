from collections import defaultdict

def card_type(a):
    
    temp = defaultdict(int)
    j = 0
    for n in a:
        j += 1 if n == 1 else 0
        temp[n] += 1 if n > 1 else 0

    n = list(temp.values())

    n.sort(reverse=True)

    if n[0] + j == 5:
        return 7

    if n[0] + j == 4:
        return 6
    if n[0] + j == 3 and n[1] == 2:
        return 5

    if n[0] + j == 3 and n[1] == 1:
        return 4
    
    if n[0] + j == 2 and n[1] == 2:
        return 3
    
    if n[0] + j == 2 and n[1] == 1:
        return 2

    return 1


def solve(input_str: str):
    temp = {
       'A': 14, 
       'K': 13, 
       'Q': 12, 
       'J': 1, 
       'T': 10 
    }

    result = []
    for line in input_str.splitlines():
       left, right = line.split(" ")
       left = list(map(lambda c: int(c) if c.isnumeric() else temp[c], left))
       right = int(right)
       result.append(([card_type(left)] + left, right))        

    result.sort()
    total = 0
    for i, el in enumerate(result):
        a,b = el
        total += b * (i+1)

    return total


SAMPLE_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))