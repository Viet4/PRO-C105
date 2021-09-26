import csv
import math

with open ("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]


def Mean(data):
    total = 0
    values = len(data)

    for i in data:
        total+= int(i)
    
    mean = total / values
    return mean

squared = []

for i in data:
    subtract = (int(i) - Mean(data))**2
    squared.append(subtract)

added = 0

for i in squared:
    added+= i

rooted = math.sqrt(added / (len(data) - 1))

print(rooted)
