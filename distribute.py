def get_input():
    items = []
    print (
        "Enter the runtimes of your files in the order you plan on watching"
        " them.\nOptionally you can add the number of times an episode of the "
        "same length\nappears. Type \"done\" or press enter again to finish."
    )
    while True:
        input = raw_input("> ")
        if input == "done" or input == "": break
        components = input.split(" ")
        if len(components) == 1: components.append(1)
        items += [int(components[0]) for i in range(int(components[1]))]

    print "\nIn how many days do you want to watch them?"
    days = int(raw_input("> "))
    average = sum(items) / days
    print "\nOn average you can watch", average, "minutes per day."

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

def show_list(daylist):
    for i, day in enumerate(daylist):
        print "Day", i + 1, ":",
        for item in day: print item,
        print

if __name__ == "__main__":
    items, average = get_input()
    daylist = distribute(items, average)
    show_list(daylist)
