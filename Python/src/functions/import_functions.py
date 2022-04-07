def remove_newline(list):
    toreturn = []
    for i in list:
        toreturn.append(i.replace("\n", ""))
    return toreturn


def load_file(filename):
    f = open(filename, "r")
    toreturn = f.readlines()
    f.close()
    return remove_newline(toreturn)
