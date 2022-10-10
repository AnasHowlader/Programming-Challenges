air_temp = [10,0,-10]
air_speed = [15,25,35]

def wind_chill_calculation(air_temp, air_speed):
    wind_chill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return wind_chill

x = 0
y = 0
while x < 3:
    while y < 3:
        print(f"The wind chill for the temp of {air_temp[x]} and air speed of {air_speed[y]} is {(wind_chill_calculation(air_temp[x],air_speed[y]))}")
        x+=1
        y+=1

air_temp_input = float(input("Enter an air temperature: "))
air_speed_input = float(input("Enter an air speed: "))

result = wind_chill_calculation(air_temp_input, air_speed_input)
print(result)