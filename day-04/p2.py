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


def count_cards(i, c_data, card_counts):
    """
    Args:
        i: index to evaluate
        c_data (e.g.): ({"6", "31", "83"}, {"83", "17", "48"})
        card_counts (e.g.): [1, 1, 1, 1]
    """
    # retrieve number of cards
    card_count = card_counts[i]

    # calculate number of matches
    count = len(c_data[0] & c_data[1])

    for j in range(count):
        card_counts[i + (j + 1)] += card_count


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

# Add initial card counts to card_data
card_counts = [1 for i in card_data]

# Iterate through and count cards
for i, c_data in enumerate(card_data):
    count_cards(i, c_data, card_counts)

# Display sum (result 13768818)
print(sum(card_counts))
