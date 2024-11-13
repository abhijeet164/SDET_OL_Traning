# There are two jumping statements break and continue

for i in range(10):
    if i == 5:
        break
    print(i)

print("Break executed successfully")

for j in range(10):
    if j == 5:
        continue
    print(j)
print("continue executed successfully")
