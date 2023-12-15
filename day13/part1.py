def calculate(pattern: str):

    for i in range(1,len(pattern)):
        if pattern[i-1] != pattern[i]:
            continue

        prev = i - 1
        n = i

        while True:
            prev -= 1
            n += 1

            if prev < 0 or n >= len(pattern):
                return i

            if pattern[prev] != pattern[n]:
                break

    return 0

def solve(input_str: str):
    patterns = input_str.split("\n\n")
    total = 0
    for pattern in patterns:
        rows = pattern.splitlines()
        columns = list(zip(*rows))
        
        total_rows =  calculate(rows)      
        total_cols = calculate(columns)

        total += (total_cols + 100 * total_rows)

    return total


SAMPLE_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

SAMPLE_INPUT_2 = """####.##.#..#.#...
....##.####.#.#..
....##.####.#.#..
####.##.#..#.#...
..#####...####.##
#####..##.###...#
.##...##.....###.
.##...##.....###.
#####..##.###...#
..#####...####.##
#.##.##.#..#.#..."""

print("sample input 2a: ", solve(SAMPLE_INPUT_2))

with open("input.txt", "r") as input_file:
    print("input: 27202", solve(input_file.read()))

