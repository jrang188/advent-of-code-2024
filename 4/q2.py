slices = [
    ((0, 0), (0, 2), (1, 1), (2, 0), (2, 2)), 
]

variants = ["MSAMS", "MMASS", "SSAMM", "SMASM"]

def counter(matrix, slices, variants):
    count = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            for slice in slices:
                word = "".join(
                    [
                        matrix[y + dy][x + dx]
                        for dy, dx in slice
                        if 0 <= (y + dy) < len(matrix)
                        and 0 <= (x + dx) < len(matrix[0])
                    ]
                )
                if word in variants:
                    count += 1

    print(count)


with open("input.txt") as f:
    matrix = []
    for line in f:
        matrix.append([c for c in line.strip()])

    counter(matrix, slices, variants)
