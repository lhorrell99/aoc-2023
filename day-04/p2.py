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


def count_cards(i, can_vals, win_vals, card_counts):
    """
    Args:
        i: index to evaluate
        can_vals: array of candidate values for all cards
        win_vals: array of winning values for all cards
        card_counts: array storing number of copies of each card
    """
    # retrieve number of cards
    card_count = card_counts[i]

    # calculate number of matches
    count = len(can_vals[i] & win_vals[i])

    for j in range(count):
        card_counts[i + (j + 1)] += card_count

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

# Init a card_counts array
card_counts = [1 for i in win_vals]

# Iterate through and count cards
for i in range(len(win_vals)):
    count_cards(i, can_vals, win_vals, card_counts)

# Display sum (result 13768818)
print(sum(card_counts))
