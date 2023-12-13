import sys
from itertools import cycle
from math import lcm

# Increase recursion limit
sys.setrecursionlimit(100000)

data_filepath = "day-08/data.txt"


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def recurse(start, c, mappings, sequence):
    dir = next(sequence)
    dest = mappings[start][dir]

    # Base case
    if dest[2] == "Z":
        return c

    # Recurse
    return recurse(dest, c + 1, mappings, sequence)


# Load data
sequence, mappings = load_data(data_filepath, "\n\n")

# Assign sequence to a cycle
sequence = cycle(list(sequence))

# Build mappings dictionary
mappings = mappings.split("\n")
keys = [i[0:3] for i in mappings]
vals = [{"L": i[7:10], "R": i[12:15]} for i in mappings]
mappings = dict(zip(keys, vals))

# Initially assign all starting locations to dest (and init other counter vars)
dest = list(filter(lambda x: x[2] == "A", keys))

# Find the first "Z" location for each start point
first_z_loc = [recurse(i, 1, mappings, sequence) for i in dest]

# Since "Z" locations are visited at constant intervals, lcm gives answer (result 18215611419223)
print(lcm(*first_z_loc))
