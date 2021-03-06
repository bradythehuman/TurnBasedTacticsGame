effected_stats = {'block': ['str_armor'],
                  'bleed': ['health']
                  }


def run_effect(effect, type, stats):
    if effect == 'block':
        return block(type, stats)
    elif effect == 'bleed':
        return bleed(type, stats)


def block(type, stats):  # stats = (armor)
    if type == 'stat':
        return stats[0] + 2


def bleed(type, stats):  # stats = (health)
    if type == 'end_of_turn':
        return stats[0] - 1
