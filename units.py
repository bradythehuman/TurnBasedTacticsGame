# Used to turn units.csv into a list of dictionaries. 1 dictionary for each unit
def init_units_dict(path):
    with open(path, 'r') as f:
        lines_string = f.readlines()

        lines = []
        for line in lines_string:
            line = line.rstrip('\n')
            lines.append(line.split(','))

        units = []
        for line in lines[1:]:
            unit = {}
            for i in range(0, len(line)):
                key = lines[0][i]
                value = line[i]
                try:
                    unit[key] = int(value)
                except ValueError:
                    if ';' in value:
                        unit[key] = value.split(';')
                    else:
                        unit[key] = value
            units.append(unit)
    return units

