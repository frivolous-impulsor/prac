import math
import itertools

miu1 = 5
miu2 = 10
miu3 = 10
miu4 = 1

miu_list = [miu1, miu2, miu3, miu4]

lam1 = 1
lam2 = 0.5
lam3 = 0.5
lam4 = 0.1
sumLam = lam1+lam2+lam3+lam4
lam_list = [lam1, lam2, lam3, lam4]

p1 = lam1/sumLam
p2 = lam2/sumLam
p3 = lam3/sumLam
p4 = lam4/sumLam

p_list = [p1, p2, p3, p4]

def lam_M(R_list, M):
    sum = 0
    for i in range(len(R_list)):
        sum += (p_list[i] * R_list[i])
    return M/sum



def R_i_M(i, preR_list, preLam):
    result = 1/miu_list[i]
    result += ((p_list[i] * preLam*preR_list[i])/miu_list[i])
    return result


def findR(iteration):
    if(iteration < 2):
        result = []
        for i in range(4):
            result.append(R_i_M(i, [0,0,0,0], 0));
        return result
    else:
        result = []

        preR = findR(iteration-1)
        print(preR)
        lam = lam_M(preR, iteration-1)
        print(lam)
        for i in range(4):
            R_i = R_i_M(i, preR, lam)
            result.append(R_i)
        return result

def q1():
    R_list = [0.5676767676767677, 0.12626262626262627, 0.12626262626262627, 1.6363636363636362]
    V_list = [1.111, 0.556, 0.556, 0.111]
    sum = 0
    for i in range(4):
        sum+= (R_list[i]*V_list[i])
    print(4/sum)

def q2():
    possibleStates = [[]]

def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a,b in zip((-1,)+c,c+(n+k-1,))]


def q1b():
    states = list(partitions(4,4))

    targetStates = []
    for state in states:
        if(state[3] == 2):
            targetStates.append(state)

    sum = 0
    for state in states:
        stateProduct = 1
        for i in range(4):
            stateProduct = stateProduct* (lam_list[i]/miu_list[i])**(state[i])
        sum += stateProduct

    c = sum**(-1)

    probTotal = 0
    for state in targetStates:
        product = 1
        for i in range(4):
            product *= ((lam_list[i]/miu_list[i])**(state[i]))
        product *=c
        probTotal += product
    print(f"p = {probTotal}")


    print(f"c = {c}")

