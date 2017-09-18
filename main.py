from msvcrt import getch
import functions

units = {'tag': ['name', 'strength_armor', 'free_armor', 'strength', 'health', 'initiative', 'recovery',
                 'weapon_damage', 'strength_damage_low', 'strength_damage_high', 'footprint_diameter', 'attack_radius',
                 'faction', ['ability_names']]}

units_in_play = {'example': ['tag', ]}

turn_order = [[]]

board = {'top': ["-"]*120,
         'a': ["-"]*100,
         'b': ["-"]*80,
         'c': ["-"]*60,
         'd': ["-"]*10,
         'e': ["-"]*10,
         'f': ["-"]*10,
         'g': ["-"]*10,
         'h': ["-"]*10,
         'i': ["-"]*10,
         'j': ["-"]*10,
         'bottom': ["-"]*10,
         }

row_order = ['top', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'bottom']

functions.display(board)

while True:
    value = getch()
    print(value)
