class Windchill:
    def __init__(self, air_temperature, wind_speed):
        self.air_temperature = air_temperature
        self.wind_speed = wind_speed


    def WindChillCalculation(self):
        wind_chill = 35.74 + 0.6215 * float(self.air_temperature) - 35.75 * float(self.wind_speed) ** 0.16 + 0.4275 * float(
        self.air_temperature) * float(self.wind_speed) ** 0.16
        return wind_chill

air_temp_input = float(input("Enter an air temperature: "))
air_speed_input = float(input("Enter an air speed: "))

air_temperatures = [10,0,-15]
wind_speeds = [15,25,35]

result = Windchill(air_temp_input, air_speed_input)
final_wind_chill = result.WindChillCalculation()
outcome = f"Temperature = {air_temp_input} and Wind Speed = {air_speed_input}, therefore the wind chill is: {final_wind_chill}"

print(f"Temperature of {air_temperatures[0]} and speed of {wind_speeds[0]} gives a wind chill of: {Windchill(10, 15).WindChillCalculation()}")
print(f"Temperature of {air_temperatures[1]} and speed of {wind_speeds[1]} gives a wind chill of: {Windchill(0, 25).WindChillCalculation()}")
print(f"Temperature of {air_temperatures[2]} and speed of {wind_speeds[2]} gives a wind chill of: {Windchill(-10, 35).WindChillCalculation()}")
print(outcome)

