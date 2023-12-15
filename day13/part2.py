

def calculate(pattern: str):

    def diff(i_a,i_b):

        a = list(pattern[i_a])
        b = list(pattern[i_b])
        
        found = 0
        
        for j in range(len(a)):
            if a[j] != b[j]:
                found += 1

        return found

    diffs = 0
    for i in range(1,len(pattern)):
        diffs = diff(i-1, i)
        if diffs > 1:
            continue
        
        prev = i - 1
        n = i

        while True:
            prev -= 1
            n += 1

            if prev < 0 or n >= len(pattern):
                if diffs == 1:
                    return i
                break

            if pattern[prev] != pattern[n]:
                if diffs == 1:
                    break

                diffs = diff(prev,n)

                if diffs > 1:
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

print("sample input 2a: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: 27202", solve(input_file.read()))

