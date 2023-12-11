data_filepath = "day-05/data-test.txt"


def load_data(filepath, split_delimiter):
    """
    Args:
        filepath (e.g.): "day-02/data.txt"
        split_delimiter (e.g.): "\n"
    Returns:
        list of entries, split on double newlines
    """

    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def create_mapping_dict(map_string):
    """
    Args:
        map_string (e.g.): "50 98 2"
    Returns:
        (e.g.): {"to": 50, "from": 98, "range": 2}
    """

    map = map_string.split(" ")
    return {"to": int(map[0]), "from": int(map[1]), "range": int(map[2])}


def process_map(map):
    """
    Args:
        map (e.g.): 'seed-to-soil map:\n50 98 2\n52 50 48'
    Returns:
        descriptor (e.g.): 'seed-to-soil map'
        processed_values (e.g.): [{'from_start': '50', 'to_start': '98', 'range': '2'}]
    """

    descriptor, values = map.split(":\n")
    return [create_mapping_dict(r) for r in values.split("\n")]


def transform(layer, value, maps, forward):
    src, dest = ("to", "from") if forward else ("from", "to")

    for m in maps[layer]:
        if m[src] <= value < m[src] + m["range"]:
            return m[dest] + (value - m[src])

    # No mapping found
    return value


def recurse_back(layer, value, maps):
    if layer == -1:
        return value

    # Calculate new value
    value = transform(layer, value, maps, False)

    # Recurse
    return recurse_back(layer - 1, value, maps)


def recurse_forward(layer, value, maps):
    if layer == len(maps):
        return value

    # Calculate new value
    value = transform(layer, value, maps, True)

    # Recurse
    return recurse_forward(layer + 1, value, maps)


def test_seed_range(val, seeds_list):
    for s in seeds_list:
        if s["start"] <= val < s["start"] + s["range"]:
            return True

    return False


# Load data
base_data = load_data(data_filepath, "\n\n")

# Process seed values
seeds = base_data.pop(0)
descriptor, seeds = seeds.split(": ")
seeds = [int(i) for i in seeds.split(" ")]

# Pair elements and assign to nested dictionaries
seeds = zip(seeds[::2], seeds[1::2])
seeds = [{"start": i[0], "range": i[1]} for i in seeds]

# Process maps
maps = [process_map(i) for i in base_data]

# Enumerate
maps_enum = enumerate(maps)

# Generate test candidates (the lower bound of each range in each layer)
test_vals = [(i, m["to"]) for i, map in maps_enum for m in map]

# Add the lower bounds of each seed range
test_vals = test_vals + [(-1, m["start"]) for m in seeds]

# Recurse back
test_vals = [(c[0], c[1], recurse_back(*c, maps)) for c in test_vals]

# Recurse forward
test_vals = [(c[0], c[1], c[2], recurse_forward(c[0], c[1], maps)) for c in test_vals]

# Filter values where input is outside a seed range
test_vals = filter(lambda x: test_seed_range(x[2], seeds), test_vals)

# Sort by lowest match
test_vals = sorted(test_vals, key=lambda x: x[3])

# Display output
print(test_vals[0])
