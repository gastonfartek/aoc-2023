def solve(input_str: str):
  matrix = [list(r) for r in input_str.splitlines()]

  transposed = list(zip(*matrix))

  length = len(transposed[0])

  total = 0
  for row in transposed:
     add = 0
     for i, col in enumerate(row):
        if col == 'O':
           total += length - i + add
        
        if col == ".":
           add += 1

        if col == '#':
           add = 0

  return total

SAMPLE_INPUT = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

