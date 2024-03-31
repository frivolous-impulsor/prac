import unittest
import random

#Part 1

#1.1
class IndexMinPQ:
    def __init__(self, n) -> None:
        self.val: list[int] = [None for i in range (n)]
        self.pm: list[int] = [None for i in range (n)]
        self.im: list[int] = [None for i in range (n)]
        self.size = 0
    
    def swap(self, i, j):
        self.pm[self.im[i]] = j
        self.pm[self.im[j]] = i
        self.im[i],self.im[j] = self.im[j],self.im[i]
    
    def swim(self, i):
        p = (i-1)//2
        while i > 0 and self.val[self.im[i]] < self.val[self.im[p]]:
            self.swap(i, p)
            i = p
            p = (i-1)//2
        
    def insert(self, key, value):
        insertIndex = self.size
        self.val[key] = value
        self.pm[key] = insertIndex
        self.im[insertIndex] = key
        self.swim(insertIndex)
        self.size +=1


class TestIndexHeapTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testSize = 20
        self.heap = IndexMinPQ(20)
    
    def testInsert(self):
        heap = self.heap
        insertSize = 4
        insertVals = [random.randint(1,100) for i in range(insertSize)]

        for i in range(insertSize):
            heap.insert(i,insertVals[i])
        expectedVal = [None for i in range(self.testSize)]
        for i in range(len(insertVals)):
            expectedVal[i] = insertVals[i]
        self.assertEqual(heap.val, expectedVal)




def go_test(val):
    if val == 1 and __name__ == '__main__':
        unittest.main()

go_test(1)