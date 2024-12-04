lines = []
results = []
order = []
orderLine = []

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


# for line in lines:
#   for x in range(len(line) - 1):
#     if (line[x] > line[x + 1] & (line[x + 1] - line[x] <= 3) & (line[x+1] - line[x] >= 1)):
#       orderLine.append(True)
#     else:
#       orderLine.append(False)
    
#single line, only if increasing
line = lines[1]
for x in range(0, len(line) - 1):
     if ((line[x] < line[x + 1]) and (line[x + 1] - line[x] <= 3) and (line[x + 1] - line[x] >= 1)):
       orderLine.append(True)
     else:
       orderLine.append(False)
    
print(line)
print(orderLine)