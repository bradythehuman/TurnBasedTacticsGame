import unit_classes as uc

def string_to_list(string):
    result = []
    for i in string:
        result.append(i)
    return result



def add_stats(render, units_in_play, unit_key):
    unit = uc.unit_dict[unit_key]


    render[1] += string_to_list(unit_specs['name'])

    render[3] += string_to_list('Armor: ' + str(stats['armor'][0]) + ' / ' + str(stats['armor'][1]) + ' (' + str(stats['armor'][2]) + ')')
    render[4] += string_to_list('Strength: ' + str(stats['strength'][0]) + ' / ' + str(stats['strength'][1]))
    render[5] += string_to_list('Health: ' + str(stats['health'][0]) + ' / ' + str(stats['health'][1]))
    render[6] += string_to_list('Damage: ' + str(stats['damage'][0]) + ' / ' + str(stats['damage'][1]) + ' (' + str(stats['damage'][2]) + ':' + str(stats['damage'][3]) + ')')
    render[7] += string_to_list('Initiative: ' + str(stats['initiative'][0]) + ' / ' + str(stats['initiative'][1]))
    render[8] += string_to_list('Recovery: ' + str(stats['recovery']))
    if int(stats['attack_range'][0]) == 1:
        render[9] += string_to_list('Attack Range: ' + str(stats['attack_range'][1]))
    else:
        render[9] += string_to_list('Attack Range: ' + str(stats['attack_range'][0]) + ':' + str(stats['attack_range'][1]))

    return render
