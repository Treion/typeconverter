print("▄▄▄▄▄ ▄· ▄▌ ▄▄▄·▄▄▄ .     ▄▄·        ▐ ▄  ▌ ▐·▄▄▄ .▄▄▄  ▄▄▄▄▄▄▄▄ .▄▄▄  ")
print("•██  ▐█▪██▌▐█ ▄█▀▄.▀·    ▐█ ▌▪▪     •█▌▐█▪█·█▌▀▄.▀·▀▄ █·•██  ▀▄.▀·▀▄ █·")
print(" ▐█.▪▐█▌▐█▪ ██▀·▐▀▀▪▄    ██ ▄▄ ▄█▀▄ ▐█▐▐▌▐█▐█•▐▀▀▪▄▐▀▀▄  ▐█.▪▐▀▀▪▄▐▀▀▄ ")
print(" ▐█▌· ▐█▀·.▐█▪·•▐█▄▄▌    ▐███▌▐█▌.▐▌██▐█▌ ███ ▐█▄▄▌▐█•█▌ ▐█▌·▐█▄▄▌▐█•█▌")
print(" ▀▀▀   ▀ • .▀    ▀▀▀     ·▀▀▀  ▀█▄▀▪▀▀ █▪. ▀   ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀ .▀  ▀")
print()

def inputingValue():
    print("     ┌───┬───────────┐")
    print("     │ s │ string    │")
    print("     │ i │ integer   │")
    print("     │ f │ float     │")
    print("     │ b │ boolean   │")
    print("     │ c │ character │")
    print("     └───┴───────────┘")
    print()
    startInput = input("From the table above,\nselect the data-type you would like to input: ").lower()
    print()
    if startInput == "s":
        value = input("YOU ARE ENTERING A STRING VALUE \nEnter a string: ")
    elif startInput == "i":
        value = int(input("YOU ARE ENTERING AN INTEGER VALUE \nEnter a number: "))
    elif startInput == "f":
        value = float(input("YOU ARE ENTERING A FLOAT VALUE \nEnter a number: "))
    elif startInput == "b":
        while True:
            x = input("YOU ARE ENTERING A BOOLEAN VALUE \nEnter True or False: ").lower()
            if x == "true":
                value = True
                break
            elif x == "false":
                value = False
                break
            else:
                print("Invalid input. Please enter either True or False.")
                print("")
    elif startInput == "c":
        value = input("YOU ARE ENTERING A CHARACTER VALUE \nEnter a character: ")[0]
    else:
        print("Input Error: Invalid data-type selected.")
        return "Close"
    print("A", type(value), "value has been successfully stored.\n")
    return value

inputValue = inputingValue()

if inputValue != "Close":
    print("")
    print("     ┌───┬───────────┐")
    print("     │ s │ string    │")
    print("     │ i │ integer   │")
    print("     │ f │ float     │")
    print("     │ b │ boolean   │")
    print("     │ c │ character │")
    print("     └───┴───────────┘")
    print("")
    convertInput = input("From the table above,\nselect the data-type you want to convert the value to: ").lower()
    print()
    try:
        if convertInput == "s":
            inputValue = str(inputValue)
        elif convertInput == "i":
            inputValue = int(inputValue)
        elif convertInput == "f":
            inputValue = float(inputValue)
        elif convertInput == "b":
            if str(inputValue).lower() == "true":
                inputValue = True
            elif str(inputValue).lower() == "false":
                inputValue = False
            else:
                raise ValueError("Cannot convert to boolean.")
        elif convertInput == "c":
            inputValue = str(inputValue)[0]
        else:
            print("Conversion Error: Invalid type selected.")
            exit()

        print("Successfully converted! New value:", inputValue, "| Type:", type(inputValue))

    except ValueError as x:
        print("Conversion Failed:", x)
