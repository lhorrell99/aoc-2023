data_filepath = "day-04/data.txt"


def load_data(filepath):
    """
    Args:
        filepath (e.g.): "day-02/data.txt"
    Returns:
        list of entries, split on newlines
    """

    with open(filepath) as file:
        data = file.read()

    return data.split("\n")


def count_matches(i, can_vals, win_vals):
    """
    Args:
        i: index to evaluate
        can_vals: array of candidate values for all cards
        win_vals: array of winning values for all cards
    Returns:
        the value of the card
    """

    count = len(can_vals[i] & win_vals[i])

    if count:
        return 2 ** (count - 1)

    return 0


puzzle = load_data(data_filepath)

# Remove card numbers
puzzle = [i.split(": ")[1] for i in puzzle]

# Separate winning and candidate numbers
puzzle = [i.split("| ") for i in puzzle]

# Extract winning and candidate values
win_vals = [i[0].split(" ") for i in puzzle]
can_vals = [i[1].split(" ") for i in puzzle]

# Filter empty strings and add to sets
win_vals = [set(filter(None, i)) for i in win_vals]
can_vals = [set(filter(None, i)) for i in can_vals]

# Calculate all card values
card_values = [count_matches(i, can_vals, win_vals) for i in range(len(win_vals))]

# Display sum
print(sum(card_values))
