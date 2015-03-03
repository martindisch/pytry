import random
import string

script = open('Hamlet.txt', 'r')
text = script.read()
script.close()

monkeyTyped = ''
lengthRecord = 0
strokes = 0

while len(monkeyTyped) < len(text) - 1:
    monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + ' '))
    strokes = strokes + 1
    if monkeyTyped[len(monkeyTyped) - 1] == text[len(monkeyTyped) - 1]:
        if len(monkeyTyped) > lengthRecord:
            print monkeyTyped
            lengthRecord = len(monkeyTyped)
    else:
        monkeyTyped = ''
    
    if strokes % 100000 == 0:
        print text[0:lengthRecord] + '\nafter ' + str(strokes) + ' keystrokes'
print "Done. I'll get myself a banana."
