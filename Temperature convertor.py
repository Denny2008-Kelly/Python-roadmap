unit = input("Enter the unit of temperature(C,K,F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    funit = input("Enter the converted temperature unit(K,F): ").upper()
    print(funit)
    if funit == "K":
        ftemp = temp + 273
        print(round(ftemp, 2))
    elif funit == "F":
        ftemp = (temp*1.8) + 32
        print(round(ftemp, 2))
    else:
        print(f"{funit}is an invalid unit")

elif unit == "K":
    funit = input("Enter the converted temperature unit(C,F): ").upper()
    print(funit)
    if funit == "C":
        ftemp = temp - 273
        print(round(ftemp, 2))
    elif funit == "F":
        ftemp = ((temp-273)*1.8) + 32
        print(round(ftemp, 2))
    else:
        print(f"{funit}is an invalid unit")

elif unit == "F":
    funit = input("Enter the converted temperature unit(C,K): ").upper()
    print(funit)
    if funit == "C":
        ftemp = (temp-32)/1.8
        print(round(ftemp, 2))
    elif funit == "K":
        ftemp = ((temp-32)/1.8)+273
        print(round(ftemp, 2))
    else:
        print(f"{funit} is an invalid unit")

else:
    print(f"{unit} is an invalid unit")