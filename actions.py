import unit_classes as uc
import graphics
from msvcrt import getch


def action(action, unit_key, map_num):
    map = graphics.map_selection(map_num)

    if action == 'move':
        move(unit_key, map)


def get_location(unit_key, map, prompt):
    location = uc.unit_dict[unit_key].location + ['1by1_square']
    selected_location = []

    while not selected_location:
        selected_key = uc.find_selected_unit(location)
        scene = graphics.render_map(map)
        scene = graphics.add_cursor(scene, location)

        if selected_key:
            scene = graphics.add_stats(scene, selected_key)

        scene = scene + [graphics.string_to_list('   ' + prompt)]
        graphics.print_screen(scene)

        ch = getch()
        if ch in b'wasd':
            location = graphics.move_cursor(ch, location)
        elif ch == b'e':
            location = uc.unit_dict[unit_key].location
        elif ch == b'\r':
            selected_location = location
    return selected_location


def get_target(prompt):
    pass


def get_input(prompt):
    pass


def move(unit_key, map):
    max_movement = uc.unit_dict[unit_key].effected_stats['movement']
    starting_location = uc.unit_dict[unit_key].location
    spaces_moved = 0
    while spaces_moved > max_movement or spaces_moved == 0:
        target = get_location(unit_key, map, 'Select an empty space up to ' + str(max_movement) + ' spaces away...')
        spaces_moved = abs(int(starting_location[0]) - int(target[0])) + abs(starting_location[1] - target[1])
        for key in uc.unit_dict:
            if uc.unit_dict[key].location == target[:2]:
                spaces_moved = 0

    uc.unit_dict[unit_key].location = target
