import re

with open("input_test.txt") as f:
    res = 0
    mulDict = {}
    mulPattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in f:
        mulMatches = re.finditer(mulPattern, line)

        for mulMatch in mulMatches:
            num1, num2 = map(int, mulMatch.groups()) 
            i = mulMatch.start()
            dict[(num1, num2)] = i
            
    print(dict)

    print(res)
            
