import re
import itertools

with open("input.txt") as f:
    res = 0
    
    mulPattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    doPattern = r"do\(\)"
    dontPattern = r"don't\(\)"
    toggle = True
    for line in f:
        orderedMatches = []
        matches = itertools.chain(re.finditer(mulPattern, line), re.finditer(doPattern, line), re.finditer(dontPattern, line))        
        for match in matches:
            orderedMatches.append((match.start(), match))
        orderedMatches.sort(key=lambda x: x[0])
        
        for match in orderedMatches:
            if match[1].group(0) == "do()":
                toggle = True
            elif match[1].group(0) == "don't()":
                toggle = False
            else:
                num1, num2 = int(match[1].group(1)), int(match[1].group(2))
                if toggle:
                    res += num1 * num2
                    
    print(res)
