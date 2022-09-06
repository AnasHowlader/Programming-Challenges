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
meters = "Meters: " + str(rods_to_meters(rodnum))
furlongs = "Furlongs: " + str(furlongs_to_rods(rodnum))
feet = "Feet: " + str(feet_to_meters(rodnum))
miles = "Miles: " + str(miles_to_meters(rodnum))
minstowalk = "Minutes to walk: " + str(minutes_to_walk(rodnum))
print(meters)
print(furlongs)
print(feet)
print(miles)
print(minstowalk)

