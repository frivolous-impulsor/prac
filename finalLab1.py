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
    
    def sink(self, i):
        left = i * 2 + 1
        right = left + 1
        smaller = left
        if right < self.size and self.val[left] > self.val[right]:
            smaller = right
        if smaller < self.size and self.val[self.im[i]] > self.val[self.im[smaller]]:
            self.swap(i, smaller)
            self.sink(smaller)  

    def remove(self, key): 
        removed = (key, self.val[key])
        kPosition = self.pm[key]
        endPosition = self.size-1
        self.swap(kPosition,endPosition)
        self.val[key] = None
        self.pm[key] = None
        self.im[endPosition] = None
        self.size -=1
        self.sink(kPosition)
        return removed




class TestIndexHeapTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testSize = 20
        self.heap = IndexMinPQ(20)
    
    def testInsert(self):
        heap = self.heap
        insertSize = 4
        insertVals = [10, 12, 5, 0]
        insertPm = [2,3,1,0]
        insertIm = [3,2,0,1]

        for i in range(insertSize):
            heap.insert(i,insertVals[i])
        expectedVal = [None for i in range(self.testSize)]
        expectedPm = [None for i in range(self.testSize)]
        expectedIm = [None for i in range(self.testSize)]
        for i in range(len(insertVals)):
            expectedVal[i] = insertVals[i]
            expectedPm[i] = insertPm[i]
            expectedIm[i] = insertIm[i]
        self.assertEqual(heap.val, expectedVal)
        self.assertEqual(heap.pm, expectedPm)
        self.assertEqual(heap.im, expectedIm)
        self.assertEqual(heap.size, insertSize)

    def testRemove(self):
        heap = self.heap
        insertSize = 4
        insertVals = [10, 12, 5, 0]
        insertPm = [0,2,1]
        insertIm = [0,2,1]

        for i in range(insertSize):
            heap.insert(i,insertVals[i])
        heap.remove(3)
        expectedVal = [None for i in range(self.testSize)]
        expectedPm = [None for i in range(self.testSize)]
        expectedIm = [None for i in range(self.testSize)]
        for i in range(len(insertPm)):
            expectedVal[i] = insertVals[i]
            expectedPm[i] = insertPm[i]
            expectedIm[i] = insertIm[i]
        self.assertEqual(heap.val, expectedVal)
        self.assertEqual(heap.pm, expectedPm)
        self.assertEqual(heap.im, expectedIm)



def go_test(val):
    if val == 1 and __name__ == '__main__':
        unittest.main()

go_test(1)