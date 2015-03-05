# Read numbers and then calculate the arithmetic medium

total = 0
count = 0

while 1:
    inp = input("Give me a number: ")
    
    if inp == 0:
        break

    count += 1    
    total += inp

if count != 0:
    print str(total / count)
