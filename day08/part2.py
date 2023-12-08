import math

def solve(input_str: str):

    instructions, lines = input_str.split("\n\n")
    instructions = list(map(int, instructions.replace("L", "0").replace("R","1")))

    m = {}
    n = []
    for line in lines.splitlines():
        a, b = line.split(" = ")
        m[a] = tuple(b.replace("(","").replace(")", "").split(", "))     
        if a[2] == 'A':
            n.append(a)   

    l = len(instructions)
    
    # m_cache = {}
    # for key in m.keys():
    #     i = 0
    #     nn = m[key][0]
    #     while nn[2] != "Z":
    #         nn = m[nn][instructions[i % l]]
    #         i += 1

    #     m_cache[key] = [(nn,i)]
    #     i = 0
    #     nn = m[key][1]
    #     while nn[2] != "Z":
    #         nn = m[nn][instructions[i % l]]
    #         i += 1

    #     m_cache[key].append((nn,i))
    

    # done = False
    # print('cache done')
    # while not done:
        # max_n = 0
        
        # for n_i in range(0,len(n)):

            # while n[n_i][0][2] != "Z":
            # while True:
            #     i = n[n_i][1] 
            #     n[n_i][0] = m[n[n_i][0]][instructions[i % l]]
            #     n[n_i][1] += 1
                
            #     if n[n_i][0][2] == "Z":
            #         break
            # key = n[n_i][0]
            # i = n[n_i][1] 
            # n[n_i][0] = m_cache[key][instructions[i % l]][0]
            # n[n_i][1] += m_cache[key][instructions[i % l]][1]
            
            # max_n = max(max_n, n[n_i][1])
    result = []       
    for n_i in range(0,len(n)):
        # remaining = max_n - n[n_i][1]
        
        # while True:
        #     curr_key = n[n_i][0]
        #     curr_i = n[n_i][1]
        #     next_i = curr_i + 1
        #     next_cache_value = m_cache[curr_key][instructions[next_i % l]]

        #     if next_cache_value[1] + curr_i < remaining:
        #         n[n_i][0] = next_cache_value[0]
        #         n[n_i][1] = curr_i + next_cache_value[1] + 1
        #         remaining = remaining - n[n_i][1]
        #     else:
        #         break
        i = 0
        while n[n_i][2] != 'Z':
            key = n[n_i]
            n[n_i] = m[key][instructions[i % l]]
            i+=1
            
        result.append(i)
        # if is_done(n):
        #         done = True
        #         break
    

    return math.lcm(*result)

  

SAMPLE_INPUT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))