import random
import string

script = open('Hamlet.txt', 'r')
text = script.read()
script.close()

monkeyTyped = ''

while len(monkeyTyped) < len(text):
    monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + ' '))
    if monkeyTyped[len(monkeyTyped) - 1] == text[len(monkeyTyped) - 1]:
        print monkeyTyped
    else:
        monkeyTyped = monkeyTyped[:-1]

print "Done. I'll get myself a banana."
