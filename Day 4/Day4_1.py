import re

data = open("test_input.txt")
XMAS_count = 0

def horizontal_check():
    count = 0
    lines = data.readlines()
    for line in lines:
        print(re.findall(r'XMAS|SAMX', line))
        count += len(re.findall(r'XMAS', line))
    return count

XMAS_count += horizontal_check()
print(XMAS_count)