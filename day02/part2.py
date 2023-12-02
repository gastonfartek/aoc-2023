import re

def solve(input_str: str):

  result = 0

  for i, line in enumerate(input_str.splitlines()):

    n = {'red': 0, 'green': 0, 'blue': 0}

    line = line.replace("Game "+str(i+1)+":", "")
    matches = re.findall(r'(\d+)\s+(\w+)(?=,|\s*;|$)', line)

    for num, color in  matches:
      n[color] = max(n[color],  int(num))
        

    result += n['red'] * n['green'] * n["blue"]
    

  return result



SAMPLE_IMPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

print("sample input: ", solve(SAMPLE_IMPUT))

with open("input.txt", "r") as input_file:
    # Reading from a file
    print("input: ", solve(input_file.read()))