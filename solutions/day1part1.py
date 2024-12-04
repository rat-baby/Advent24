list1 = []
list2 = []
line = []
differences = []

with open('resources/day1.txt', 'r') as input:
  lines = input.readlines()

for i, text in enumerate(lines):
  line = lines[i].split()
  list1.append(line[0])
  list2.append(line[1])

list1.sort()
list2.sort()

for i, text in enumerate(list1):
  value1 = int(text)
  value2 = int(list2[i])
  differences.append(abs(value1 - value2))

print(sum(differences))