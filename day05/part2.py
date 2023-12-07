from collections import defaultdict
from functools import cache


def overlap(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return end1 >= start2 and end2 >= start1

def solve(input_str: str):
  
  data = input_str.split('\n\n')
  seeds_input = list(map(int, data[0].replace("seeds: ", "").split(" ")))

  seeds = []

  for i in range(0, len(seeds_input), 2):
    #  seeds.append((seeds_input[i], seeds_input[i+1]))
     seeds.append((seeds_input[i], seeds_input[i] + seeds_input[i+1]))

  destination_map = []

  # new_seeds = set()
  # while len(seeds) > 0:
  #    seed_length = seeds.pop()
  #    seed_start = seeds.pop()
  #    seed_end = seed_start + seed_length
  #    for i in range(seed_start, seed_end):
  #       new_seeds.add(i)


  # 1- loop thorugh each destination
  # 2 - at the start of each destination there is 
  #     a set of seed ranges and we need to
  #     compute a new set of ranges based on the
  #     overlaping source/dest range
  # 3 - store overlapping ranges (updated with dist) on a new array
  # 4 - re-append non-overlapping ranges (left and right) to the same seeds array
  #     so they can be computed or added to the the new array
  # 5 - after we looped through all the seed ranges re-set seeds array to the new array

  #[(57, 13), (81, 14)], [(57, 13), (81, 14)]
  for destination in data[1:]:
    lines = destination.splitlines()
    
    updated = []
    while len(seeds) > 0:  

      # seed_start, seed_range_length = seeds.pop()
      # seed_end = seed_start + seed_range_length
      seed_start, seed_end = seeds.pop()

      found = False
      for line in lines[1:]:
        dest, source, range_length = list(map(int,line.split(" ")))
        
        if overlap(seed_start, seed_end, source, source + range_length):
          # n = dest - source
          # new_range = (max(seed_start, source) + n, min(seed_end, source + range_length) + n)
          l = max(seed_start, source)
          r = min(seed_end, source + range_length)
          # v = source + dest
          new_range = (l - source + dest, r - source + dest)

          if not r > l:
            continue
          # new_range = (l, r - l)
          # new_range = (max(seed_start, source) - source + dest, min(seed_end, source + range_length) - source + dest)
          updated.append(new_range)

          #range to the left
          if seed_start < source:
            # seeds.append((seed_start, source - 1))
            seeds.append((seed_start, l))

          #range to the right
          if seed_end > source + range_length:
            # seeds.append((source + range_length + 1, seed_end))
            seeds.append((source + range_length, seed_end))

          found = True
          break
      
      #if no matching range found
      if not found:
        # updated.append((seed_start, seed_end))
        updated.append((seed_start, seed_end))

    seeds = updated


  return min(seeds)



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