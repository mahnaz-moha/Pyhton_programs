temperature = input('Celsius (1) or Fahrenheit (2)')
base = int(input("How's the weather? "))
if temperature == '1':
    celsius_to_fahrenheit = (base * 9 / 5) + 32
    print(f'it is now {celsius_to_fahrenheit} Fahrenheit.')
elif temperature == '2':
    fahrenheit_to_celsius = (base - 32) * 5 / 9
    print(f'it is now {fahrenheit_to_celsius} degrees.')