from functools import cache

@cache
def parse_card(card_number: int, card: str):
  card = card.replace("Card " + str(card_number+1)+":", "")
  left,  right = card.split('|') 
  
  left = left[1:len(left)-1]
  right = right + " "
  matches = 0

  i = 0
  while i < len(left):
    search = " "+left[i:i+2]+" "
    if search in right:
      matches += 1
    
    i = i + 3

  return [card_number + 1 + i for i in range(matches)]

def solve(input_str: str):
  cards = input_str.splitlines()
  cards_index = [i for i in range(len(input_str.splitlines()))]


  for i in cards_index:
    new_cards = parse_card(i, cards[i])
    for nc in new_cards:
      cards_index.append(nc)
     
      
  return len(cards_index)



SAMPLE_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))