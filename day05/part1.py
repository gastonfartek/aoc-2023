from collections import defaultdict

def solve(input_str: str):
  
  data = input_str.split('\n\n')
  seeds = list(map(int, data[0].replace("seeds: ", "").split(" ")))

  destination_map = []

  for destination in data[1:]:
     lines = destination.splitlines()
     key = lines[0]
     values = []
     for line in lines[1:]:
        values.append(list(map(int,line.split(" "))))

    #  values.sort(key= lambda v: v[1])
     destination_map.append(values)

  source_index = 1
  destination_index = 0
  range_index = 2
  min_value = float('inf')
  
  for seed_value in seeds:
    mapped_value = seed_value

    for maps in destination_map:
      for m in maps:
        if m[source_index] < mapped_value and m[source_index] + m[range_index] > mapped_value:
            mapped_value = mapped_value - m[source_index] + m[destination_index]
            break
    
    min_value = min(min_value, mapped_value)

  return min_value


# 50 98 2
# 52 50 48

# 79 -> 81



# if source <= value and source + range > value
# mapped_value = value - source + destination



  print(data)

SAMPLE_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))