x: float
y: float
def getZ(x: float, y: float):
    return x + y/x

def getFlow(x, y):
    deno = (x)
    if deno > 0.0001:
        return ("+")
    elif deno < 0.0001:
        return ("-")
    else:
        return ("0")

def grabInfo(x, y):
    print(getZ(x,y))
    print(getFlow(x,y))

grabInfo(-0.5,-3)