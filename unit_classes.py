import effects

unit_count = 1
turn_order = [('player', 'leader', ['minions'])]
unit_dict = {}


def find_selected_unit(cursor):
    unit_key = ''
    for key in unit_dict:
        if unit_dict['location'][0] == cursor[0] and unit_dict[key]['location'][1] == cursor[1]:
            unit_key = key
    return unit_key


def dynamic_unit_init(unit_type, location):
    constructor = globals()[unit_type]
    unit_dict[str(unit_count)] = constructor(location)
    return unit_count + 1


class Unit:
    basic_actions = ['move', 'attack', 'rest', 'play_card']

    def __init__(self, location):
        self.location = location
        self.footprint_diameter = 1
        self.faction = None
        self.effects = ['block']
        self.effected_stats = None
        self.current_stats = {}
        self.resource_damage = {'armor': 0,
                                'strength': 0,
                                'health': 0,
                                'initiative': 0
                                }
        self.base_stats = {'str_armor': 0,
                           'free_armor': 0,
                           'strength': 0,
                           'health': 0,
                           'initiative': 0,
                           'weapon_damage': 0,
                           'str_damage_lo': None,
                           'str_damage_hi': None,
                           'abilities': []
                           }

    def apply_effects(self):
        stats = self.base_stats.copy()
        for key in ['str_armor', 'free_armor', 'strength', 'health', 'initiative', 'weapon_damage']:
            stats[key + '_multiplier'] = 1
        for effect in self.effects:
            effected = effects.effected_stats[effect]
            effected_stats = [stats[x] for x in effected]
            effected_stats = effects.run_effect(effect, 'stat', effected_stats)
            for i in range(len(effected)):
                stats[effected[i]] = effected_stats[i]

        self.effected_stats = stats

    def calculate_stats(self):
        self.apply_effects()

        for key in ['strength', 'health', 'initiative']:
            self.current_stats[key] = self.effected_stats[key] - self.resource_damage[key]

        max_str_armor = self.effected_stats['str_armor'] - self.resource_damage['armor']
        if max_str_armor < 1:
            self.current_stats['armor'] = self.effected_stats['free_armor']
        elif max_str_armor <= self.current_stats['strength']:
            self.current_stats['armor'] = self.effected_stats['free_armor'] + max_str_armor
        elif max_str_armor > self.current_stats['strength']:
            self.current_stats['armor'] = self.effected_stats['free_armor'] + self.current_stats['strength']


class Spearman(Unit):
    def __init__(self, location):
        self.str_armor = 2

tom = Spearman(('1', 1))
print(tom.str_armor)
print(tom)
