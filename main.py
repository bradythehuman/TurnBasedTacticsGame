from msvcrt import getch
import units
import graphics

units_in_play = {'1': {'player': 1, 'turn group': 1, 'location': ('1', 1), 'tag': 1, 'armor lost': 0,
                       'strength lost': 0, 'health lost': 0, 'initiative lost': 0, 'status effects': []}}
unit_id_counter = 1
turn_order = [[]]

cursor_location = ['1', 1, '1by1_square']
map = graphics.map_selection(1)

running = True

while running:
    scene = graphics.render_map(map, units_in_play)
    scene_w_cursor = graphics.add_cursor(scene, cursor_location)
    scene_w_stats = units.add_stats(scene_w_cursor, cursor_location, units_in_play)
    graphics.print_screen(scene_w_stats)
    ch = getch()
    cursor_location = graphics.move_cursor(ch, cursor_location)
    print(ch)
