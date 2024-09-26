class LFSR:
    def __init__(self, n: int) -> None:
        #all vals obey little endian, least sig fig first
        self.degree = n
        self.p: list[int]
        self.initVal: list[int]
    
    def str2List(self, strNums: str):
        
        nums = [int(c) for c in strNums]
        return nums
    
    def list2Str(self, nums: list[int]):
        strList: list[str] = map(str, nums)
        delimiter: str = ''
        return delimiter.join(strList)
    
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
        pointer: int = self.degree
        lp: int = pointer - self.degree
        mark: int = lp
        rp: int = pointer-1
        while pointer < kSize:
            result = 0
            while lp <= rp:
                result += self.p[lp - mark]*key[lp]
                lp +=1
            result = result % 2
            key[pointer] = result
            pointer +=1
            lp = pointer - self.degree
            mark = lp
            rp = pointer-1
        return key
    
    def encode(self, plainText: list[int]):
        size = len(plainText)
        key = self.generateKey(size)
        cipherText: list[int] = [0 for _ in range(size)]
        for i in range(size):
            cipherText[i] = key[i] ^ plainText[i]
        return cipherText
    
    def decode(self, cipherText: list[int]):
        size = len(cipherText)
        key = self.generateKey(size)
        plainText: list[int] = [0 for _ in range(size)]
        for i in range(size):
            plainText[i] = key[i] ^ cipherText[i]
        return plainText

def test():
    q1 = LFSR(20)
    q1.setP(q1.str2List("11010100010001101010"))
    q1.setInitVal(q1.str2List("00110110010101101111"))
    
    plainText = q1.str2List("00111101011100111000000111001100010011010110110100")
    length = len("00111101011100111000000111001100010011010110110100")
    keystream = q1.generateKey(len("00111101011100111000000111001100010011010110110100"))
    ciphertex = q1.encode(plainText)
    print(ciphertex)
    print(plainText)
    print(keystream)
    
    guess = [0 for _ in plainText]
    for i in range(length):
        guess[i] = ciphertex[i] ^ plainText[i]
    print(guess)

test()