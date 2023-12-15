import copy
def solve(input_str: str):
  
  def run(matrix):
    m = copy.deepcopy(matrix)

    for i in range(len(m[0])):
        add = 0
        for r_i in range(len(m)):
            col = m[r_i][i]
        
            if col == 'O':
                if add > 0:
                    m[r_i-add][i] = 'O'
                    m[r_i][i] = '.'
                
            if col == ".":
                add += 1

            if col == '#':
                add = 0
    

    for r_i, row in enumerate(m):
        add = 0
        for i, col in enumerate(row):
            if col == 'O':
                if add > 0:
                    m[r_i][i-add] = 'O'
                    m[r_i][i] = '.'
                
            if col == ".":
                add += 1

            if col == '#':
                add = 0

    for i in range(len(m[0]) -1, -1, -1):
        add = 0
        for r_i in range(len(m) -1, -1, -1):
            col = m[r_i][i]
        
            if col == 'O':
                if add > 0:
                    m[r_i+add][i] = 'O'
                    m[r_i][i] = '.'
                
            if col == ".":
                add += 1

            if col == '#':
                add = 0

    for r_i in range(len(m) -1, -1, -1):
        add = 0
        row = m[r_i]
        for i in range(len(row) -1, -1, -1):
            col = row[i]
            if col == 'O':
                if add > 0:
                    m[r_i][i+add] = 'O'
                    m[r_i][i] = '.'
                
            if col == ".":
                add += 1

            if col == '#':
                add = 0
    
    return m
  
  m = [list(r) for r in input_str.splitlines()]
  keys = []
  runs = []
  remaining_runs = 1000000000
  while True:
    new_m = run(m)
    remaining_runs -= 1
    key_new_m = "".join(["".join(a) for a in new_m])

    if key_new_m in keys:
        runs = runs[keys.index(key_new_m):]
        break

    runs.append(new_m)    
    keys.append(key_new_m)
    m = new_m

  index = (remaining_runs % len(runs))
  length = len(runs[index])

#   total = 0
#   for i, row in enumerate(runs[index]):
#       for c in row:
#           if c == 'O':
#               total += length - i
  
  total = sum(length - i for i, row in enumerate(runs[index]) for c in row if c == 'O')

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

