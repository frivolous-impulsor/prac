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

def q2b():
    lam = 10
    miu = 11
    c = 2

    pi_0 = (1 + (lam/miu) + 0.5 * (lam/miu)**2*(1/(1-lam/(2*miu))))**(-1)
    #print(pi_0)

    pi_1 = lam/miu*pi_0
    #print(pi_1)
    result2 = 10*(1 - pi_1 - pi_0)
    print(result2)

def q2c():
    lam = 10
    miu = 11
    c = 3
    pi_0 = (1 + lam/miu + 0.5*(lam/miu)**2 + 1/6*(lam/miu)**3*(1/(1-lam/(3*miu))))**(-1)
    #print(pi_0)
    pi_1 = lam/miu*pi_0
    #print(pi_1)
    pi_2 = 1/2*(lam/miu)**2*pi_0
    #print(pi_2)

    result3 = 10*(1-pi_0 - pi_1 - pi_2)
    print(result3)

def q2d(x):
    cost1 = 9.091 + x
    cost2 = 2.841 + 2*x
    cost3 = 0.718 + 3*x

    print(cost1)
    print(cost2)
    print(cost3)

def q3():
    mean1 = 3/666.667
    rate1 = 222.222
    rate2 = 1/(4.5*10**(-3))
    print(1/(222.222-10))
q3()