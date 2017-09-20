import os


def map_selection(map_number):
    if map_number == 1:
        map = {'top': ['#'] * 42,
               '1': ['#'] + ["-"] * 40 + ['#'],
               '2': ['#'] + ["-"] * 40 + ['#'],
               '3': ['#'] + ["-"] * 40 + ['#'],
               '4': ['#'] + ["-"] * 40 + ['#'],
               '5': ['#'] + ["-"] * 40 + ['#'],
               '6': ['#'] + ["-"] * 40 + ['#'],
               '7': ['#'] + ["-"] * 40 + ['#'],
               '8': ['#'] + ["-"] * 40 + ['#'],
               '9': ['#'] + ["-"] * 40 + ['#'],
               '10': ['#'] + ["-"] * 40 + ['#'],
               '11': ['#'] + ["-"] * 40 + ['#'],
               '12': ['#'] + ["-"] * 40 + ['#'],
               '13': ['#'] + ["-"] * 40 + ['#'],
               '14': ['#'] + ["-"] * 40 + ['#'],
               '15': ['#'] + ["-"] * 40 + ['#'],
               '16': ['#'] + ["-"] * 40 + ['#'],
               '17': ['#'] + ["-"] * 40 + ['#'],
               '18': ['#'] + ["-"] * 40 + ['#'],
               '19': ['#'] + ["-"] * 40 + ['#'],
               '20': ['#'] + ["-"] * 40 + ['#'],
               'bottom': ['#'] * 42,
               'dimensions': (20, 40)
               }
    else:
        map = {}
    return map


def render_map(map, units_in_play):
    populated_map = populate_map(map, units_in_play)

    row_order = ['top', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                 '18', '19', '20', 'bottom']

    render = []
    for i in range(0, 25):
        render.append([' '] * 89)

    for i in range(len(row_order)):
        for j in range(len(populated_map[row_order[i]])):
            render[i + 1][j * 2 + 3] = populated_map[row_order[i]][j]

    return render


def populate_map(map_mod, units_in_play):
    for key in units_in_play:
        location = units_in_play[key]['location']
        map_mod[location[0]][location[1]] = 'X'
    return map_mod


def print_screen(render):
    os.system('cls')
    for line in render:
        print(''.join(line))


def map_to_render_vertical(key):
    if key == 'top':
        result = 1
    elif key == 'bottom':
        result = 24
    else:
        result = int(key) + 1
    return result


def map_to_render_horizontal(number):
    return number * 2 + 3

# cursor_render uses amount of spaces offset on a map. Not offset on the render. Also uses (y, x)
cursor_render = {'1by1_square': {'[': [(0, 0)],
                                 ']': [(0, 0)],
                                 'vertical_range': (0, 0),
                                 'horizontal_range': (0, 0)},
                 '2by2_square': {'[': [(0, 0), (1, 0)],
                                 ']': [(0, 1), (1, 1)],
                                 'vertical_range': (0, 1),
                                 'horizontal_range': (0, 1)}
                 }


def add_cursor(render, cursor):
    for i in cursor_render[cursor[2]]['[']:
        render[map_to_render_vertical(cursor[0]) + i[0]][map_to_render_horizontal(cursor[1]) - 1 + i[1]] = '['

    for i in cursor_render[cursor[2]][']']:
        render[map_to_render_vertical(cursor[0]) + i[0]][map_to_render_horizontal(cursor[1]) + 1 + i[1]*2] = ']'

    return render


def move_cursor(ch, cursor):
    vertical = int(cursor[0])
    vertical_range = cursor_render[cursor[2]]['vertical_range']
    horizontal_range = cursor_render[cursor[2]]['horizontal_range']

    if ch == b'w' and vertical + vertical_range[0] > 1:
        cursor[0] = str(vertical - 1)
    elif ch == b's' and 20 > vertical + vertical_range[1]:
        cursor[0] = str(vertical + 1)
    elif ch == b'a' and 1 < cursor[1] + horizontal_range[0]:
        cursor[1] = cursor[1] - 1
    elif ch == b'd' and 40 > cursor[1] + horizontal_range[1]:
        cursor[1] = cursor[1] + 1
    elif ch == b'e':
        if cursor[2] == '1by1_square':
            cursor = change_cursor(cursor, '2by2_square')
        else:
            cursor = change_cursor(cursor, '1by1_square')

    return cursor


def change_cursor(cursor, new_type):
    vertical = int(cursor[0])
    vertical_range = cursor_render[new_type]['vertical_range']
    horizontal_range = cursor_render[new_type]['horizontal_range']

    if 20 < vertical + vertical_range[1]:
        cursor[0] = str(vertical - 1)
    elif vertical + vertical_range[0] < 1:
        cursor[0] = str(vertical + 1)

    if cursor[1] + horizontal_range[1] > 40:
        cursor[1] = cursor[1] - 1
    elif 1 > cursor[1] + horizontal_range[0]:
        cursor[1] = cursor[1] + 1

    cursor[2] = new_type
    return cursor
