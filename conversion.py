# This program/script perform usual conversion.


# function Choosing a conversion category (distance, flow, volume, Area, pressure, Liquid Flow, Speed, Gas Flow)
def conversion_cat():
    while True:
        print("welcome !")
        print("Choose a category from the list below? Enter corresponding number")
        print("1. Distance \n2. Area \n3. Volume \n4. Pressure \n5. Speed \n6. Mass \n7. Liquid Flow \n8. Gas Flow")
        conversion_choice = input()
        if conversion_choice.isnumeric() and len(conversion_choice) == 1 and 0 < int(conversion_choice) < 9:
            return int(conversion_choice)
        else:
            continue


# Function to get value to convert from user
def value_to_convert():
    while True:
        print("Enter value to convert: ")
        value_entered = input()
        if value_entered.isnumeric():
            value_entered = int(value_entered)
            return float(value_entered)
        else:
            continue


# Function to prompt user to enter a distance unit from a pool of predefined units
def choose_unit(category_choice):
    distance_units_dict = {1: "mm", 2: "in", 3: "cm", 4: "m", 5: "km", 6: "mi", 7: "ft", 8: "yd"}
    area_units_dict = {1: "hectare", 2: "sqmi", 3: "km2", 4: "acre", 5: "m2", 6: "sqft", 7: "ft2", 8: "sqi",
                       9: "in2", 10: "sqyd", 11: "yd2"}
    volume_units_dict = {1: "m3", 2: "bbl", 3: "l", 4: "cuft", 5: "gal", 6: "qt"}
    pressure_units_dict = {1: "Mpa", 2: "atm", 3: "bar", 4: "pa", 5: "psi"}
    speed_units_dict = {1: "mph", 2: "kmh", 3: "ft/s", 4: "m/s", 5: "knot"}
    mass_units_dict = {1: "t", 2: "kg", 3: "g", 4: "lbs", 5: "oz", 6: "mg"}
    liqflow_units_dict = {1: "bpd", 2: "bph", 3: "bpm", 4: "gph", 5: "gpm", 6: "l/h", 7: "m3h", 8: "m3d", 9: "l/s"}
    gasflow_units_dict = {1: "mscfd", 2: "scfh", 3: "scfm", 4: "cf/d", 5: ""}

    if category_choice == 1:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Distance : mm, in, cm, m, km, mi, ft, yd")
            unit = input()
            for item in distance_units_dict.keys():
                if unit.isalpha() and distance_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 2:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Area : acre, m2, ft2 (square foot), km2, hectare, yd2 (square yard), "
                  "sqmi (square mile), in2 (square inch)")
            unit = input()
            for item in area_units_dict.keys():
                if area_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 3:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Volume : m3, bbl (for us Barrel), l, cuft, gal (for us gallon), qt")
            unit = input()
            for item in volume_units_dict.keys():
                if volume_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 4:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Pressure : Mpa, atm (standard atmosphere), bar, pa, psi")
            unit = input()
            for item in pressure_units_dict.keys():
                if pressure_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 5:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Speed : mph, kmh, ft/s, m/s, knot")
            unit = input()
            for item in speed_units_dict.keys():
                if speed_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 6:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Mass : t, kg, g, lbs, oz, mg")
            unit = input()
            for item in mass_units_dict.keys():
                if mass_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 7:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Liquid Flow : bpd (bbls/day), bph (bbls/hour), bpm, gph, gpm, l/h, m3h, m3d, l/s")
            unit = input()
            for item in liqflow_units_dict.keys():
                if liqflow_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue

    if category_choice == 8:
        while True:
            print("Enter unit: (choose/type from the list/table below): ")
            print("Gas Flow : mscfd (million standard cubic feet per day), scfh, scfm")
            unit = input()
            for item in gasflow_units_dict.keys():
                if gasflow_units_dict[item] == unit:
                    return str(unit)
                else:
                    continue


