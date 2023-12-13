data_filepath = "day-02/data.txt"


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


def get_game_id(game):
    """
    Args:
        game (e.g.): "Game 1"
    Returns:
        (e.g.): 1
    """

    game_id = game.split(" ")

    return int(game_id[1])


def get_draw_dict(draw_string):
    """
    Args:
        draw_string (e.g.): "3 blue, 4 red"
    Returns:
        (e.g.): {"red": 4, "blue": 3}
    """

    return {i.split(" ")[1]: int(i.split(" ")[0]) for i in draw_string.split(", ")}


def process_game_data(game_data_string):
    """
    Args:
        game_data_string (e.g.): "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    Returns:
        (e.g.): [{"r": 4, "b": 3}, {"r": 1, "g": 2, "b": 6}, {"g": 2}]
    """

    game_data = game_data_string.split("; ")

    return [get_draw_dict(i) for i in game_data]


def build_game_dict(puzzle):
    """
    Args:
        puzzle: input data, split on newlines
    Returns:
        dictionary of game IDs (keys) and processed game data (values)
    """

    # Split on colon
    puzzle = [r.split(": ") for r in puzzle]

    # Get dictionary keys (game numbers)
    keys = [get_game_id(r[0]) for r in puzzle]

    # Build dictionary values
    vals = [process_game_data(r[1]) for r in puzzle]

    return dict(zip(keys, vals))


def get_power(game_data):
    """
    Args:
        game_data (e.g.): (1, [{"blue": "3", "red": "4"}, {"red": "1", "green": "2", "blue": "6"}, {"green": "2"}])
    Returns:
        True if all draws could have come from bag
    """
    min_bag = {"red": 0, "green": 0, "blue": 0}

    game_id, draws = game_data

    for draw in draws:
        for k in draw.keys():
            if min_bag[k] < draw[k]:
                min_bag[k] = draw[k]

    return min_bag["red"] * min_bag["green"] * min_bag["blue"]


# Load data
puzzle = load_data(data_filepath, "\n")

# Process data
puzzle = build_game_dict(puzzle)

# Get powers
puzzle = [get_power(game) for game in puzzle.items()]

# Sum list (result 63711)
print(sum(puzzle))
