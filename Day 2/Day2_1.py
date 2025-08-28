reports = [list(map(int, report.split())) for report in open("input.txt").readlines()]
safe_counter = 0

def req1(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False
    return True
def req2(report):
    for i in range(len(report) - 1):
        if abs(int(report[i]) - int(report[i+1])) not in [num for num in range(1, 4)]:
            return False
    return True

for report in reports:
    if req1(report) and req2(report):
        safe_counter += 1

print(f"Amount of safe reports: {safe_counter}")