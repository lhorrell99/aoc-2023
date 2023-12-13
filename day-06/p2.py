data_filepath = "day-06/data.txt"


def load_data(filepath, split_delimiter):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


def process_base_data(base_string):
    label, data = base_string.split(":")
    data = data.split()
    return int("".join(data))


def get_roots(a, b, c):
    desc_root = (b**2 - 4 * a * c) ** 0.5
    return (-b + desc_root) / (2 * a), (-b - desc_root) / (2 * a)


# Process base data (note: t = time, r = record, c = charge, s = distance)
base_data = load_data(data_filepath, "\n")
t = process_base_data(base_data[0])
r = process_base_data(base_data[1])

# Find roots of 0 >= c**2 - t * c + r (quadratic rule)
root_1, root_2 = get_roots(1, -t, r)

# Display number of integer values satisfying inequality (result 20048741)
print(int(root_1) - int(root_2))
