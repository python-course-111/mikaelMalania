# temperature converter from celcius to fahrenheit

temp = float(input("Enter temperature: "))
temp_type = input("Enter temperature type (C/F): ")

if temp_type == "C":
    temp = (temp * 9/5) + 32
    print("Temperature in fahrenheit:", temp)
elif temp_type == "F":
    temp = (temp - 32) * 5/9
    print("Temperature in celcius:", temp)
