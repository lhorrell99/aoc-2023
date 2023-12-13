data_filepath = "day-04/data.txt"


def load_data(filepath, split_delimiter):
    """
    Args:
        filepath (e.g.): "day-00/data.txt"
        split_delimiter (e.g.): "\n"
    Returns:
        list of entries, split on specified delimiter
    """

    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def count_matches(i, c_data):
    """
    Args:
        i: index to evaluate
        card_data (e.g.): ({"6", "31", "83"}, {"83", "17", "48"})
    Returns:
        the value of the card
    """

    count = len(c_data[0] & c_data[1])

    if count:
        return 2 ** (count - 1)

    return 0


# Load data
puzzle = load_data(data_filepath, "\n")

# Remove card numbers
puzzle = [i.split(": ")[1] for i in puzzle]

# Separate winning and candidate numbers
puzzle = [i.split("| ") for i in puzzle]

# Extract winning and candidate values and add to sets
win_vals = [set(i[0].split()) for i in puzzle]
can_vals = [set(i[1].split()) for i in puzzle]

# Zip list
card_data = list(zip(can_vals, win_vals))

# Calculate all card values
card_values = [count_matches(i, c) for i, c in enumerate(card_data)]

# Display sum (result 20117)
print(sum(card_values))
