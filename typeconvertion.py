print("▄▄▄▄▄ ▄· ▄▌ ▄▄▄·▄▄▄ .     ▄▄·        ▐ ▄  ▌ ▐·▄▄▄ .▄▄▄  ▄▄▄▄▄▄▄▄ .▄▄▄  ")
print("•██  ▐█▪██▌▐█ ▄█▀▄.▀·    ▐█ ▌▪▪     •█▌▐█▪█·█▌▀▄.▀·▀▄ █·•██  ▀▄.▀·▀▄ █·")
print(" ▐█.▪▐█▌▐█▪ ██▀·▐▀▀▪▄    ██ ▄▄ ▄█▀▄ ▐█▐▐▌▐█▐█•▐▀▀▪▄▐▀▀▄  ▐█.▪▐▀▀▪▄▐▀▀▄ ")
print(" ▐█▌· ▐█▀·.▐█▪·•▐█▄▄▌    ▐███▌▐█▌.▐▌██▐█▌ ███ ▐█▄▄▌▐█•█▌ ▐█▌·▐█▄▄▌▐█•█▌")
print(" ▀▀▀   ▀ • .▀    ▀▀▀     ·▀▀▀  ▀█▄▀▪▀▀ █▪. ▀   ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀ .▀  ▀")
print("")
print("     ┌───┬───────────┐")
print("     │ s │ string    │")
print("     │ i │ integer   │")
print("     │ f │ float     │")
print("     │ b │ boolean   │")
print("     │ c │ character │")
print("     └───┴───────────┘")
print("")

startInput = input("From the following table above,\nselect the data-type you would like to input: ").lower()
print("")

if startInput == "s":
    inputvalue = input("YOU ARE ENTERING A STRING VALUE \nEnter a string: ")
elif startInput == "i":
    inputvalue = int(input("YOU ARE ENTERING AN INTEGER VALUE \nEnter a number: "))
elif startInput == "f":
    inputvalue = float(input("YOU ARE ENTERING A FLOAT VALUE \nEnter a number: "))
elif startInput == "b":
    while True:
        inputvalue = input("YOU ARE ENTERING A BOOLEAN VALUE \nEnter True or False: ").lower()
        if inputvalue == "true":
            inputvalue = True
            break
        elif inputvalue == "false":
            inputvalue = False
            break
        else:
            print("You have to input either True or False")
elif startInput == "c":
    inputvalue = input("YOU ARE ENTERING A CHARACTER VALUE \nEnter a character: ")[0]
else:
    print("Input Error: Invalid data-type selected.")
    exit()

print("A", type(inputvalue), "value has been successfully stored.")
print(inputvalue)
