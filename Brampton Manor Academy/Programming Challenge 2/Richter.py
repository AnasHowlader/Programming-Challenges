
def magnitude(richter_value):
    return float(10**((1.5*richter_value)+4.8))


richter_value = float(input("Enter an richter value:"))
your_richter_value = f"Your richter value has an energy release of  {(magnitude(richter_value))}"
print(your_richter_value)


values = [1,5,9.1,9.2,9.5]
for value in values:
    print(f"Energy released for a magnitude of {value}: {magnitude(value)/(4.184*10**9)} Joules")