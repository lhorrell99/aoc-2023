data_filepath = "day-01/data.txt"

string_digit_replacements = [
    ["one", "o1e"],
    ["two", "t2o"],
    ["three", "t3e"],
    ["four", "f4r"],
    ["five", "f5e"],
    ["six", "s6x"],
    ["seven", "s7n"],
    ["eight", "e8t"],
    ["nine", "n9e"],
]


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def replace_substrings(s, candidates):
    for c in candidates:
        s = s.replace(c[0], c[1])
    return s


def get_first_digit(s):
    for char in s:
        if char.isdigit():
            return char


# Load data
puzzle = load_data(data_filepath, "\n")

# Replace substrings
puzzle = [replace_substrings(s, string_digit_replacements) for s in puzzle]

# Extract first and last digits from each string
puzzle = [get_first_digit(s) + get_first_digit(s[::-1]) for s in puzzle]

# Cast to integers
puzzle = [int(s) for s in puzzle]

# Display sum (result 55652)
print(sum(puzzle))
