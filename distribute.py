def get_input():
    items = []
    print (
        "Enter the runtimes of your files in the order you plan on watching"
        " them.\nOptionally you can add the number of times an episode of the "
        "same length\nappears. Type \"done\" or press enter again to finish."
    )
    while True:
        inp = input("> ")
        if inp == "done" or inp == "": break
        components = inp.split(" ")
        if len(components) == 1: components.append(1)
        items += [int(components[0]) for i in range(int(components[1]))]

    print("\nIn how many days do you want to watch them?")
    days = int(input("> "))
    average = int(sum(items) / days)
    print("\nOn average you can watch", average, "minutes per day.")

    return items, average

def distribute(items, average):
    diff, temp, daylist = 0, [], []
    while len(items) > 0:
        temp.append(items.pop(0))
        if sum([diff] + temp) > average or len(items) == 0:
            dLess = diff + sum(temp[:-1]) - average
            dMore = diff + sum(temp) - average
            if abs(dLess) < abs(dMore) and len(temp[:-1]) > 0:
                diff = dLess
                daylist.append(temp[:-1])
                items = temp[-1:] + items
            else:
                diff = dMore
                daylist.append(temp)
            temp = []

    return daylist

def show_list(daylist, average):
    cgreen, cred, cend = '\033[92m', '\033[91m', '\033[0m'
    s_daylist = [[str(d) for d in day] for day in daylist]
    s = "Day {0}: {1}"
    lines = [s.format(i + 1, " ".join(day)) for i, day in enumerate(s_daylist)]
    maxlen = max([len(line) for line in lines])
    for i, line in enumerate(lines):
        color = cgreen if sum(daylist[i]) - average >= 0 else cred
        diff = str(int(sum(daylist[i]) - average))
        lines[i] += color + diff.rjust(8 + maxlen - len(line)) + cend
    print("\n".join(lines))

if __name__ == "__main__":
    items, average = get_input()
    daylist = distribute(items, average)
    show_list(daylist, average)
