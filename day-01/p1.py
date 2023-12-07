with open("data.txt") as file:
    puzzle = file.readlines()

puzzle_int_vals = []

for row in puzzle:
    int_vals = []
    for v in row:
        try:
            int_vals.append(int(v))
        except ValueError:
            continue
    puzzle_int_vals.append(int_vals)

sum = 0
for row in puzzle_int_vals:
    sum += int(str(row[0])+str(row[-1]))

print("sum:", sum)