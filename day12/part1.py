def solve(input_str: str):

  def calculate(springs, groups):

    if len(springs) == 0:
      return 1 if len(groups) == 0 else 0
    
    if len(groups) == 0:
      return 0 if '#' in springs else 1

    total = 0
    
    if springs[0] == '.':
      total += calculate(springs[1:], groups)

    if springs[0] == '?':
      total += calculate("." + springs[1:], groups)
      total += calculate("#" + springs[1:], groups)
    
    if springs[0] == '#':
      if groups[0] <= len(springs) and "." not in springs[:groups[0]] and (groups[0] == len(springs) or springs[groups[0]] != '#'):
        total += calculate(springs[groups[0] + 1:], groups[1:])

    return total


  total = 0

  for line in input_str.splitlines():
    springs, groups  = line.split()
    groups = list([int(n) for n in groups.split(",")])

    value = calculate(springs, groups)
    total += value

  
  return total


SAMPLE_INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

