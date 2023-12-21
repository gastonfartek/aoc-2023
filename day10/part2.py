from collections import defaultdict


from collections import defaultdict


def solve(input_str: str):
    lines = input_str.splitlines()
    rows_length = len(lines)
    cols_length = len(lines[0])

    # PART 1
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
    loop = {}
    o = "e"
    while True:
        next_i, next_j = orientation[o]
        current_position = (current_position[0] + next_i, current_position[1] + next_j)

        loop[current_position] = lines[current_position[0]][current_position[1]]

        if current_position == starting_pos:
            break

        pipe = lines[current_position[0]][current_position[1]]
        o = pipe_map[pipe][o]

    # 

    pipes = ["|","L","J"]
    total = 0
    for i in range(rows_length):
        for j in range(cols_length):
            if lines[i][j] != '.':
                continue
            k = j - 1

            count = 0
            while k >= 0:
                if (i,k) in loop and loop[(i,k)] in pipes:
                    count += 1
                k -= 1

            total += 1 if count % 2 == 1 else 0

    return total    


SAMPLE_INPUT = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

