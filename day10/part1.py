from collections import defaultdict

def solve(input_str: str):

    lines =  input_str.splitlines()

    orientation = {
        "s": (1,0),
        "e": (0,1),
        "w": (0,-1),
        "n": (-1,0)
    }
    pipe_map = {
        "|": {
            "s": "s",
            "n": "n" 
        },
        "-": {
            "e": "e", 
            "w": "w"
        },
        "L": {
            "s": "e",
            "w": "n",
        },
        "J": {
            "s": "w", 
            "e": "n"
        },
        "7": {
            "e": "s",
            "n": "w"
        },
        "F": {
            "n": "e",
            "w": "s"
        }
    }

    starting_pos = None

    for i in range(0, len(lines)):
        if 'S' not in lines[i]:
            continue

        starting_pos = (i,lines[i].index('S'))
        break

    current_position = starting_pos
    o = "e"
    steps = 0
    while True:
        next_i, next_j = orientation[o]
        current_position = (current_position[0] + next_i, current_position[1] + next_j)
        steps += 1

        if current_position == starting_pos:
            break

        pipe = lines[current_position[0]][current_position[1]]
        o = pipe_map[pipe][o]

    return steps / 2


    


SAMPLE_INPUT = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

# print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

