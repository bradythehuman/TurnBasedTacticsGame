import os


def map_selection(map_number):
    if map_number == 1:
        map = {'top': ['#'] * 42,
               'a': ['#'] + ["-"] * 40 + ['#'],
               'b': ['#'] + ["-"] * 40 + ['#'],
               'c': ['#'] + ["-"] * 40 + ['#'],
               'd': ['#'] + ["-"] * 40 + ['#'],
               'e': ['#'] + ["-"] * 40 + ['#'],
               'f': ['#'] + ["-"] * 40 + ['#'],
               'g': ['#'] + ["-"] * 40 + ['#'],
               'h': ['#'] + ["-"] * 40 + ['#'],
               'i': ['#'] + ["-"] * 40 + ['#'],
               'j': ['#'] + ["-"] * 40 + ['#'],
               'k': ['#'] + ["-"] * 40 + ['#'],
               'l': ['#'] + ["-"] * 40 + ['#'],
               'm': ['#'] + ["-"] * 40 + ['#'],
               'n': ['#'] + ["-"] * 40 + ['#'],
               'o': ['#'] + ["-"] * 40 + ['#'],
               'p': ['#'] + ["-"] * 40 + ['#'],
               'q': ['#'] + ["-"] * 40 + ['#'],
               'r': ['#'] + ["-"] * 40 + ['#'],
               's': ['#'] + ["-"] * 40 + ['#'],
               't': ['#'] + ["-"] * 40 + ['#'],
               'bottom': ['#'] * 42,
               'dimensions': (20, 40)
               }
    else:
        map = {}
    return map


def render_map(map, units_in_play):
    populated_map = populate_map(map, units_in_play)

    row_order = ['top', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'bottom']
    render = [' ' * 89]
    for i in row_order:
        render.append('   ' + ' '.join(populated_map[i]) + '   ')
    render.append(' ' * 89)


    return render


def clear_screen():
    os.system('cls')


def populate_map(map_mod, units_in_play):
    for i in units_in_play:
        location = i['location']
        map_mod[location[0]][location[1]] = 'X'
    return map_mod


def print_screen(screen_type):
    pass


# converts spaces on map to space on main grid
def map_to_render(tuple):
    coordinates_y_x = [0, 0]
    coordinates_y_x[0] = tuple[0] -95
    coordinates_y_x[1] = tuple[1] * 2 + 3
    return coordinates_y_x


def map_to_render_verticle(letter):
    return letter[0] -95


def map_to_render_horizontal(number):
    return number[1] * 2 + 3
