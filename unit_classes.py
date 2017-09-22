unit_count = 0
unit_dict = {}


def dynamic_unit_init(unit_type):
    unit_dict[str(unit_count)] = unit_type



class Unit:
    def __init__(self, location):
        self.location = location
