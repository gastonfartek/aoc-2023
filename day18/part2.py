from collections import defaultdict
from heapq import heappush, heappop

def solve(input_str: str):
  
  dig_plan = [[line.split()[-1][-2], int(line.split()[-1][2:-2], 16)] for line in input_str.splitlines()]
  
  edges = [[0,0]]

  orientation = {
     '2': (0, -1),
     '0': (0, 1),
     '3': (-1, 0),
     '1': (1 , 0),
  }
  
  current = [0,0]
  perimeter = 0
  for move in dig_plan:
     o, amount = move
     amount = int(amount)
     current[0] += orientation[o][0] * amount
     current[1] += orientation[o][1] * amount
     perimeter += amount
     edges.append(current.copy())
  

  area = 0

  for i in range(len(edges)):
     a = i - 1
     b = (i + 1) % len(edges)
    #  b = 0 if b == len(edges) else b
     area += edges[i][0] * (edges[a][1] - edges[b][1])

  area = abs(area) // 2

  total = perimeter + (area - perimeter // 2 + 1)


  return total

SAMPLE_INPUT = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read().strip()))

