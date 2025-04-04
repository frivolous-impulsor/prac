import math

def q3():
    k = 10
    r = 0.4
    s = 0.3
    ratio1 = r/s
    ratio2 = r/(2*s)
    comp1 = (1-(ratio1)**(k+1))/(1 - ratio1)
    comp2 = ((ratio2)**(k+1))/(1 - ratio2)
    pi_0 = (comp1 + comp2)**(-1)
    
    reg1 = 509.216
    reg2 = 0.451
    expected = (reg1 + reg2) * pi_0
    print(expected)

def waysRec(i, j, waysChart: dict, c):
    if((i, j) in waysChart.keys()):
        return waysChart[(i,j)]
    
    if(i == -1):
        if j == 0:
            waysChart[(i, j)] = 1
        else:
            waysChart[(i, j)] = 0
        return waysChart[(i, j)]



    if j < c[i]:
        waysChart[(i,j)] = waysRec(i-1, j, waysChart, c)
    else:
        waysChart[(i,j)] = waysRec(i-1, j, waysChart, c) + waysRec(i, j-c[i], waysChart, c)
    return waysChart[(i,j)]
        

def waysCoin(n: int, c: list[int]):
    waysChart = dict()
    res = waysRec(len(c)-1, n, waysChart, c)
    print(res)
    

def dot(a, b):
    return a[0] * b[0] + a[1] *b[1]

def norm(a):
    return math.sqrt(dot(a, a))

def is34Q(x, y):
    return (y<0)

def getDir(x, y):
    a = [x,y]
    b = [1,0]
    if a == [0,0]:
        raise Exception("speed must be non zero")
    raw = int(math.acos(dot(a, b)/(norm(a)*norm(b)))/(2*math.pi)*360)
    if is34Q(x,y):
        return 360-raw
    return raw

def reverse(speedX, speedY):
    speed = int(math.sqrt(speedX**2 + speedY**2))
    direction = getDir(speedX, speedY)
    print("original:")
    print(f"speedX: {speedX}")
    print(f"speedY: {speedY}")
    print(f"speed: {speed}")
    print(f"direction: {direction}")

    speedX = -speedX
    speedY = -speedY
    direction = getDir(speedX, speedY)

    print("\nafter calling reverse():")
    print(f"speedX: {speedX}")
    print(f"speedY: {speedY}")
    print(f"speed: {speed}")
    print(f"direction: {direction}")

def reverseX(speedX, speedY):
    speed = int(math.sqrt(speedX**2 + speedY**2))
    direction = getDir(speedX, speedY)
    print("original:")
    print(f"speedX: {speedX}")
    print(f"speedY: {speedY}")
    print(f"speed: {speed}")
    print(f"direction: {direction}")

    speedX = -speedX
    direction = getDir(speedX, speedY)

    print("\nafter calling reverse():")
    print(f"speedX: {speedX}")
    print(f"speedY: {speedY}")
    print(f"speed: {speed}")
    print(f"direction: {direction}")

def q1():
    inputList = [[0,20], [-20, 0], [-30, -100], [1, 1], [50,-50]]
    count = 1
    for input in inputList:
        print(count)
        reverseX(input[0], input[1])
        count+=1
        print('\n')
q1()