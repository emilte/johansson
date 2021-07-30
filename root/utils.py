
def getIndexOfTuple(tuplelist, index, value):
    for i, tuple in enumerate(tuplelist):
        if tuple[index] == value:
            return i
    return None
