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

   garden_positions = set([((0,0),starting_point[0], starting_point[1])])

   i = 0
   while True:
      if i == total_steps:
         break

      i += 1

      new_positions = set()

      for pos in garden_positions:
         map_index, row_index, column_index = pos
         
         l = len(new_positions)
         for r, c in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr = row_index + r
            nc = column_index + c
            map_shift = (0,0)

            if nr < 0:
               nr = rows_length - 1
               map_shift = (-1, 0)
               
            if nr == rows_length:
               nr = 0
               map_shift = (1, 0)
            
            if nc < 0:
               nc = cols_length - 1
               map_shift = (0, -1)
               
            if nc == cols_length:
               nc = 0
               map_shift = (0, 1)

            new_map_index = (map_index[0] + map_shift[0], map_index[1] + map_shift[1])
            if matrix[nr][nc] != '#':
               new_positions.add((new_map_index, nr, nc))

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
print("sample input: ", solve(SAMPLE_INPUT, 10))
print("sample input: ", solve(SAMPLE_INPUT, 50))
print("sample input: ", solve(SAMPLE_INPUT, 100))
print("sample input: ", solve(SAMPLE_INPUT, 500))
print("sample input: ", solve(SAMPLE_INPUT, 1000))
print("sample input: ", solve(SAMPLE_INPUT, 5000))

# with open("input.txt", "r") as input_file:
#     print("input: ", solve(input_file.read().strip(), 64))

