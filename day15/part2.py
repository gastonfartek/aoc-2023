from collections import defaultdict, deque

def solve(input_str: str):
  
  def hash(step):

    current_value = 0
    for s in step:
        current_value = ((ord(s) + current_value) * 17) % 256

    return current_value
  
  boxes_order = defaultdict(list)
  boxes_focal_length_values = defaultdict(dict)
  for step in input_str.split(','):
     
     if "-" in step:
        op = step[:-1]
        box_number = hash(list(op))
        if op not in boxes_order[box_number]:
           continue
        
        index = boxes_order[box_number].index(op)
        del boxes_order[box_number][index]
        del boxes_focal_length_values[box_number][op]

     if "=" in step:
        op, focal_length = step.split('=') 
        box_number = hash(op)
        boxes_focal_length_values[box_number][op] = focal_length

        if op not in boxes_order[box_number]:
           boxes_order[box_number].append(op)
    
  total = 0
  for box_number in boxes_order.keys():
    for slot_number, lens in enumerate(boxes_order[box_number]):
      total += (1 + int(box_number)) * (slot_number + 1) * int(boxes_focal_length_values[box_number][lens])

  return total

  
   
SAMPLE_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


