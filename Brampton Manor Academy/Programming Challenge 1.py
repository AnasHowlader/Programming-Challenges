#Rod Conversions

def rods_to_meters(rodnum):
    return float(rodnum*5.0292)

def furlongs_to_rods(rodnum):
    return float(rodnum/40)


def feet_to_meters(rodnum):
    return ((rodnum*5.0292)/0.3048)


def miles_to_meters(rodnum):
    return float((rodnum*5.0292)/1609.34)


def minutes_to_walk(rodnum):
    return ((rodnum*5.0292)/82.6666667)


rodnum = float(input("Enter distance in rods:"))
meters = f"Meters:   {(rods_to_meters(rodnum))}"
furlongs = f"Furlongs:   {(furlongs_to_rods(rodnum))}"
feet = f"Feet:  {(feet_to_meters(rodnum))}"
miles = f"Miles:  {(miles_to_meters(rodnum))}"
minstowalk = f"Minutes to walk:  {(minutes_to_walk(rodnum))}"
print(meters)
print(furlongs)
print(feet)
print(miles)
print(minstowalk)

