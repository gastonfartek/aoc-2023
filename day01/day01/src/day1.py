# def input():
with open ("input.txt", "r") as f:
  lines = f.readlines()
  # return lines

def sample_input():
  with open ("sample_input.txt", "r") as f:
    lines = f.readlines()
  return lines

# Part 1


def part1(lines):
  result = 0
  for line in lines:
      
      for char in line:
          if char.isnumeric():
            result += int(char) * 10
            break

      for char in reversed(line):
          if char.isnumeric():
            result += int(char)
            break
  return result

def part2(lines): 
  result = 0
  for line in lines:
      line = line.replace("one", "o1e")
      line = line.replace("two", "t2o")
      line = line.replace("three", "t3h")
      line = line.replace("four", "f4r")
      line = line.replace("five", "f5e")
      line = line.replace("six", "s6x")
      line = line.replace("seven", "s7n")
      line = line.replace("eight", "e8t")
      line = line.replace("nine", "n9e")
      
      for char in line:
          if char.isnumeric():
            result += int(char) * 10
            break

      for char in reversed(line):
          if char.isnumeric():
            result += int(char)
            break
  return result

sample_input_1 =  """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sample_input_2 =  """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

print("Part 1 - sample input (142): ", part1(sample_input_1.split("\n")))
print("Part 1 - input (53080): ", part1(lines))
print("Part 2 - sample input (281): ", part2(sample_input_2.split("\n")))
print("Part 2 - input (53268): ", part2(lines))


