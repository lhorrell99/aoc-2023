from functools import reduce

data_filepath = "day-06/data.txt"


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def process_base_data(base_string):
    label, data = base_string.split(":")
    data = data.split()
    return [int(i) for i in data]


def get_possible_distances(t):
    return [c * (t - c) for c in range(t)]


def filter_distances(d_list, r):
    return list(filter(lambda x: x > r, d_list))


# Process base data
base_data = load_data(data_filepath, "\n")
times = process_base_data(base_data[0])
records = process_base_data(base_data[1])

# Find all possible distances
distances = [get_possible_distances(t) for t in times]

# Enumerate
distances = enumerate(distances)

# Filter any below the record
distances = [filter_distances(d, records[i]) for i, d in distances]

# Count
distances = [len(d) for d in distances]

# Display product (result 633080)
print(reduce((lambda x, y: x * y), distances))
