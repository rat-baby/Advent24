lines = []
results = []
order = []
orderLine = []
isSafe = []
final = 0

#retrieve from text file in an array of line strings
with open('resources/day2.txt', 'r') as input:
  lines = input.readlines()

#split array of lines into a multidimentional array of individual number strings
for i,line in enumerate(lines):
  lines[i] = line.split()

#convert all number strings into ints
for row in lines:
  for i,value in enumerate(row):
    row[i] = int(value)


for index, line in enumerate(lines):
  orderLine = []

  #steps through the array creating a new array orderLine for each one
  #adding 1 for if it's decreasing within safe levels, 2 if increasing
  #within safe levels, and 0 if its unsafe
  for x in range(0, len(line) - 1):
    lineItem = 0
    if ((line[x] < line[x + 1]) and (line[x + 1] - line[x] <= 3) and (line[x + 1] - line[x] >= 1)):
       lineItem = 1
    elif ((line[x] > line[x + 1]) and (line[x] - line[x + 1] <= 3) and (line[x] - line[x - 1] >=1)):
      lineItem = 2
    else:
      lineItem = 0
    orderLine.append(lineItem)
  
  order = []
  for i in range (0, len(orderLine) - 1):
    retval = False
    if (orderLine[i] == orderLine[i + 1]):
      retval = True
    order.append(retval)


  if (all(order)):
    isSafe.append(True)
  else:
    isSafe.append(False)
  
  if (index == 2):
    print(lines[2])
    print(orderLine)
    print(order)
    print(isSafe[2])



    
for value in isSafe:
  if value:
    final = final + 1

