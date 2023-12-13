data_filepath = "day-01/data.txt"


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def get_first_digit(s):
    for char in s:
        if char.isdigit():
            return char


# Load data
puzzle = load_data(data_filepath, "\n")

# Extract first and last digits from each string
puzzle = [get_first_digit(s) + get_first_digit(s[::-1]) for s in puzzle]

# Cast to integers
puzzle = [int(s) for s in puzzle]

# Display sum (result 56108)
print(sum(puzzle))
