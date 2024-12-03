import re

with open("input.txt") as f:
    res = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in f:
        matches = re.findall(pattern, line)

        for match in matches:
            num1, num2 = int(match[0]), int(match[1])
            res += num1 * num2

    print(res)
            
