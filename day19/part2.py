from collections import defaultdict, deque

def solve(input_str: str):
  workflows_input = input_str.split("\n\n")[0]
  
  workflows = defaultdict(list)
  
  for line in workflows_input.splitlines():
    name, values = line.split('{')

    values = values.replace('}', '')

    for value in values.split(','):
      if ':' not in value:
        workflows[name].append([value])
        continue

      c = '<' if '<' in value else '>'
      l, r = value.split(c)
      r, d = r.split(":")
      workflows[name].append((l, c, int(r), d))

  ratings = deque()

  ratings.append(({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in'))

  total = 0
  
  while ratings:
    
    rating, key = ratings.popleft()
    
    while True:

      if key in ("A", "R"):
        if key == "A":
         x = rating['x'][1] - rating['x'][0] 
         m = rating['m'][1] - rating['m'][0] 
         a = rating['a'][1] - rating['a'][0] 
         s = rating['s'][1] - rating['s'][0] 
         total += (x * m * a * s)
         
        break

      workflow = workflows[key]

      for workflow_values in workflow:
        
        if len(workflow_values) == 1:
          key = workflow_values[0]
          ratings.append((rating, key))
          break

        k = workflow_values[0]
        rating_value = rating[workflow_values[0]]
        sign = workflow_values[1]
        value = workflow_values[2]
        destination = workflow_values[3]

        if sign == "<" and rating_value[0] < value:
            if rating_value[1] < value:
              ratings.append((rating, destination))
              break
            
            new_r = {'x': list(rating['x']), 'm': list(rating['m']), 'a': list(rating['a']), 's': list(rating['s'])}
            new_r[k][1] = value - 1
            rating[k][0] = value

            if new_r[k][0] <= new_r[k][1]:
               ratings.append((new_r, destination))
            # ratings.append((rating, key))

        if sign == ">" and rating_value[1] > value:
            if rating_value[0] > value:
              ratings.append((rating, destination))
              break
         
            new_r = {'x': list(rating['x']), 'm': list(rating['m']), 'a': list(rating['a']), 's': list(rating['s'])}
            new_r[workflow_values[0]][0] = value + 1
            rating[workflow_values[0]][1] = value
            ratings.append((new_r, destination))
               # ratings.append((rating, key))

  return total

SAMPLE_INPUT = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

print("sample input: ", solve(SAMPLE_INPUT))

# with open("input.txt", "r") as input_file:
#     print("input: ", solve(input_file.read().strip()))

      