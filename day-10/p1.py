import sys

# Increase recursion limit
sys.setrecursionlimit(100000)

data_filepath = "day-10/data.txt"


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


def recurse(a, b, count, map, pipes):
    """
    Args:
        a (e.g.): ("S", 6956)
        b (e.g.): ("W", 6956)
        count: 0
        map: the flattened map
    Returns:
        the number of steps to the furthest location from the start point
    """

    # Base case - indexes aligned and not 1
    if a[1] == b[1] and count:
        return count

    # Find new locations in map
    next_a_loc = a[1] + deltas[a[0]]
    next_b_loc = b[1] + deltas[b[0]]

    # Find next directions
    next_a = (pipes[map[next_a_loc]][a[0]], next_a_loc)
    next_b = (pipes[map[next_b_loc]][b[0]], next_b_loc)

    return recurse(next_a, next_b, count + 1, map, pipes)


# Load data
base_data = load_data(data_filepath, "\n")
row_len = len(base_data[0])

# Flatten
map = "".join(base_data)

# Define index deltas for flattened map
deltas = {
    "N": -row_len,
    "E": 1,
    "S": row_len,
    "W": -1,
}

# Define from-to pairings for all pipe shapes
pipes = {
    "|": {"N": "N", "S": "S"},
    "-": {"E": "E", "W": "W"},
    "L": {"S": "E", "W": "N"},
    "J": {"E": "N", "S": "W"},
    "7": {"N": "W", "E": "S"},
    "F": {"N": "E", "W": "S"},
    ".": {},
}

# Find start index and starting directions
s_loc = map.index("S")
s_a, s_b = [(d, s_loc) for d in deltas.keys() if d in pipes[map[s_loc + deltas[d]]]]

# Calculate and display furthest location from start point (result 7066)
print(recurse(s_a, s_b, 0, map, pipes))
