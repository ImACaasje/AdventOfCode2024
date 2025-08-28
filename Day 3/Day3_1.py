import re
answer = 0

input = open("input.txt").read()
print(input)
pattern = r"mul\((\d+),(\d+)\)"

for a, b in re.findall(pattern, input):
    answer += int(a) * int(b)
print(answer)