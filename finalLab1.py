import unittest
import random
import math

#Part 1

#1.1
class IndexMinPQ:
    def __init__(self, n) -> None:
        self.val: list[int] = [None for i in range (n)]
        self.pm: list[int] = [None for i in range (n)]
        self.im: list[int] = [None for i in range (n)]
        self.size = 0

    def contains(self, i):
        return self.val[i] != None
    
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

    def peek(self):
        if self.size == 0:
            raise ValueError("priority queue currently empty, can't peek")
        topKey = self.im[0]
        topVal = self.val[topKey]
        return (topKey, topVal)
    
    def pop(self):
        if self.size == 0:
            raise ValueError("priority queue currently empty, can't pop")
        topKey = self.im[0]
        return self.remove(topKey)


class TestIndexHeapTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testSize = 4
        self.heap = IndexMinPQ(self.testSize)
    
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

class WeightEdge:
    def __init__(self, u, v, weight) -> None:
        self.u = u
        self.v = v
        self.weight = weight
    
    def weight(self):
        return self.weight
    
    def init(self):
        return self.u
    
    def final(self):
        return self.v

class directedWeightedGraph:
    def __init__(self, n) -> None:
        self.numV = n
        self.numE = 0
        self.adjList = [set() for i in range(n)]

    def vList(self, v):
        if v >= self.numV:
            raise IndexError("vertex not exist")
        return self.adjList[v]

    def addEdge(self, n1, n2, w):
        edge = WeightEdge(n1, n2, w)
        adjList = self.adjList
        adjList[n1].add(edge)
        self.numE +=1

    def addEdgeBoth(self, n1, n2, w):
        edge1 = WeightEdge(n1, n2, w)
        edge2 = WeightEdge(n2, n1, w)
        adjList = self.adjList
        adjList[n1].add(edge1)
        adjList[n2].add(edge2)
        self.numE +=2

    def removeVertex(self, v):
        self.adjList[v].clear()
        for elist in self.adjList:
            for edge in elist:
                a = edge.init()
                b = edge.final()
                if a == v or b == v:
                    elist.remove(edge)

    def dijkstra(self, s):
        def relax(v: int):
            nonlocal edge_to
            nonlocal dist_to
            nonlocal pq
            nonlocal adjList
            for edge in adjList[v]:
                to = edge.final()
                if dist_to[to] > dist_to[v] + edge.weight:
                    dist_to[to] = dist_to[v] + edge.weight
                    edge_to[to] = v

                    if pq.contains(to):
                        pq.update(to, dist_to[to])
                    else:
                        pq.insert(to, dist_to[to])

        numV = self.numV
        adjList = self.adjList
        edge_to = [None for i in range(numV)]
        dist_to = [math.inf for i in range(numV)]
        dist_to[s] = 0
        pq = IndexMinPQ(self.numE)
        pq.insert(s, 0)
        
        while pq.size > 0:
            relax(pq.pop()[0])
        return (edge_to, dist_to)
        
route = directedWeightedGraph(7)
route.addEdgeBoth(1,0,6)
route.addEdgeBoth(1,4,10)
route.addEdgeBoth(0,2,7)
route.addEdgeBoth(2,4,2)
route.addEdgeBoth(4,5,3)
route.addEdgeBoth(2,3,4)
route.addEdgeBoth(3,5,8)
route.addEdgeBoth(5,6,3)


print(route.dijkstra(2))


def go_test(val):
    if val == 1 and __name__ == '__main__':
        unittest.main()

go_test(0)
