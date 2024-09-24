class LFSR:
    def __init__(self, n: int) -> None:
        #all vals obey little endian, least sig fig first
        self.degree = n
        self.p: list[int]
        self.initVal: list[int]
    
    def str2List(self, strNums: str):
        
        nums = [int(c) for c in strNums]
        return nums
    
    def setP(self, Ps: list[int]):
        if (len(Ps) != self.degree):
            raise Exception("length of Ps must be the same as degree of LFSR")
        self.p = Ps
    
    def setInitVal(self, initVals: list[int]):
        if (len(initVals) != self.degree):
            raise Exception("length of initVals must be the same as degree of LFSR")
        self.initVal = initVals

    def generateKey(self, size: int):
        if (size <= self.degree):
            return self.p[:size]
        key = [0 for _ in range(size)]
        for i in range(len(self.initVal)):
            key[i] = self.initVal[i]
        pointer: int = len(self.initVal)
        

q1 = LFSR(6)
q1.setP(q1.str2List("110101"))

print(q1.p)