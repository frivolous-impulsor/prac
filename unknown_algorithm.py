import random
import math
import timeit
import matplotlib.pyplot as plt

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    #if we already have this node, wouldn't it just erase all the connections for this node?
    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)

def init_d(G):
    n = G.number_of_nodes()
    #a n-by-n matrix initialized all to inf
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    #Set the weight of an entry if row and col is connected, and diagonal entries are set to weight of zero(0 saying no cost to go from a vertex to it self)
    return d

#Assumes G represents its nodes as integers 0,1,...,(n-1)
def unknown(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                #if the cost between u and v is shorter in other ways, cost is updated to the lower
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d
#d the matrix of shortest cost between row and col


def testWithNegative():
    graph = DirectedWeightedGraph()
    for i in range(3): graph.add_node(i)
    graph.add_edge(0, 1, 5)
    graph.add_edge(1, 2, -4)
    graph.add_edge(0, 2, 4)
    dist = unknown(graph)
    print(dist)

    graph1 = DirectedWeightedGraph()
    for i in range(5): graph1.add_node(i)
    graph1.add_edge(0, 1, 3)
    graph1.add_edge(1, 2, 3)
    graph1.add_edge(1, 3, 2)
    graph1.add_edge(3, 1, 4)
    graph1.add_edge(0, 2, -1)
    graph1.add_edge(2, 4, 2)
    dist1 = unknown(graph1)
    print(dist1)
def addRandomEdge(g: DirectedWeightedGraph, n):
    topV = n - 1
    u = random.randint(0, topV)
    v = random.randint(0, topV)
    w = random.randint(-100, 100)
    while u == v:
        v = random.randint(0, topV)
    g.add_edge(u, v, w)
def timeComplexityTest():
    intervals = [None for _ in range(100)]
    trial = 10
    for gSize in range(100):
        gSize = gSize+1
        graph = DirectedWeightedGraph()
        for i in range(gSize):
            graph.add_node(i)
        print(graph.adj)
        eSize = gSize**2//2
        #Add edges
        for _ in range(eSize):
            addRandomEdge(graph, gSize)
        #test time
        time = 0
        for _ in range(trial):
            init = timeit.default_timer()
            unknown(graph)
            time += timeit.default_timer() - init
        time = time/trial
        intervals[gSize-1] = time
    plt.plot([i+1 for i in range(100)], intervals)
    plt.xlabel("size of graph(#vertex)")
    plt.ylabel("time consumption of unknown(sec)")
    plt.show()


            

timeComplexityTest()
#Reflect:
#It works perfectly for finding the distance from col to row! 
#With 2 sample graphs I set, I manually checked the minmum cost from any vertex u to any vertex v, 
#and the result of unknown function corresponds perfect with my calculation, where the cost takes into consideration of negative weight.

#Time Complexity
#Theoretically, the funtion is at O(n^3), due to the massive triple layer for loops. 
#I configured a timeComplexityTest that test the time complexity as a function of size of graph, n.
#n ranges from 10 to 100, the edge number for each graph is half of n^2
#For each graph the unknown function runs for 10 times and I document the average time for that graph in intervals list.
#Finally, we plot the intervals. As the size of the graph grows linearly, the time consumption grows approximately in cube.
#Such time complexity is not at all surprising, since it literally calculates every single combination of routing to find the shortest path, 
#which ensures the precision, without ignoring redundant calculation. Thus the time complexity spikes.