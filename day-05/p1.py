data_filepath = "day-05/data.txt"


def load_data(filepath):
    """
    Args:
        filepath (e.g.): "day-02/data.txt"
    Returns:
        list of entries, split on double newlines
    """

    with open(filepath) as file:
        data = file.read()

    return data.split("\n\n")


def process_map(map):
    """
    Args:
        map (e.g.): 'seed-to-soil map:\n50 98 2\n52 50 48'
    Returns:
        descriptor (e.g.): 'seed-to-soil map'
        processed_values (e.g.): [{'from_start': '50', 'to_start': '98', 'range': '2'}]
    """

    # Extract map descriptor
    descriptor, values = map.split(":\n")

    processed_values = []
    for row in values.split("\n"):
        row = row.split(" ")
        processed_values.append(
            {"to_start": int(row[0]), "from_start": int(row[1]), "range": int(row[2])}
        )

    return descriptor, processed_values


def find_mapping(val, maps, from_to_key):
    """
    Args:
        val (e.g.): 79
        maps: dictionary of map data
        from_to_key (e.g.): "seed-to-soil map"
    Returns:
        the mapped value
    """

    for m in maps[from_to_key]:
        if m["from_start"] <= val < m["from_start"] + m["range"]:
            return m["to_start"] + (val - m["from_start"])

    # No mapping found
    return val


base_data = load_data(data_filepath)
seeds = base_data.pop(0)

# Process seeds values
seeds = seeds.split(": ")[1]
seeds = [int(i) for i in seeds.split(" ")]

# Process maps (TODO: clean up)
keys = [process_map(i)[0] for i in base_data]
vals = [process_map(i)[1] for i in base_data]
maps = dict(zip(keys, vals))

# Get seed-to-soil maps
soils = [find_mapping(i, maps, "seed-to-soil map") for i in seeds]

# Get soil-to-fertilizer maps
fertilizers = [find_mapping(i, maps, "soil-to-fertilizer map") for i in soils]

# Get fertilizer-to-water maps
waters = [find_mapping(i, maps, "fertilizer-to-water map") for i in fertilizers]

# Get water-to-light maps
lights = [find_mapping(i, maps, "water-to-light map") for i in waters]

# Get light-to-temperature maps
temperatures = [find_mapping(i, maps, "light-to-temperature map") for i in lights]

# Get temperature-to-humidity maps
humidities = [find_mapping(i, maps, "temperature-to-humidity map") for i in temperatures]

# Get humidity-to-location maps
locations = [find_mapping(i, maps, "humidity-to-location map") for i in humidities]

# Print closest location (result 165788812)
print(min(locations))
