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

    def generateKey(self, kSize: int):
        if (kSize <= self.degree):
            return self.initVal[:kSize]
        key = [0 for _ in range(kSize)]
        for i in range(self.degree):
            key[i] = self.initVal[i]
        pointer: int = len(self.initVal)
        lp: int = pointer - self.degree
        rp: int = pointer-1
        while pointer < kSize:
            result = 0
            while lp < rp:
                result += self.p[lp % self.degree]*key[lp]
                lp +=1
            result = result % 2
            key[pointer] = result
            pointer +=1
            lp = pointer - self.degree
            rp = pointer-1
        return key
        

        

q1 = LFSR(20)
q1.setP(q1.str2List("11010100010001101010"))
q1.setInitVal(q1.str2List("00110110010101101111"))
print(q1.generateKey(10000))
