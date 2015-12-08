while True:
    files = []
    while True:
        filename = raw_input("File to read ('done' to finish, 'exit' to leave)\n")
        if filename == "done":
            break
        if filename == "exit":
            exit()
        files.append(filename)
    print ""
    if len(files) > 0:
        multiples = open(files[0]).read().splitlines()
        files.pop(0)
        for f in files:
            content = open(f).read().splitlines()
            multiples = set(content).intersection(set(multiples))
        
        for item in multiples:
            print item
    print ""