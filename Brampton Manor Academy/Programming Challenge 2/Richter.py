
def magnitude(richter_value):
    return float(10**((1.5*richter_value)+4.8))

def tons_of_tnt(richter_value):
    return float((magnitude(richter_value))/(4.184*10**9))

def tons_of_tnt(richter_value_1):
    return float((magnitude(richter_value_1))/(4.184*10**9))

def tons_of_tnt(richter_value_5):
    return float((magnitude(richter_value_5))/(4.184*10**9))

def tons_of_tnt(richter_value_91):
    return float(float(magnitude(richter_value_91))/(4.184*10**9))

def tons_of_tnt(richter_value_92):
    return float(float(magnitude(richter_value_92))/(4.184*10**9))

def tons_of_tnt(richter_value_95):
    return float(float(magnitude(richter_value_95))/(4.184*10**9))

richter_value = float(input("Enter an richter value:"))
your_richter_value = "Your richter value has an energy release of " + str(magnitude(richter_value))
print(your_richter_value)

richter_value_1 = "Richter Value 1 = " + str(magnitude(1))
print(richter_value_1)

richter_value_5 = "Richter Value 5 = " + str(magnitude(5))
print(richter_value_5)

richter_value_91 = "Richter Value 9.1 = " + str(magnitude(9.1))
print(richter_value_91)

richter_value_92 = "Richter Value 9.2 = " + str(magnitude(9.2))
print(richter_value_92)

richter_value_95 = "Richter Value 9.5 = " + str(magnitude(9.5))
print(richter_value_95)


print("Energy released for a magnitude of 1: " + str(magnitude(1)/(4.184*10**9)))
print("Energy released for a magnitude of 5: " + str(magnitude(5)/(4.184*10**9)))
print("Energy released for a magnitude of 9.1: " + str(magnitude(9.1)/(4.184*10**9)))
print("Energy released for a magnitude of 9.2: " + str(magnitude(9.2)/(4.184*10**9)))
print("Energy released for a magnitude of 9.5: " + str(magnitude(9.5)/(4.184*10**9)))
