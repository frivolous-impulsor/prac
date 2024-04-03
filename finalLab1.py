import unittest
import random
import math
import timeit
import matplotlib.pyplot as plt
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
        if self.im[left] == None:
            return
        right = left + 1
        smaller = left
        if self.im[right] !=None and self.val[self.im[left]] > self.val[self.im[right]]:
            smaller = right
        if self.val[self.im[i]] > self.val[self.im[smaller]]:
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

    def dijkstra(self, s, k=None):
        def relax(v: int):
            nonlocal edge_to
            nonlocal dist_to
            nonlocal pq
            nonlocal adjList
            nonlocal relaxLimit
            for edge in adjList[v]:
                to = edge.final()
                if dist_to[to] > dist_to[v] + edge.weight and relaxLimit[to] > 0:
                    dist_to[to] = dist_to[v] + edge.weight
                    edge_to[to] = v

                    if pq.contains(to):
                        pq.update(to, dist_to[to])
                    else:
                        pq.insert(to, dist_to[to])
                    relaxLimit[to] -=1
        if k == None: k = self.numV
        numV = self.numV
        adjList = self.adjList
        edge_to = [None for i in range(numV)]
        dist_to = [math.inf for i in range(numV)]
        relaxLimit = [k for i in range(numV)]
        dist_to[s] = 0
        pq = IndexMinPQ(self.numE)
        pq.insert(s, 0)
        relaxLimit[s] -=1
        
        while pq.size > 0:
            relax(pq.pop()[0])
        return (edge_to, dist_to)
    
    def bellmanFord(self, s, k=None):
        if k == None: k = self.numV
        numV = self.numV
        if s >= numV:
            raise ValueError("starting vertex not exist in graph")
        numE = self.numE
        relaxLimit = [k for i in range(numV)]
        adjList = self.adjList
        dist_to = [math.inf for i in range(numV)]
        dist_to[s] = 0
        relaxLimit[s] -=1
        edge_to = [None for i in range(numV)]

        for i in range(numV - 1):
            for edges in adjList:
                for edge in edges:
                    if dist_to[edge.final()] > dist_to[edge.init()] + edge.weight and relaxLimit[edge.final()] > 0:
                       dist_to[edge.final()] = dist_to[edge.init()] + edge.weight 
                       edge_to[edge.final()] = edge.init() 
                       relaxLimit[edge.final()] -=1

        
        for i in range(numV - 1):
            for edges in adjList:
                for edge in edges:
                    if dist_to[edge.final()] > dist_to[edge.init()] + edge.weight and relaxLimit[edge.final()] > 0:
                       dist_to[edge.final()] = -math.inf
                       relaxLimit[edge.final()] -=1

        return (dist_to, edge_to)
    
class GraphTest(unittest.TestCase):
    def setUp(self) -> None:
        self.route = directedWeightedGraph(7)
        self.route.addEdgeBoth(1,0,6)
        self.route.addEdgeBoth(1,4,10)
        self.route.addEdgeBoth(0,2,7)
        self.route.addEdgeBoth(2,4,2)
        self.route.addEdgeBoth(4,5,3)
        self.route.addEdgeBoth(2,3,4)
        self.route.addEdgeBoth(3,5,8)
        self.route.addEdgeBoth(5,6,3)
        return super().setUp()
        
    def testDijk(self):
        route = self.route
        init_0 = route.dijkstra(0)
        self.assertEqual(init_0, ([None, 0, 0, 2, 2, 4, 5], [0, 6, 7, 11, 9, 12, 15]))

#performance(accurary, time, space) experiment 
#graph size, with graph density(numE/numV) and k(numV) being constant
#We assume moderately dense(numE/numV) graph. 
#For extremly sparse, numE -> 0.
#For extremly dense(any vertex reaches any other vertex), numE -> numV**2
#For moderately dense, we pick mid -> numV**2 // 2
class GraphTestOnSize:
    def __init__(self, scale) -> None:
        self.scale: int = scale
        self.trial = 5
        self.scaleList: list[int] = [2*(2**i) for i in range(1,scale+1)]
        self.sizeEList = [None for i in range(scale)]
        for i in range(scale):
            self.sizeEList[i] = (self.scaleList[i]**2)//4

    def randEdge(self, high: int):
        s: int = random.randint(0, high-1)
        e: int = random.randint(0, high-1)
        while s == e: e = random.randint(0, high-1)
        weight = random.randint(0, 1000)
        return (s, e, weight)

        
    def testTime(self, funcId: int):
        scaleList = self.scaleList
        sizeEList =self.sizeEList
        count = 0
        #(time record initiated
        intervals = [None for _ in range(self.scale)]
        for i in range(self.scale):
            sizeE = sizeEList[i]
            graph = directedWeightedGraph(scaleList[i])
            for _ in range(sizeE):
                edgeTuple = self.randEdge(scaleList[i])
                graph.addEdge(edgeTuple[0], edgeTuple[1], edgeTuple[2])

            #one graph assembled complete
            time = 0
            for _ in range(self.trial):
                if id == 0:
                    init = timeit.default_timer()
                    graph.dijkstra(0)
                    interval = timeit.default_timer() - init
                else:
                    init = timeit.default_timer()
                    graph.bellmanFord(0)
                    interval = timeit.default_timer() - init
                time += interval
            time = time/self.trial
            intervals[i] = time
            count +=1
            print(count/self.scale*100, "%")
        print(intervals)
        #time record completed)
        
        #(plot initiated
        plt.plot(scaleList, intervals)
        plt.xlabel("scale of graph(#V)")
        plt.ylabel("time(sec)")
        plt.show()
        #plot completed)
        

test1 = GraphTestOnSize(8)
test1.testTime(0)
            




#graph density
        

#k


def go_test(val):
    if val == 1 and __name__ == '__main__':
        unittest.main()

go_test(0)
