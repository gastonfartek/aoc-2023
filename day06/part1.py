from functools import reduce
import operator

def solve(input_str: str):
    temp = input_str.replace("Time: ", "").replace("Distance: ", "").strip().splitlines()
    time = list(map(int,filter(lambda n: n.isnumeric(), temp[0].split(" "))))
    distance = list(map(int,filter(lambda n: n.isnumeric(), temp[1].split(" "))))

    counts = []
    for i in range(0, len(time)):
        t = time[i]
        d = distance[i]

        counts.append(0)
        for j in range(1,t):
          # 6 * (7 -6)
          if j * (t - j) > d:
             counts[i] += 1
    
    return reduce(operator.mul, counts)


SAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))