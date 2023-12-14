data_filepath = "day-10/data.txt"


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


# Load data
base_data = load_data(data_filepath, "\n")
