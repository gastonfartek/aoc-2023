def solve(input_str: str):
  steps = [list(step) for step in input_str.split(',')]

  total = 0
  for step in steps:
    current_value = 0
    for s in step:
      current_value = ((ord(s) + current_value) * 17) % 256

    total += current_value

  return total

SAMPLE_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))