# Function performing distance conversion
def distance(u_from, val, u_to):
    metric_dict = {
        'Em': 1000000000000000000,
        'Pm': 1000000000000000,
        'Tm': 1000000000000,
        'Gm': 1000000000,
        'Mm': 1000000,
        'km': 1000,
        'hm': 100,
        'dam': 10,
        'm': 1,
        'dm': .1,
        'cm': .01,
        'mm': .001,
        'μm': .000001,
        'nm': .000000001,
        'pm': .000000000001,
        'fm': .000000000000001,
        'am': .000000000000000001
    }
    imperial_dist_dict = {
        'lea': 190080,
        'mi': 63360,
        'fu': 7920,
        'ch': 792,
        'rod': 198,
        'yd': 36,
        'ft': 12,
        'li': 7.92,
        'in': 1,
        'th': .001
    }

    if u_from in metric_dict and u_to in imperial_dist_dict:
        metric_base = metric_dict.get(u_from, None)
        imperial_base = imperial_dist_dict.get(u_to, None)
        converted_val = val * metric_base * 39.3701 * imperial_base
        return str(round(converted_val, 5))

    elif u_from in imperial_dist_dict and u_to in metric_dict:
        imperial_base = imperial_dist_dict.get(u_from, None)
        metric_base = metric_dict.get(u_to, None)
        converted_val = val * imperial_base * .0254 / metric_base
        return str(round(converted_val, 5))

    elif u_from in metric_dict and u_to in metric_dict:
        metric_from = metric_dict.get(u_from, None)
        metric_to = metric_dict.get(u_to, None)
        converted_val = val * metric_from / metric_to
        return str(round(converted_val, 5))

    elif u_from in imperial_dist_dict and u_to in imperial_dist_dict:
        imp_from = imperial_dist_dict.get(u_from, None)
        imp_to = imperial_dist_dict.get(u_to, None)
        converted_val = val * imp_from / imp_to
        return str(round(converted_val, 5))


def area(u_from, val, u_to):
    area_dict = {
        'hectare': 10000,
        'sqmi': 2.59e+6,
        'km2': 1e+6,
        'acre': 4046.86,
        'm2': 1,
        'sqft': 0.092903, 'ft2': 0.092903,
        'sqi': 0.00064516, "in2": 0.00064516,
        'sqyd': 0.836127, 'yd2': 0.836127,
    }

    uni_from = area_dict.get(u_from, None)
    uni_to = area_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


def volume(u_from, val, u_to):
    volume_dict = {
        'cbm': 33814, 'cum': 33814, 'm3': 33814, 'm^3': 33814, 'm**3': 33814,
        'bbl': 5376, 'bbls': 5376, 'oil_bbl': 5376,
        'l': 33.814,
        'cuft': 957.506, 'cft': 957.506, 'ft**3': 957.506, 'ft^3': 957.506,
        'gal': 128, 'us_gal': 128,
        'qt': 32,
        'pt': 16,
        'cp': 8.11537, 'cup': 8.11537,
        'gi': 4,
        'oz': 1,
        'cuinch': 0.554113, 'cinch': 0.554113, 'inch**3': 0.554113, 'inch^3': 0.554113, 'ci': 0.554113,
        'ml': 0.033814,
        'tsp': 0.166667,
        'tbsp': .5,
    }

    uni_from = volume_dict.get(u_from, None)
    uni_to = volume_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


def pressure(u_from, val, u_to):
    pressure_dict = {
        'Mpa': 1000000,
        'atm': 101325,
        'bar': 100000,
        'pa': 1,
        'psi': 6894.76
    }

    uni_from = pressure_dict.get(u_from, None)
    uni_to = pressure_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


def speed(u_from, val, u_to):
    speed_dict = {
        'mph': 0.44704,
        'kmh': 0.277778,
        'ft/s': 0.3048,
        'm/s': 1,
        'knot': 0.514444
    }

    uni_from = speed_dict.get(u_from, None)
    uni_to = speed_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


def mass(u_from, val, u_to):
    mass_dict = {
        't': 1e+6,
        'kg': 1000,
        'lbs': 453.592,
        'oz': 28.3495,
        'g': 1,
        'mg': 0.001
    }

    uni_from = mass_dict.get(u_from, None)
    uni_to = mass_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


def liquidflow(u_from, val, u_to):
    lflow_dict = {
        'bph': 0.7,
        'bpd': 0.02917,
        'bpm': 42,
        'gph': 0.01667,
        'gpm': 1,
        'l/h': 0.004403,
        'm3h': 4.4029,
        'm3d': 0.1835,
        'l/s': 15.8503
    }

    uni_from = lflow_dict.get(u_from, None)
    uni_to = lflow_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


def gasflow(u_from, val, u_to):
    gasflow_dict = {
        'mscfd': 1179.868608,
        'scfh': 0.028,
        'scfm': 1.70,
        'm3/h': 1
    }

    uni_from = gasflow_dict.get(u_from, None)
    uni_to = gasflow_dict.get(u_to, None)
    converted_val = val * uni_from / uni_to
    return str(round(converted_val, 5))


# Main body of the code I call my functions here to perform the conversion
category = conversion_cat()
if category == 1:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = distance(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 2:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = area(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 3:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = volume(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 4:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = pressure(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 5:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = speed(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 6:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = mass(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 7:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = liquidflow(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))

elif category == 8:
    unit_from = choose_unit(category)
    value = value_to_convert()
    unit_to = choose_unit(category)
    result = gasflow(unit_from, value, unit_to)
    print("{} {} is equal to {} {}".format(value, unit_from, result, unit_to))
