from collections import deque

def solve(input_str: str):
    result = 0
    for line in input_str.splitlines():
        nums = [deque(map(int,line.split()))]

        while True:
            
            current = nums[-1]
            length = len(current)
            new_sequence = deque(current[i+1] - current[i] for i in range(length - 1))
            nums.append(new_sequence)

            if all(n == 0 for n in nums[-1]):
                break
            
        nums[-1].appendleft(0)

        for i in range(len(nums) -1 , 0, -1):
            nums[i-1].appendleft(nums[i-1][0] - nums[i][0])

        result += nums[0][0]
    return result


SAMPLE_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

SAMPLE_INPUT_2 = """10 13 16 21 30 45"""

print("sample input 1: ", solve(SAMPLE_INPUT))

print("sample input 2: ", solve(SAMPLE_INPUT_2))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

