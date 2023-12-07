data_filepath = "day-01/data.txt"

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

string_digits_rev = [[d[0][::-1], d[1]] for d in string_digits]


def load_data(filepath):
    with open(filepath) as file:
        data = file.read()
    return data.split("\n")


def replace_first_substring(s, match_candidates):
    positions = []

    for m in match_candidates:
        pos = s.find(m[0])
        if pos >= 0:
            # Substring found in array
            positions.append(m + [pos])

    if positions:
        # Return min of positions by third element (position in parent string)
        first_match = min(positions, key=lambda p: p[2])

        # Replace the first occurence with the corresponding digit
        s = s.replace(first_match[0], first_match[1], 1)

    return s


def get_first_digit(s):
    for char in s:
        if char.isdigit():
            return char


# Load data
puzzle = load_data(data_filepath)

# Replace the first string digit
puzzle = [replace_first_substring(s, string_digits) for s in puzzle]

# Reverse all the strings
puzzle = [s[::-1] for s in puzzle]

# Replace all first (reversed) string digits
puzzle = [replace_first_substring(s, string_digits_rev) for s in puzzle]

# Restore original string order
puzzle = [s[::-1] for s in puzzle]

# Extract first and last digits from each string
puzzle = [get_first_digit(s) + get_first_digit(s[::-1]) for s in puzzle]

# Cast to integers
puzzle = [int(s) for s in puzzle]

# Display sum
print(sum(puzzle))
