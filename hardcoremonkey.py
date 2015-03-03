import random
import string

script = open('Hamlet.txt', 'r')
text = script.read()
script.close()

monkeyTyped = ''
lengthRecord = 0

while len(monkeyTyped) < len(text) - 1:
    monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + ' '))
    if monkeyTyped[len(monkeyTyped) - 1] == text[len(monkeyTyped) - 1]:
        if len(monkeyTyped) > lengthRecord:
            print monkeyTyped
            lengthRecord = len(monkeyTyped)
    else:
        monkeyTyped = ''
print "Done. I'll get myself a banana."
