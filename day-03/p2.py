data_filepath = "day-03/data-test.txt"


def load_data(filepath):
    """
    Args:
        filepath (e.g.): "day-02/data.txt"
    Returns:
        list of entries, split on newlines
    """

    with open(filepath) as file:
        data = file.read()

    return data.split("\n")


def test_neighbours(candidate, schema_string, symbols, rel_indices):
    """
    Args:
        candidate: (index, value) tuple to test e.g. (13, '4')
        schema_string: the (1D) engine schematic
        symbols: all symbols contained in engine schematic
        rel_indices: relative locations of neighbours in schema_string
    Returns:
        Index of symbolic neighbour (if present)
    """

    for i in rel_indices:
        if schema_string[candidate[0] + i] in symbols:
            # Only ever 1 symbol adjacent to a number (tested)
            return candidate[0] + i

    return None


def explore_neighbours(c_index, schema_string):
    """
    Args:
        candidate: (index, value) tuple to test e.g. (13, '4')
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

    right = recurse_right(c_index)
    left, start_index = recurse_left(c_index)
    left = left[:-1]

    return [start_index, int(left + right)]


puzzle = load_data(data_filepath)
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

# Save indices of all elements
puzzle_enum = list(enumerate(puzzle_str))

# Remove all symbols
puzzle_digits = list(filter(lambda x: x[1].isnumeric(), puzzle_enum))

# Find all digits with symbolic ("*") neighbours (tuple format is (index, value, symbolic neighbour index))
digits_sym_neighbours = [
    [n[0], n[1], test_neighbours(n, puzzle_str, "*", neighbours)] for n in puzzle_digits
]

# Remove any digits without any symbolic ("*") neighbours
digits_sym_neighbours = filter(lambda x: x[2], digits_sym_neighbours)

# Find continuous numbers (tuple format is (start index, value, symbolic neighbour index))
schema_numbers = [explore_neighbours(i[0], puzzle_str) + [i[2]] for i in digits_sym_neighbours]

# Convert to tuples (enables hashing)
schema_numbers = [tuple(i) for i in schema_numbers]

# Remove duplicates
schema_numbers = list(set(schema_numbers))
