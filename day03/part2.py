import pprint
from collections import deque

pp = pprint.PrettyPrinter(indent=4)

def solve(input_str: str):

  matrix = []

  symbols = []

  for i, line in enumerate(input_str.splitlines()):
    chars = list(line)
    matrix.append(chars)

    for j, char in enumerate(chars):
      if char == "*":
        symbols.append((i,j))

  result = 0

  row_length = len(matrix)
  cols_length = len(matrix[0])

  visited = set()

  for i, j in symbols:
    numbers = []
    for di, dj in [(-1,0),(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]:
      next_i = i + di
      next_j = j + dj

      if next_i < 0 or next_i > row_length or next_j < 0 or next_j > cols_length or (next_i, next_j) in visited or not matrix[next_i][next_j].isnumeric():
        continue
      
      
      n_index = next_j
      number = deque()

      while n_index >= 0 and matrix[next_i][n_index].isnumeric():
        visited.add((next_i, n_index))
        number.appendleft(matrix[next_i][n_index])
        n_index -= 1
      
      n_index = next_j + 1
      while n_index < cols_length and matrix[next_i][n_index].isnumeric():
        visited.add((next_i, n_index))
        number.append(matrix[next_i][n_index])
        n_index += 1

      numbers.append( int(''.join(number)))
    
    if len(numbers) == 2:
      result += numbers[0] * numbers[1]

  return result



SAMPLE_IMPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

print("sample input: ", solve(SAMPLE_IMPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))