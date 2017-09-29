from msvcrt import getch
import unit_classes as uc
import graphics as g
import actions

cursor_location = ['1', 1, '1by1_square']
selected_map = 1
running = True

uc.dynamic_unit_init('King', ['1', 1], 'Player 1')
uc.dynamic_unit_init('King', ['1', 5], 'Player 2')

while running:  # Main map loop
    unit_key = uc.find_selected_unit(cursor_location)
    g.graphics(selected_map, cursor_location, unit_key)

    ch = getch()
    if ch in b'wasd':
        cursor_location = g.move_cursor(ch, cursor_location)
    elif ch == b'\r' and unit_key:  # Ability select loop
        action_list_cursor = 0
        selected_action = ''
        action_list = ['move', 'b', 'c', 'd', 'e', 'f', 'g']
        while not selected_action:  # Action selection loop
            g.graphics(selected_map, cursor_location, unit_key, action_list_cursor, action_list)
            ch = getch()
            if ch in b'ws':
                if ch == b'w' and action_list_cursor > 0:
                    action_list_cursor -= 1
                elif ch == b's' and action_list_cursor < len(action_list) - 1:
                    action_list_cursor += 1
            elif ch == b'\r':
                selected_action = action_list[action_list_cursor]
                action_list = []
        actions.action(selected_action, unit_key, selected_map)
