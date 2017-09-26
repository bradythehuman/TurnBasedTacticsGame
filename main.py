from msvcrt import getch
import unit_classes as uc
import graphics as g

units_in_play = {'1': {'player': 1, 'turn group': 1, 'location': ('1', 1), 'tag': 1, 'armor lost': 0,
                       'strength lost': 0, 'health lost': 0, 'initiative lost': 0, 'status effects': []}}



cursor_location = ['1', 1, '1by1_square']
selected_map = g.map_selection(1)

running = True

while running:  # Main map loop
    unit_key = uc.find_selected_unit(cursor_location)
    g.graphics(selected_map, units_in_play, cursor_location, unit_key)

    ch = getch()
    if ch in b'wasd':
        cursor_location = g.move_cursor(ch, cursor_location)
    elif ch == b'\r' and unit_key:  # Ability select loop
        action_list_cursor = 0
        selected_action = ''
        action_list = []
        while not selected_action:
            ch = getch()
            if ch in b'ws':
                if ch == b'w' and action_list_cursor > 0:
                    action_list_cursor += 1
                elif ch == b's' and action_list_cursor < len(action_list) - 1:
                    action_list_cursor -= 1
            elif ch == b'\r':
                selected_action = action_list[action_list_cursor]
                action_list = []

    print(ch)