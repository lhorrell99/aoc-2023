from collections import Counter
from functools import cmp_to_key

data_filepath = "day-07/data.txt"


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


def get_numeric_value(char):
    """
    Args:
        char (e.g.): "A"
    Returns:
        (e.g.): 14
    """

    map = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    return map[char] if char in map.keys() else int(char)


def get_numeric_hand(hand_string):
    """
    Args:
        hand_string (e.g.): "32T3K"
    Returns:
        (e.g.): [3, 2, 10, 3, 13]
    """

    return [get_numeric_value(char) for char in hand_string]


def get_hand_type(hand):
    """
    Args:
        hand (e.g.): [3, 2, 10, 3, 13]
    Returns:
        the type of hand (lower is stronger)
    """

    hand_types = {
        (5,): 0,
        (1, 4): 1,
        (2, 3): 2,
        (1, 1, 3): 3,
        (1, 2, 2): 4,
        (1, 1, 1, 2): 5,
        (1, 1, 1, 1, 1): 6,
    }

    # Separate joker cards
    hand_no_jokers = list(filter(lambda x: x != 1, hand))
    hand_jokers = list(filter(lambda x: x == 1, hand))

    # Classify hand without jokers
    counts = dict(Counter(hand_no_jokers))
    count_values = sorted(counts.values())

    # Add the jokers to the highest occuring card
    if count_values:
        count_values[-1] += len(hand_jokers)
    else:
        # Edge case "JJJJJ"
        count_values = [len(hand_jokers)]

    # Convert to tuple (enables hashing)
    count_values = tuple(count_values)

    return hand_types[count_values]


def compare_hands(a, b):
    """
    Args:
        a (e.g.): [11, 6, 14, 10, 11]
        b (e.g.): [13, 5, 9, 14, 13]
    Returns:
        the hand with highest value of the first non-equal element
    """

    # a_hand, b_hand = a[2], b[2]
    ab = list(zip(a, b))

    for pair in ab:
        if pair[0] == pair[1]:
            continue

        return 1 if pair[0] < pair[1] else -1


# Load data
base_data = load_data(data_filepath, "\n")

# Split hands and bids
data = [i.split(" ") for i in base_data]

# Add numeric hand representations (and cast bids to integer)
data = [[i[0], int(i[1]), get_numeric_hand(i[0])] for i in data]

# Add types
data = [[*i, get_hand_type(i[2])] for i in data]

# Sort by strength of first non-matching value
data = sorted(data, key=cmp_to_key(lambda a, b: compare_hands(a[2], b[2])))

# Sort by hand types
data = sorted(data, key=lambda x: x[3])

# Reverse (so that index is equal to global rank)
data = reversed(data)

# Add bid * rank
data = [[*j, (i + 1) * j[1]] for i, j in enumerate(data)]

# Display sum (result 250254244)
print(sum([i[4] for i in data]))
