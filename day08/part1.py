
def solve(input_str: str):

    instructions, lines = input_str.split("\n\n")
    instructions = list(map(int, instructions.replace("L", "0").replace("R","1")))

    m = {}
    for line in lines.splitlines():
        a, b = line.split(" = ")
        m[a] = tuple(b.replace("(","").replace(")", "").split(", "))        

    i = 0
    l = len(instructions)
    n = "AAA"
    while n != "ZZZ":
        n = m[n][instructions[i % l]]
        i += 1

    return i


SAMPLE_INPUT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

SAMPLE_INPUT_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

print("sample input 1: ", solve(SAMPLE_INPUT))

print("sample input 2: ", solve(SAMPLE_INPUT_2))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))