from msvcrt import getch
import units
import graphics

units_in_play = [{'player': 1, 'turn_group': 1, 'location': ('a', 1), 'tag': 1, 'armor lost': 0, 'strength lost': 0,
                  'health lost': 0}]
turn_order = [[]]

cursor location = ['a', 1]

units = units.init_units_dict('units.csv')
map = graphics.map_selection(1)
render = graphics.render_map(map, units_in_play)

for line in render:
    print(line)
