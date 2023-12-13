data_filepath = "day-05/data.txt"


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
        map (e.g.): "seed-to-soil map:\n50 98 2\n52 50 48"
    Returns:
        descriptor (e.g.): "seed-to-soil map"
        processed_values (e.g.): [{"from_start": "50", "to_start": "98", "range": "2"}]
    """

    descriptor, values = map.split(":\n")
    return [create_mapping_dict(r) for r in values.split("\n")]


def transform(layer, value, maps, forward):
    """
    Args:
        layer (e.g.): 1
        value (e.g.): 50
        maps (e.g.): [[{"from_start": "50", "to_start": "98", "range": "2"}]]
        forward (e.g.): True
    Returns:
        the new value after applying the transformation from the specified map and layer
    """

    src, dest = ("from", "to") if forward else ("to", "from")

    for m in maps[layer]:
        if m[src] <= value < m[src] + m["range"]:
            return m[dest] + (value - m[src])

    # No mapping found
    return value


def recurse_forward(layer, value, maps):
    """
    Args:
        layer (e.g.): 1
        value (e.g.): 50
        maps (e.g.): [[{"from_start": "50", "to_start": "98", "range": "2"}]]
    Returns:
        the corresponding location value
    """

    if layer == len(maps):
        return value

    # Calculate new value
    value = transform(layer, value, maps, True)

    # Recurse
    return recurse_forward(layer + 1, value, maps)


# Load data
base_data = load_data(data_filepath, "\n\n")

# Process seed values
seeds = base_data.pop(0)
descriptor, seeds = seeds.split(": ")
seeds = [int(i) for i in seeds.split(" ")]

# Process maps
maps = [process_map(i) for i in base_data]

# Find locations
locations = [recurse_forward(0, s, maps) for s in seeds]

# Print closest location (result 165788812)
print(min(locations))
