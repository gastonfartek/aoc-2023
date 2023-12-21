from collections import defaultdict
from heapq import heappush, heappop

def solve(input_str: str):
  
  matrix = [list(map(int,list(s))) for s in input_str.splitlines()]
  
  rows_length = len(matrix)
  cols_length = len(matrix[0])

  adjList = defaultdict(list)
  result = {}
  
  for i in range(rows_length):
     for j in range(cols_length):
        if j + 1 < cols_length:
          adjList[(i,j)].append([matrix[i][j+1], (i, j + 1)])
        if i + 1 < rows_length:
          adjList[(i,j)].append([matrix[i+1][j], (i + 1, j)])
        if j - 1 >= 0:
          adjList[(i,j)].append([matrix[i][j-1], (i, j - 1)])
        if i - 1 >= 0:
          adjList[(i,j)].append([matrix[i-1][j], (i - 1, j)])
  
  # result[(0,0)] = 0

  allowed_moves = {
     (0, 1): ((-1, 0), (0,1), (1, 0)),
     (0, -1): ((-1, 0), (0,-1), (1, 0)),
     (1, 0): ((0, -1), (0,1), (1, 0)),
     (-1, 0): ((0, -1), (0,1), (-1, 0))
  }
  
  h = []
  heappush(h, [0, (0,0), ((0,0), 0)])
  seen = set()
  
  while h:
     cost, coords, direction = heappop(h)
     d, count = direction

     if coords == (rows_length - 1, cols_length - 1): 
        return cost
    #  if coords in result and result[coords] < cost:
     if (coords[0], coords[1], d[0], d[1], count) in seen:
        continue
     
     result[coords] = cost
     seen.add((coords[0], coords[1], d[0], d[1], count))

     

     for node in adjList[coords]:
        adj_cost, adj_coords = node
        adj_node_dir = (adj_coords[0] - coords[0], adj_coords[1] - coords[1])

        if adj_node_dir == d:
          if count < 3:
            heappush(h, (cost + adj_cost, adj_coords, (adj_node_dir, count + 1)))

          continue
        
        if d == (0,0) or adj_node_dir in allowed_moves[d]:
          heappush(h, (cost + adj_cost, adj_coords, (adj_node_dir, 1)))

  return 0

SAMPLE_INPUT = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read().strip()))

