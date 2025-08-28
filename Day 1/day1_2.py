similarity = 0
list1 = []
list2 = []

for line in open("input.txt").readlines():
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

for num in list1:
    similarity += num * list2.count(num)
print(similarity)