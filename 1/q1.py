
col1, col2 = [], []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        nums = line.split()
        col1.append(int(nums[0]))
        col2.append(int(nums[1]))

col1.sort()
col2.sort()

sum = 0
for i in range(len(col1)):
    sum += abs(col1[i] - col2[i])
    
print(f"Sum of differences: {sum}")