unit_count = 0
turn_order = [('player', 'leader',['minions'])]
unit_dict = {}


def dynamic_unit_init(unit_type):
    unit_dict[str(unit_count)] = unit_type


class Unit:
    basic_actions = ['move', 'attack', 'rest', 'play_card']


    def __init__(self, location):
        self.location = location
        self.footprint_diameter = 1
        self.faction = None
        self.effects = {''}
        self.effected_stats = None

        self.resource_damage = {'armor_damage': 0,
                                'strength_damage': 0,
                                'health_damage': 0,
                                'used_initiative': 0
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
        stats = self.base_stats
        for effect in self.effects:


        self.effected_stats = {''}

    def calculate_stats(self):
        self.current_armor =
        self.current_strength =
        self.current_health =


class Spearman(Unit):
    def __init__(self, location):
        self.str_armor = 2

tom = Spearman()
print(tom.str_armor)
print(tom.free_armor)
