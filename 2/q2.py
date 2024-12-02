def tooRapidOrNothing(level1, level2):
    diff = abs(level1 - level2)
    return diff < 1 or diff > 3


def isAscending(levels):
    for i in range(1, len(levels)):
        if levels[i] < levels[i - 1] or tooRapidOrNothing(levels[i], levels[i - 1]):
            return False
    return True


def isDescending(levels):
    for i in range(1, len(levels)):
        if levels[i] > levels[i - 1] or tooRapidOrNothing(levels[i], levels[i - 1]):
            return False
    return True


def isSafe(levels):
    return isAscending(levels) or isDescending(levels)


def isTolerable(levels):
    for i in range(len(levels)):
        if isSafe(levels[:i] + levels[i + 1 :]):
            return True
    return False


safeCounter = 0
with open("input.txt") as f:
    reports = f.readlines()
    for report in reports:
        # split by space and cast to int
        levels = [int(level) for level in report.split()]

        if isSafe(levels) or isTolerable(levels):
            safeCounter += 1

print(safeCounter)
