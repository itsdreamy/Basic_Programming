print("Welcome to Temperature Converter!")
celcius = float(input("Please enter the temperature in celcius: "))

fahrenheit = (celcius * (9/5)) + 32
kelvin = celcius + 273.15

print(f"{celcius} C is {fahrenheit} F")
print(f"{celcius} C is {kelvin} K")