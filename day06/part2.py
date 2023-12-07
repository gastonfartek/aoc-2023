from functools import reduce
import operator

def solve(input_str: str):
    temp = input_str.replace("Time: ", "").replace("Distance: ", "").strip().splitlines()
    time = int("".join(list(filter(lambda n: n.isnumeric(), temp[0]))))
    distance = int("".join(list(filter(lambda n: n.isnumeric(), temp[1]))))

    t = time
    d = distance

    found = False
    result = []
    i = 0
    while not found:
      i += 1
      if i * (t - i) > d:
        result.append(i)
        found = True
    

    found = False
    i = t
    while not found:
      i -= 1
      if i * (t - i) > d:
        result.append(i)
        found = True
        
    return result[1] - result[0] + 1


SAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))