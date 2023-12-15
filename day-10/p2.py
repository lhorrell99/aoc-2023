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


def pad(target, char):
    """
    Args:
        target: 2 dimensional list
        char: padding character
    Returns:
        list padded with the specified character
    """

    r_len = len(target[0])
    target.insert(0, char * r_len)
    target.append(char * r_len)
    target = [char + i + char for i in target]

    return target


def recurse_label_loop(a, b, count, map, pipes, deltas):
    """
    Args:
        a (e.g.): ("S", 6956)
        b (e.g.): ("W", 6956)
        count: 0
        map: the flattened map
        pipes: the pipes dictionary
        deltas: the search deltas dictionary
    Returns:
        the number of steps to the furthest location from the start point
    """

    # Base case - indexes aligned and not 1
    if a[1] == b[1] and count:
        return map

    # Replace pipe locations in map with "1"
    map[a[1]] = "1"
    map[b[1]] = "1"

    # Find new locations in map
    next_a_loc = a[1] + deltas[a[0]]
    next_b_loc = b[1] + deltas[b[0]]

    # Find next directions
    next_a = (pipes[map[next_a_loc]][a[0]], next_a_loc)
    next_b = (pipes[map[next_b_loc]][b[0]], next_b_loc)

    return recurse_label_loop(next_a, next_b, count + 1, map, pipes, deltas)


def recurse_label_exterior(s, search_queue, map, deltas):
    """
    Args:
        s (e.g.): ("0", 10)
        search_queue: [('0', 11), ('0', 20)]
        map: the flattened map
        pipes: the pipes dictionary
        deltas: the search deltas dictionary
    Returns:
        the map with all regions outside the exterior of the loop labelled
    """

    # Mark current location
    map[s[1]] = "*"

    # Find neighbours of current location
    neighbours = [(map[s[1] + deltas[d]], s[1] + deltas[d]) for d in deltas.keys()]

    # Remove any non-zero neighbours (either map edges or part of loop)
    neighbours = list(filter(lambda x: x[0] == "0", neighbours))

    # Add to search queue
    search_queue = search_queue + neighbours

    # Base case: no more zeros reachable
    if not search_queue:
        return map

    # Recurse through queue
    next_loc = search_queue.pop()

    return recurse_label_exterior(next_loc, search_queue, map, deltas)


# Load data
base_data = load_data(data_filepath, "\n")

# Pad list (ensures there is one continuous region outside loop)
base_data = pad(base_data, ".")

# Pad again with edge markers
base_data = pad(base_data, "#")

# Get row_len
row_len = len(base_data[0])

# Flatten and assign to list
map = list("".join(base_data))

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

# Find start index and starting directions (and mark pipe start with "1")
s_loc = map.index("S")
s_a, s_b = [(d, s_loc) for d in deltas.keys() if d in pipes[map[s_loc + deltas[d]]]]
map[s_loc] = "1"

# Mark pipe location on map with "1"
map = recurse_label_loop(s_a, s_b, 0, map, pipes, deltas)

# Initially assume all non-pipe locations are inside the loop (while preserving edge padding)
map = ["1" if i == "1" else "#" if i == "#" else "0" for i in map]

# Recursively search map for region outside the loop
s_c = ("0", map.index("0"))
map = recurse_label_exterior(s_c, [], map, deltas)

# Region inside in the loop is labelled with remaining "0" characters
print(len(list(filter(lambda x: x=="0", map))))
