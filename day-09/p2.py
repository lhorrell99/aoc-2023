from functools import reduce

data_filepath = "day-09/data.txt"


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


def get_differences(seq):
    """
    Args:
        seq (e.g.): [0, 3, 6, 9, 12, 15]
    Returns:
        (e.g.): [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
    """

    if not sum(seq):
        return [seq]

    # Calculate differences
    diffs = [y - x for x, y in zip(seq, seq[1:])]

    # Recurse
    return [seq] + get_differences(diffs)


# Load data
base_data = load_data(data_filepath, "\n")

# Retrieve sequences and cast to integers
sequences = [[int(j) for j in i.split(" ")] for i in base_data]

# Get differences
sequences = [get_differences(s) for s in sequences]

# Reverse nested arrays
sequences = [list(reversed(s)) for s in sequences]

# Extract first elements
sequences = [[i[0] for i in s] for s in sequences]

# Reduce to calculate previous element
sequences = [reduce(lambda x, y: -(x - y), s) for s in sequences]

# Display sum (result 1100)
print(sum(sequences))
