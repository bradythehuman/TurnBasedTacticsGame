import os
import unit_classes as uc


def graphics(selected_map, cursor_location, unit_key, action_cursor=0, action_list=[]):
    map = map_selection(selected_map)
    scene = render_map(map)
    scene_w_cursor = add_cursor(scene, cursor_location)

    if unit_key:
        scene_w_stats = add_stats(scene_w_cursor, unit_key)
        if action_list:

            print_screen(add_actions(scene_w_stats, action_cursor, action_list))
        else:
            print_screen(scene_w_stats)
    else:
        print_screen(scene_w_cursor)


def string_to_list(string):
    result = []
    for i in string:
        result.append(i)
    return result


def add_stats(render, unit_key):
    unit = uc.unit_dict[unit_key]

    render[1] += string_to_list(unit.name)

    render[3] += string_to_list('Armor: ' + str(unit.current_stats['armor']) + ' / ' + str(unit.effected_stats['str_armor']) + ' (' + str(unit.effected_stats['free_armor']) + ')')
    render[4] += string_to_list('Strength: ' + str(unit.current_stats['strength']) + ' / ' + str(unit.effected_stats['strength']))
    render[5] += string_to_list('Health: ' + str(unit.current_stats['health']) + ' / ' + str(unit.effected_stats['health']))
    render[6] += string_to_list('Damage: ' + str(unit.current_stats['damage']) + ' / ' + str(unit.effected_stats['weapon_damage']) + ' (' + str(unit.effected_stats['str_damage_lo']) + ':' + str(unit.effected_stats['str_damage_hi']) + ')')
    render[7] += string_to_list('Initiative: ' + str(unit.current_stats['initiative']) + ' / ' + str(unit.effected_stats['initiative']))
    render[8] += string_to_list('Recovery: ' + str(unit.effected_stats['recovery']))
    if unit.effected_stats['attack_range_lo'] == unit.effected_stats['attack_range_hi']:
        render[9] += string_to_list('Attack Range: ' + str(unit.effected_stats['attack_range_lo']))
    else:
        render[9] += string_to_list('Attack Range: ' + str(unit.effected_stats['attack_range_lo']) + ':' + str(unit.effected_stats['attack_range_hi']))

    return render


def add_actions(scene, action_cursor, action_list):
    if action_cursor <= 3:
        added_lines = ['  ' + x for x in action_list[:5]]
        print(added_lines[action_cursor])

        added_lines[action_cursor] = ' [' + added_lines[action_cursor][2:] + ']'
    elif action_cursor == len(action_list) - 1:
        added_lines = ['   ' + x for x in action_list[-5:]]
        added_lines[4] = '  [' + added_lines[4][2:] + ']'
    else:
        added_lines = ['   ' + x for x in action_list[action_cursor - 3:action_cursor + 2]]
        added_lines[3] = '  [' + added_lines[3][2:] + ']'

    added_lines = [string_to_list(line) for line in added_lines]
    return scene + added_lines



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


def render_map(map):
    populated_map = populate_map(map)

    row_order = ['top', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                 '18', '19', '20', 'bottom']

    render = []
    for i in range(0, 25):
        render.append([' '] * 89)

    for i in range(len(row_order)):
        for j in range(len(populated_map[row_order[i]])):
            render[i + 1][j * 2 + 3] = populated_map[row_order[i]][j]

    return render


def populate_map(map_mod):
    for key in uc.unit_dict:
        location = uc.unit_dict[key].location
        map_mod[location[0]][location[1]] = uc.unit_dict[key].icon
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
