lines = []
results = []
safetyBools = []
safetyValues = []
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

def safetyCheck(line):
  for x in range(0, len(line) - 1):
    lineItem = 0
    if ((line[x] < line[x + 1]) and (abs(line[x + 1] - line[x]) <= 3) and (abs(line[x + 1] - line[x]) >= 1)):
       lineItem = 1
    elif ((line[x] > line[x + 1]) and (abs(line[x] - line[x + 1]) <= 3) and (abs(line[x] - line[x - 1]) >=1)):
      lineItem = 2
    else:
      lineItem = 0
    safetyValues.append(lineItem)

for index, line in enumerate(lines):
  safetyValues = []

  #steps through the array creating a new array orderLine for each one
  #adding 1 for if it's decreasing within safe levels, 2 if increasing
  #within safe levels, and 0 if its unsafe
  safetyCheck(line)
  
  #for each list of 0, 1, or 2, go through and check if the numbers are all equal
  safetyBools = []
  for i in range (0, len(safetyValues) - 1):
    retval = False
    if (safetyValues[i] == safetyValues[i + 1]):
      retval = True
    safetyBools.append(retval)


  #if all values are equal, commit a value of true in a new array for that line
  if (all(safetyBools)):
    isSafe.append(True)
  else:
    isSafe.append(False)



#add all true values together
for value in isSafe:
  if value:
    final = final + 1

print(final)
