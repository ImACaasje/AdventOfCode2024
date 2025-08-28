reports = [list(map(int, report.split())) for report in open("input.txt").readlines()]
safe_counter = 0

def safe(report):
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False

    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) not in [num for num in range(1, 4)]:
            return False
    return True


for report in reports:
    if safe(report):
        safe_counter += 1
        continue

    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]

        if safe(new_report):
            safe_counter +=1
            break


print(f"Number of safe reports: {safe_counter}")