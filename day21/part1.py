from collections import defaultdict
from heapq import heappush, heappop

def solve(input_str: str, total_steps: int):
   lines = input_str.splitlines()

   matrix = []
   
   starting_point = None
   
   for i, line in enumerate(lines):
      matrix.append(list(line))
      if 'S' in line:
         starting_point = (i, line.index("S"))

   rows_length = len(matrix)
   cols_length = len(matrix[0])

   garden_positions = set([starting_point])

   i = 0
   while True:
      if i == total_steps:
         break

      i += 1

      new_positions = set()

      for pos in garden_positions:
         row_index, column_index = pos
         
         l = len(new_positions)
         for r, c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr = row_index + r
            nc = column_index + c

            if 0 <= nr < rows_length and 0 <= nc < cols_length and matrix[nr][nc] != '#' and (nr, nc) not in garden_positions:
               new_positions.add((nr,nc))

      garden_positions = new_positions


   total = len(garden_positions)
   return total

SAMPLE_INPUT = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

print("sample input: ", solve(SAMPLE_INPUT, 6))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read().strip(), 64))

