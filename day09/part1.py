def solve(input_str: str):
    result = 0
    for line in input_str.splitlines():
        nums = [list(map(int,line.split()))]

        while True:
            
            current = nums[-1]
            length = len(current)
            new_sequence = []

            for i in range(length - 1):
                new_sequence.append(current[i+1] - current[i])

            nums.append(new_sequence)

            if len(list(filter(lambda x: x != 0, nums[-1]))) == 0:
                break
            
        nums[-1].append(0)

        for n in nums:
            result += n[-1]

    return result


SAMPLE_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

SAMPLE_INPUT_2 = """10 24 34 42 67 169 489 1304 3092 6596 12866 23238 39178 61916 91984 129612 179482 269732 509310 1236682 3367793"""
print("sample input 1: ", solve(SAMPLE_INPUT))

print("sample input 2: ", solve(SAMPLE_INPUT_2))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

