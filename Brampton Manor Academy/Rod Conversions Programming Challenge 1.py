#Rod Conversions

def ms(rodnum):
    meters = float(rodnum*5.0292)
    print(meters)

def fur(rodnum):
    furlongs = float(rodnum/40)
    print(furlongs)

def foot(rodnum):
    feet = ((rodnum*5.0292)/0.3048)
    print(feet)

def mil(rodnum):
    miles = float((rodnum*5.0292)/1609.34)
    print(miles)

def tim(rodnum):
    mins = ((rodnum*5.0292)/82.6666667)
    print(mins)

rodnum = float(input("Enter distance in rods:"))
meters = ms(rodnum)
furlongs = fur(rodnum)
feet = foot(rodnum)
miles = mil(rodnum)
minstowalk = tim(rodnum)
