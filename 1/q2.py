col1, col2 = [], []

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums = line.split()
        col1.append(int(nums[0]))
        col2.append(int(nums[1]))

col2Map = {}
for i in range(len(col2)):
    col2Map[col2[i]] = 1 + col2Map.get(col2[i], 0)

similarityScore = 0
for i in range(len(col1)):
    similarityScore += col1[i] * col2Map.get(col1[i], 0)

print(similarityScore)