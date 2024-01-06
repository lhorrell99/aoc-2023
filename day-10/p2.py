import sys

# Increase recursion limit
sys.setrecursionlimit(100000)

data_filepath = "day-10/data-test.txt"

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

# Define corners
corners = ["L", "J", "7", "F"]


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def get_matching_keys(val, search_dict):
    keys = [k for k, v in search_dict.items() if v == val]
    return keys


def is_start_dir(d, start_loc, p_dict, d_dict, map_dict):
    new_loc = (start_loc[0] + d_dict[d][0], start_loc[1] + d_dict[d][1])
    return True if d in p_dict[map_dict[new_loc]] else False


def recurse_find_corners(start_loc, a, count, p_dict, d_dict, map_dict):
    # Find new location in map
    next_a_loc = (a[1][0] + d_dict[a[0]][0], a[1][1] + d_dict[a[0]][1])

    # Find next direction pair
    next_a = (p_dict[map_dict[next_a_loc]][a[0]], next_a_loc)

    # Save value if it is a corner
    ret_val = [next_a] if map_dict[next_a_loc] in corners else []

    # Mark the location as visited in the map_dict
    map_dict[next_a_loc] = "*"

    # Base case - back to the start
    if next_a_loc == start_loc and count:
        return ret_val

    # Recurse
    return ret_val + recurse_find_corners(
        start_loc, next_a, count + 1, p_dict, d_dict, map_dict
    )


def expand_vert_edge(a, b):
    return [(a[0], i) for i in range(a[1], b[1] + 1)]


def get_edge_intersections(x, y, v_edges_flattened, count):
    # Base case - reached array padding
    if not x:
        return count
    
    # Increment if current point intersects and edge
    if (x, y) in v_edges_flattened:
        count += 1

    # Recurse
    return get_edge_intersections(x - 1, y, v_edges_flattened, count)


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

# Get starting directions and sort alphabetically
s_dirs = [d for d in deltas.keys() if is_start_dir(d, loc, pipes, deltas, map)]
s_dirs = sorted(s_dirs)

# Get start piece from starting directions
s_piece = [k for k in pipes.keys() if sorted(list(pipes[k].values())) == s_dirs].pop()

# Replace start piece
map[loc] = s_piece

# Recursively find polygon corners
poly_path = recurse_find_corners(loc, (s_dirs.pop(), loc), 0, pipes, deltas, map)

# Drop directions
poly_path = [i[1] for i in poly_path]

# Split poly_path into separate edges
poly_edges = list(zip(poly_path, poly_path[1:]))

# Get a list of all points that are not on the path
test_points = [k for k, v in map.items() if not v == "*"]

# Remove all horizontal poly_path elements (don't have to check)
poly_edges_vert = [e for e in poly_edges if e[0][0] == e[1][0]]

# Sort edges
poly_edges_vert = [sorted(e, key=lambda x: x[1]) for e in poly_edges_vert]

# Expand edges
poly_edges_vert = [expand_vert_edge(*e) for e in poly_edges_vert]

# Flatten edges
edges = [i for row in poly_edges_vert for i in row]

# Count edge intersections
edge_intersections = [get_edge_intersections(*xy, edges, 0) for xy in test_points]

# Filter out even values
in_poly = list(filter(lambda x: x % 2, edge_intersections))

# Display result
print(len(in_poly))
