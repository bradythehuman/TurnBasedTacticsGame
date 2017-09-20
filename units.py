# Turns units.csv into a dictionary of dictionaries named units. 1 dictionary for each unit. Key is tag column on csv
with open('units.csv', 'r') as f:
    lines_string = f.readlines()

    lines = []
    for line in lines_string:
        line = line.rstrip('\n')
        lines.append(line.split(','))

    units = {}
    for line in lines[1:]:
        unit = {}
        for i in range(1, len(line)):
            key = lines[0][i]
            value = line[i]
            try:
                unit[key] = int(value)
            except ValueError:
                if ';' in value:
                    unit[key] = value.split(';')
                else:
                    unit[key] = value
        units[line[0]] = unit


# For stats with a maximum and a current value a tuple is given in the form (current, maximum)
def retrieve_stats(unit_in_play, unit_specs=0):
    if not unit_specs:
        unit_specs = units[unit_in_play['tag']]

    arm_loss_str = unit_specs['strength_armor'] - unit_in_play['armor lost'] - unit_specs['strength'] + unit_in_play['strength lost']
    if arm_loss_str >= 0:
        armor = unit_specs['strength_armor'] + unit_specs['free_armor'] - unit_in_play['armor lost']
    else:
        armor = unit_specs['strength_armor'] + unit_specs['free_armor'] - unit_in_play['armor lost'] - arm_loss_str

    strength = unit_specs['strength'] - unit_in_play['strength lost']

    health = unit_specs['health'] - unit_in_play['health lost']

    max_str_dmg = unit_specs['strength_damage_high'] - unit_specs['strength_damage_low'] + 1
    if strength < unit_specs['strength_damage_low']:
        damage = unit_specs['weapon_damage']
    elif strength > unit_specs['strength_damage_high']:
        damage = unit_specs['weapon_damage'] + max_str_dmg
    else:
        damage = unit_specs['weapon_damage'] + strength - unit_specs['strength_damage_low'] + 1

    initiative = unit_specs['initiative'] - unit_in_play['initiative lost']

    stats = {'name': unit_specs['name'],
             'armor': [armor, unit_specs['strength_armor'], unit_specs['free_armor']],
             'strength': [strength, unit_specs['strength']],
             'health': [health, unit_specs['health']],
             'damage': [damage, unit_specs['weapon_damage'], unit_specs['strength_damage_low'], unit_specs['strength_damage_high']],
             'initiative': [initiative, unit_specs['initiative']],
             'recovery': unit_specs['recovery'],
             'attack_range': unit_specs['attack_range']
             }
    return stats


def string_to_list(string):
    result = []
    for i in string:
        result.append(i)
    return result


def add_stats(render, cursor, units_in_play):
    unit_id = 0
    for key in units_in_play:
        if units_in_play[key]['location'][0] == cursor[0] and units_in_play[key]['location'][1] == cursor[1]:
            unit_id = key

    if unit_id:
        unit_in_play = units_in_play[unit_id]
        unit_specs = units[str(unit_in_play['tag'])]

        stats = retrieve_stats(unit_in_play, unit_specs=unit_specs)

        render[1] += string_to_list(unit_specs['name'])

        render[3] += string_to_list('Armor: ' + str(stats['armor'][0]) + ' / ' + str(stats['armor'][1]) + ' (' + str(stats['armor'][2]) + ')')
        render[4] += string_to_list('Strength: ' + str(stats['strength'][0]) + ' / ' + str(stats['strength'][1]))
        render[5] += string_to_list('Health: ' + str(stats['health'][0]) + ' / ' + str(stats['health'][1]))
        render[6] += string_to_list('Damage: ' + str(stats['damage'][0]) + ' / ' + str(stats['damage'][1]) + ' (' + str(stats['damage'][2]) + ':' + str(stats['damage'][3]) + ')')
        render[7] += string_to_list('Initiative: ' + str(stats['initiative'][0]) + ' / ' + str(stats['initiative'][1]))
        render[8] += string_to_list('Recovery: ' + str(stats['recovery']))
        if stats['attack_range'][0] == 1:
            render[9] += string_to_list('Attack Range: ' + str(stats['attack_range'][1]))
        else:
            render[9] += string_to_list('Attack Range: ' + str(stats['attack_range'][0]) + ':' + str(stats['attack_range'][1]))

    return render
