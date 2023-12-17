from collections import deque

def solve(input_str: str):
  matrix = [list(s.rstrip()) for s in input_str.splitlines()]

  rows_length = len(matrix)
  cols_length = len(matrix[0])

  energized = set()

  directions_map = {
    "\\": {
      (0, 1): [(1, 0)],
      (0, -1): [(-1, 0)],
      (-1, 0): [(0, -1)],
      (1, 0): [(0, 1)]    
    },
    '/':{
      (0, 1): [(-1, 0)],
      (0, -1): [(1, 0)],
      (-1, 0): [(0, 1)],
      (1, 0): [(0, -1)]    
    },
    '-': {
      (0, 1): [(0, 1)],
      (0, -1): [(0, -1)],
      (1, 0): [(0, -1), (0, 1)],
      (-1, 0): [(0, -1), (0, 1)]
    },
    '|': {
      (0, 1): [(-1, 0), (1, 0)],
      (0, -1): [(-1, 0), (1, 0)],
      (1, 0): [(1, 0)],
      (-1, 0): [(-1, 0)]
    }
  }

  def bfs(index, direction):
    q = deque()
    q.append((index, direction))

    seen = set()

    while len(q):
      index, direction = q.popleft()
      r,c = index
      dr, dc = direction

      if not (0 <= r < rows_length and 0 <= c < cols_length):
        continue

      energized.add(index)

      if (index,direction) in seen:
        continue
      
      seen.add((index, direction))

      if matrix[r][c] == '.':
        q.append(((r + dr,c + dc), direction))
        continue
    
      for d in directions_map[matrix[r][c]][direction]:
        q.append(((r + d[0], c + d[1]), d))

  bfs((0,0), (0,1))
  energized = sorted(energized)
  return len(energized)

# print("sample input: ", solve(SAMPLE_INPUT))
print("sample input: ", solve(open('sample.txt', 'r').read().strip()))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read().strip()))

