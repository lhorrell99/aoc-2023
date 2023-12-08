data_filepath = "day-02/data.txt"

bag = {"red": 12, "green": 13, "blue": 14}


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
        game_data (e.g.): [{"r": 4, "b": 3}, {"r": 1, "g": 2, "b": 6}, {"g": 2}]
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


def filter_game(game_data, bag_data):
    """
    Args:
        game_data (e.g.): (1, [{'blue': '3', 'red': '4'}, {'red': '1', 'green': '2', 'blue': '6'}, {'green': '2'}])
    Returns:
        True if all draws could have come from bag, false if not
    """

    game_id, draws = game_data

    for draw in draws:
        for k in draw.keys():
            if bag[k] < draw[k]:
                return False

    return True


# Load data
puzzle = load_data(data_filepath)

# Process data
puzzle = build_game_dict(puzzle)

# Filter impossible games
puzzle = dict(filter(lambda x: filter_game(x, bag), puzzle.items()))

# Sum remaining keys (result 2439)
print(sum(puzzle.keys()))
