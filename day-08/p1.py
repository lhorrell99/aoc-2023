import sys
from itertools import cycle

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

    # Base case - "ZZZ" reached
    if dest == "ZZZ":
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

# Recursively find solution
print(recurse("AAA", 1, mappings, sequence))
