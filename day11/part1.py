from collections import defaultdict

def solve(input_str: str):
    lines = input_str.splitlines()
    rows_length = len(lines)
    cols_length = len(lines[0])
    
    cols_count = defaultdict(int)
    galaxies = {}

    rows_count = 0
    for i in range(len(lines)):
        line = list(lines[i])
        
        if '#' not in line:
            rows_count += 1


        for j in range(cols_length):
            if line[j] != '#':
                cols_count[j] += 1
                continue
            
            galaxies[(i, j)] = (i + rows_count, j)

    seen = set()
    result = 0
    for  i, row in enumerate(lines):
        added_cols = 0
        for j in range(cols_length):
            if cols_count[j] == rows_length:
               added_cols += 1
            
            if row[j] != '#':
                continue
            
            current_galaxy_key = (i,j)
            galaxies[current_galaxy_key] = (galaxies[current_galaxy_key][0], j + added_cols)


    for current_galaxy_key in galaxies.keys():
        for key in galaxies.keys():
            if current_galaxy_key == key:
                continue
            galaxy = galaxies[key]
            if (current_galaxy_key, key) in seen:
                continue

            result += abs(galaxy[0] - galaxies[current_galaxy_key][0]) + abs(galaxy[1] - galaxies[current_galaxy_key][1])
            seen.add((current_galaxy_key, key))
            seen.add((key, current_galaxy_key))

    return result


SAMPLE_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

