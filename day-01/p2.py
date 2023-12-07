string_digits = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
    ["nine", "9"],
]

def replace_first_string_digit(s):
    positions = []

    for digit in string_digits:
        pos = s.find(digit[0])
        if pos >= 0:
            positions.append(digit + [pos])

    if positions:
        # Return min of positions by third element
        first_string_digit = min(positions, key=lambda p: p[2])

        # Replace the first occurence with the corresponding digit
        s = s.replace(first_string_digit[0], first_string_digit[1], 1)
        
    return s


def replace_last_string_digit(s):
    # Reverse string
    s = s[::-1]
    
    positions = []
    
    for digit in string_digits:
        pos = s.find(digit[0][::-1])
        if pos >= 0:
            positions.append(digit + [pos])

    if positions:
        # return min of positions by third element
        first_string_digit = min(positions, key=lambda p: p[2])

        # replace the first occurence with the corresponding digit
        s = s.replace(first_string_digit[0][::-1], first_string_digit[1], 1)
        
    return s[::-1]


with open("data.txt") as file:
    puzzle = file.readlines()

# Replace first string digit
puzzle = [replace_first_string_digit(s) for s in puzzle]

# Replace last string digit
puzzle = [replace_last_string_digit(s) for s in puzzle]

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
