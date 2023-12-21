from collections import defaultdict, deque

def solve(input_str: str):
   lines = input_str.splitlines()

   modules = {}
   low = True
   high = False

   adj_list = defaultdict(list)

   for line in lines:
      name, destinations = line.split(" -> ")
      module_type = name if name == 'broadcaster' else name[0]
      name = name if name == 'broadcaster' else name[1:]
      
      modules[name] = {"destinations": destinations.split(", "), "module_type": module_type }
      
      for n in modules[name]['destinations']:
         adj_list[n].append(name)

      if module_type in ('&', '%'):
         modules[name]['state'] = low
   
   low_pulses = 0
   high_pulses = 0

   i = 0

   while i < 1000:

      signals = deque([(i , low) for i in modules['broadcaster']['destinations']])
      low_pulses += 1

      while signals:
         
         target, signal_type = signals.popleft()
         
         low_pulses += 1 if signal_type == low else 0
         high_pulses += 1 if signal_type == high else 0

         if target not in modules:
            continue
         
         if modules[target]['module_type'] == '&':
            if len(adj_list[target]) > 1:
               all_high = True
               for a in adj_list[target]:
                  if modules[a]['state'] != high:
                     all_high = False
                     break

               new_state = low if all_high else high
            else:
               new_state = not signal_type

            modules[target]['state'] = new_state
            for d in modules[target]['destinations']:
               signals.append((d, new_state))

         if modules[target]['module_type'] == '%' and signal_type != high:
            new_state = not modules[target]['state']
            modules[target]['state'] = new_state
            for d in modules[target]['destinations']:
               signals.append((d, modules[target]['state']))

      i += 1
   

   total = low_pulses * high_pulses
   return total

SAMPLE_INPUT = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read().strip()))

