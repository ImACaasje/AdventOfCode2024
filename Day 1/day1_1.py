distance = 0
list1 = []
list2 = []

for line in open("input.txt").readlines():
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

for (num1, num2) in zip(sorted(list1), sorted(list2)):
    distance += abs(num1-num2)
print(distance)