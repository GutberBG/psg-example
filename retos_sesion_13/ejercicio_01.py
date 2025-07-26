lucas = [2, 1]
for i in range(2, 20):
    lucas.append(lucas[i-1] + lucas[i-2])
print(lucas)