from collections import defaultdict

def solve(input_str: str):
  workflows_input, ratings_input = input_str.split("\n\n")
  
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

  ratings = []

  for r in ratings_input.splitlines():
    rating = {}
    r = r.replace('{',"").replace('}', "")

    for v in r.split(','):
      rating[v[0]] = int(v[2:])
    
    ratings.append(rating)

  

  total = 0
  
  for rating in ratings:
    


    key = 'in'
    
    while True:

      if key in ("A", "R"):
        total += sum(rating.values()) if key == "A" else 0
        break

      workflow = workflows[key]

      for workflow_values in workflow:
        
        if len(workflow_values) == 1:
          key = workflow_values[0]
          break

        rating_value = rating[workflow_values[0]]
        sign = workflow_values[1]
        value = workflow_values[2]
        destination = workflow_values[3]
        match = rating_value < value if sign == "<" else rating_value > value

        if match:
          key = destination
          break
         
         
         

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

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read().strip()))

      