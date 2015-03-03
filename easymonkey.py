import random
import string

script = open('Hamlet.txt', 'r')
text = script.read()
script.close()

monkeyTyped = ''
strokes = 0

while len(monkeyTyped) < len(text) - 1:
    monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + ' '))
    strokes = strokes + 1
    if monkeyTyped[len(monkeyTyped) - 1] == text[len(monkeyTyped) - 1]:
        if len(monkeyTyped) % 1000 == 0:
            print 'Monkey typed ' + str(len(monkeyTyped)) + ' correct characters after ' + str(strokes) + ' keystrokes'
    else:
        monkeyTyped = monkeyTyped[:-1]
print "Done. I'll get myself a banana."
