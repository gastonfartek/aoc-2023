from collections import defaultdict

def solve(input_str: str):
    lines = input_str.splitlines()
    rows_length = len(lines)
    cols_length = len(lines[0])
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            if val != '.':
                continue

            counts = 0
            left = j - 1
            right = j + 1
            top = i - 1
            bottom = i + 1
            while True:
                if left < 0 and top < 0 and right >= cols_length and bottom >= rows_length:
                    break

                if left >= 0:

            

    


    


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

# print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

