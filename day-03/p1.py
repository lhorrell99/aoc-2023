data_filepath = "day-03/data.txt"


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


def test_neighbours(candidate, schema_string, symbols, rel_indices):
    """
    Args:
        candidate: (index, value) tuple to test e.g. (13, "4")
        schema_string: the (1D) engine schematic
        symbols: all symbols contained in engine schematic
        rel_indices: relative locations of neighbours in schema_string
    Returns:
        True if value has a symbolic neighbour
    """

    for i in rel_indices:
        if schema_string[candidate[0] + i] in symbols:
            return True

    return False


def explore_neighbours(candidate, schema_string):
    """
    Args:
        candidate: (index, value) tuple to test e.g. (13, "4")
        schema_string: the (1D) engine schematic
    Returns:
        complete continuous number and starting index
    """

    def recurse_right(i):
        if schema_string[i + 1].isnumeric():
            return schema_string[i] + recurse_right(i + 1)
        return schema_string[i]

    def recurse_left(i):
        if schema_string[i - 1].isnumeric():
            r_call = recurse_left(i - 1)
            return r_call[0] + schema_string[i], r_call[1]
        return schema_string[i], i

    c_index = candidate[0]
    right = recurse_right(c_index)
    left, start_index = recurse_left(c_index)
    left = left[:-1]

    return (start_index, int(left + right))


# Load data
puzzle = load_data(data_filepath, "\n")
row_len = len(puzzle[0])

# Pad list - north/south
puzzle.insert(0, "." * row_len)
puzzle.append("." * row_len)

# Pad list - east/west
puzzle = ["." + r + "." for r in puzzle]

# Update row_len
row_len = len(puzzle[0])

# Relative indices of neighbours
neighbours = [
    -row_len - 1,
    -row_len,
    -row_len + 1,
    +1,
    row_len + 1,
    row_len,
    row_len - 1,
    -1,
]

# Reduce to 1D string
puzzle_str = "".join(puzzle)

# Find unique characters
unique_chars = "".join(set(puzzle_str))

# Find symbols (except period)
puzzle_symbols = "".join(c for c in unique_chars if not c.isnumeric() and not c == ".")

# Save indices of all elements
puzzle_enum = list(enumerate(puzzle_str))

# Remove all symbols
puzzle_digits = list(filter(lambda x: x[1].isnumeric(), puzzle_enum))

# Remove any numbers without symbolic neighbours
digits_sym_neighbours = list(
    filter(
        lambda x: test_neighbours(x, puzzle_str, puzzle_symbols, neighbours),
        puzzle_digits,
    )
)

# Find continuous numbers
schema_numbers = [explore_neighbours(i, puzzle_str) for i in digits_sym_neighbours]

# Remove duplicates
schema_numbers = list(set(schema_numbers))

# Print sum (result 528799)
print(sum(i[1] for i in schema_numbers))
