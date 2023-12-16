import sys

# Increase recursion limit
sys.setrecursionlimit(100000)

data_filepath = "day-10/data.txt"

# Define index deltas for each direction
deltas = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
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


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def get_matching_keys(val, search_dict):
    keys = [k for k, v in search_dict.items() if v == val]
    return keys


def get_start_dirs(d, start_loc, p_dict, d_dict, map_dict):
    new_loc = (start_loc[0] + d_dict[d][0], start_loc[1] + d_dict[d][1])
    return True if d in p_dict[map_dict[new_loc]] else False


def recurse(a, b, count, p_dict, d_dict, map_dict):
    # Base case - indexes aligned (and not at the start)
    if a[1] == b[1] and count:
        return count

    # Find new locations in map
    next_a_loc = (a[1][0] + d_dict[a[0]][0], a[1][1] + d_dict[a[0]][1])
    next_b_loc = (b[1][0] + d_dict[b[0]][0], b[1][1] + d_dict[b[0]][1])

    # Find next direction pairs
    next_a = (p_dict[map_dict[next_a_loc]][a[0]], next_a_loc)
    next_b = (p_dict[map_dict[next_b_loc]][b[0]], next_b_loc)

    return recurse(next_a, next_b, count + 1, p_dict, d_dict, map_dict)


# Load data
base_data = load_data(data_filepath, "\n")

# Pad
row_len = len(base_data[0])
base_data.insert(0, "." * row_len)
base_data.append("." * row_len)
base_data = ["." + r + "." for r in base_data]

# Build dictionary of indexed values
map = {(x, y): c for y, r in enumerate(base_data) for x, c in enumerate(r)}

# Find start index and starting directions
loc = get_matching_keys("S", map).pop()
sa, sb = [[d, loc] for d in deltas.keys() if get_start_dirs(d, loc, pipes, deltas, map)]

# Calculate and display furthest location from start point (result 7066)
print(recurse(sa, sb, 0, pipes, deltas, map))
