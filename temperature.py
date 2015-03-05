# Convert degrees celsius to fahrenheit

while 1:
    inp = input("1: C -> F\n2: F -> C\n3: exit\n")

    if inp == 3:
        break

    temp = input("What's the temperature? ")    

    if inp == 2:
        out = (5.0 * temp - 160.0) / 9.0
    elif inp == 1:
        out = 9.0 / 5.0 * temp + 32.0

    print out, "\n"
