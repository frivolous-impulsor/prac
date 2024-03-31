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
    
    def update(self, key, newVal):
        previouseVal = self.val[key]
        if previouseVal == newVal:
            return
        kPosition = self.pm[key]
        self.val[key] = newVal
        if newVal > previouseVal:
            self.sink(kPosition)
            return
        self.swim(kPosition)
        





class TestIndexHeapTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testSize = 20
        self.heap = IndexMinPQ(20)
    
    def testInsert(self):
        heap = self.heap
        insertSize = 4
        insertVals = [10, 5, 15, 1]

        for i in range(insertSize):
            heap.insert(i,insertVals[i])
        expectedVal = [None for i in range(self.testSize)]
        expectedPm = [None for i in range(self.testSize)]
        expectedIm = [None for i in range(self.testSize)]

        pmPre = [3,1,2,0]
        imPre = [3,1,2,0]
        for i in range(len(insertVals)):
            expectedVal[i] = insertVals[i]
            expectedPm[i] = pmPre[i]
            expectedIm[i] = imPre[i]
        self.assertEqual(heap.val, expectedVal)
        self.assertEqual(heap.pm, expectedPm)
        self.assertEqual(heap.im, expectedIm)
        self.assertEqual(heap.size, insertSize)

    def testRemove(self):
        heap = self.heap
        insertSize = 4
        insertVals = [10, 5, 15, 1]

        for i in range(insertSize):
            heap.insert(i,insertVals[i])
        expectedVal = [None for i in range(self.testSize)]
        expectedPm = [None for i in range(self.testSize)]
        expectedIm = [None for i in range(self.testSize)]
        heap.remove(3)
        pmPre = [1,0,2]
        imPre = [1,0,2]
        for i in range(3):
            expectedVal[i] = insertVals[i]
            expectedPm[i] = pmPre[i]
            expectedIm[i] = imPre[i]
        self.assertEqual(heap.val, expectedVal)
        self.assertEqual(heap.pm, expectedPm)
        self.assertEqual(heap.im, expectedIm)
        self.assertEqual(heap.size, 3)

    def testUpdate(self):
        heap = self.heap
        insertSize = 4
        insertVals = [10, 5, 15, 1]

        for i in range(insertSize):
            heap.insert(i,insertVals[i])
        expectedVal = [None for i in range(self.testSize)]
        expectedPm = [None for i in range(self.testSize)]
        expectedIm = [None for i in range(self.testSize)]
        heap.remove(3)
        heap.update(2,4)
        valPre = [10,5,4]
        pmPre = [1,2,0]
        imPre = [2,0,1]
        for i in range(3):
            expectedVal[i] = valPre[i]
            expectedPm[i] = pmPre[i]
            expectedIm[i] = imPre[i]
        self.assertEqual(heap.val, expectedVal)
        self.assertEqual(heap.pm, expectedPm)
        self.assertEqual(heap.im, expectedIm)
        self.assertEqual(heap.size, 3)


def go_test(val):
    if val == 1 and __name__ == '__main__':
        unittest.main()

go_test(1)