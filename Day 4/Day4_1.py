import re

search = "XMAS"
matches = 0

data = open("test_input.txt")
lines = [list(line) for line in data.readlines()]
print(lines)

def find(char, start):
    global matches

    line = start[0]
    char_index = start[1]
    character = search[char]
    match = 0

    if line != 0 and line != len(lines):
        # Check line above
        for i in range(char_index-1, char_index+2):
            if lines[line-1][i] == character:
                if character == search[len(search)-1]:
                    matches += 1
                    return match
                else:
                    find(char+1, (line-1, i))





for i, line in enumerate(lines):
    results = [i for i, x in enumerate(line) if x==search[0]]
    #print(results)
    for result in results:
        if i >= 4:
            # Check Above
            sigmaboy123 = [i for i, x in enumerate(lines[i-1]) if x==search[1]]
            for index in sigmaboy123:
                dir = index - i
                if abs(dir) <= 1:
                    if lines[i-2][index+dir] == search[2] and lines[i-3][index+2*dir]:
                        matches +=1
                        print(f"W in: {result} {dir} line: {line}")



print(matches)



XMAS_count = 0


