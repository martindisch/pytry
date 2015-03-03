import random
import string

script = open('Hamlet.txt', 'r')
text = script.read()
script.close()

monkeyTyped = ''

while len(monkeyTyped) < len(text) - 1:
    monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + ' '))
    if monkeyTyped[len(monkeyTyped) - 1] == text[len(monkeyTyped) - 1]:
        if len(monkeyTyped) % 100 == 0:
            print 'Monkey typed ' + str(len(monkeyTyped)) + ' characters'
    else:
        monkeyTyped = monkeyTyped[:-1]
print "Done. I'll get myself a banana."
