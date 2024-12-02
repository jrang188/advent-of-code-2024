def tooRapid(level1, level2):
    diff = abs(level1 - level2)
    return diff > 3

def noChange(level1, level2):
    diff = abs(level1 - level2)
    return diff < 1


def isAscending(levels):
    incidentCounter = 0
    for i in range(1, len(levels)):
        if levels[i] < levels[i - 1] or noChange(levels[i], levels[i - 1]):
            incidentCounter += 1
        if tooRapid(levels[i], levels[i - 1]):
            return False
    return incidentCounter < 2


def isDescending(levels):
    incidentCounter = 0
    for i in range(1, len(levels)):
        if levels[i] > levels[i - 1] or noChange(levels[i], levels[i - 1]):
            incidentCounter += 1
        if tooRapid(levels[i], levels[i - 1]):
            return False
    return incidentCounter < 2


safeCounter = 0
with open("input_test.txt") as f:
    reports = f.readlines()
    for report in reports:
        # split by space and cast to int
        levels = [int(level) for level in report.split()]

        if isAscending(levels) or isDescending(levels):
            print(levels)
            safeCounter += 1

print(safeCounter)
