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


res = waysCoin(4, [1,5,10])
res = waysCoin(6, [1,5,10])
res = waysCoin(10, [1,5,10])
res = waysCoin(14, [1,5,10])
res = waysCoin(20, [1,5,10])
