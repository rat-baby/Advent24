list1 = []
list2 = []
line = []
counts = []
finalList = []
answer = 0

with open('resources/day1.txt', 'r') as input:
  lines = input.readlines()

for i, text in enumerate(lines):
  line = lines[i].split()
  list1.append(line[0])
  list2.append(line[1])

list1.sort()
list2.sort()

for i,value1 in enumerate(list1):
  count = 0
  for value2 in list2:
    if value1 == value2:
      count = count + 1
  counts.append(count)

for i,value1 in enumerate(list1):
  count = value1 * counts[i]
  finalList.append(count)

for i,value in enumerate(finalList):
  finalList[i] = int(value or 0)

  answer = answer + finalList[i]


print(answer)

