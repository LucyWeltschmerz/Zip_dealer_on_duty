
def temp_converter():
    """
    Create a Python program that converts temperatures between Celsius and Fahrenheit. The program  should:
    1. Ask the user to enter a temperature value.
    2. Ask the user to specify the input temperature scale (Celsius or Fahrenheit).
    3. Ask the user to specify the desired output temperature scale (Celsius or Fahrenheit).
    4. Convert the temperature to the desired scale and display the result.

    For example:
    Enter temperature: 32
    Is this temperature in Celsius or Fahrenheit? (C/F): F
    Convert to Celsius or Fahrenheit? (C/F): C

    Result: 0.0 degrees Celsius

    """
    temp = int(input("Enter temperature: "))
    f_or_c = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    convert_to = input("Convert to Celsius or Fahrenheit? (C/F): ").upper()

    if f_or_c == 'F' and convert_to == 'C':
        temp_in_celsius = (temp - 32) * 5 / 9
        print(f'Result: {temp_in_celsius} degrees Celsius')
    elif f_or_c == 'C' and convert_to == 'F':
        temp_in_fahrenheit = (temp * 9/5) + 32
        print(f'Result: {temp_in_fahrenheit} degrees Fahrenheit')


temp_converter()
