import re
answer = 0
enabled = True

input = open("input.txt").read()

pattern = r"mul\((\d+),(\d+)\)"
pattern2 = r"(do\(\))|(don\'t\(\))"


def search(string):
    global enabled, answer

    match2 = re.search(pattern2, string)
    match1 = re.search(pattern, string)
    if match2 and match1:
        if match2.span()[1] < match1.span()[1]:
            match match2.group():
                case "don't()":
                    enabled = False
                case "do()":
                    enabled = True
            search(string[match2.span()[1]:])
        elif match1.span()[1] < match2.span()[1]:
            if enabled:
                a, b = re.findall(pattern, string)[0]
                answer += int(a) * int(b)
            search(string[match1.span()[1]:])
    elif match1:
        if enabled:
            a, b = re.findall(pattern, string)[0]
            answer += int(a) * int(b)
        search(string[match1.span()[1]:])
    else:
        return

search(input)
print(f"The answer is: {answer}")