sum = 0
for x in range (1000, 2300):
    if (x%7==0) and (x%5==0):
        continue
    sum += x
print(sum)
