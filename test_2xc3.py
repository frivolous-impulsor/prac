import random
import unittest
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


class Tree:
    value: int
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def print_bt(self):
        if self.left != None:
            self.left.print_bt()
        print(self.value)
        if self.right != None:
            self.right.print_bt()
    
    def add_num(self, num):
        if self == None:
            self = Tree(num)
            return self
        append_tree = Tree(num)
        if num <= self.value:
            if self.left == None:
                self.left = append_tree
            else:
                self.left.add_num(num)
        else:
            if self.right == None:
                self.right = append_tree
            else:
                self.right.add_num(num)

class Node:
    key: any
    value: int
    def __init__(self, key, val) -> None:
        self.key = key
        self.value = val

class MaxPQ:
    degrees: list[Node]
    n: int
    def __init__(self, cap) -> None:
        self.degrees = [None] * cap
        self.n = 0

    def is_maxPQ_empty(self):
        return self.n == 0

    def maxPQ_size(self):
        return self.n

    def swim(self, i):
        parenti: int = (i - 1)//2
        while i > 0 and self.degrees[parenti].value < self.degrees[i].value:
            self.degrees[parenti], self.degrees[i] = self.degrees[i], self.degrees[parenti]
            i = parenti
            parenti = (i - 1)//2



    def sink(self, i):
        heapLength = self.n
        while i*2 + 1 < heapLength:
            kid: int = i*2 + 1
            if kid + 1 < heapLength and self.degrees[kid + 1].value > self.degrees[kid].value:
                kid += 1
            if self.degrees[kid].value <= self.degrees[i].value:
                break
            self.degrees[kid], self.degrees[i] = self.degrees[i], self.degrees[kid]
            i = kid

    def put(self, degree_node):
        place = self.n
        self.degrees[place] = degree_node
        self.swim(place)
        self.n +=1

    def delete_max(self):
        length = self.n
        if length < 1:
            return 0
        self.degrees[0], self.degrees[length - 1] = self.degrees[length - 1], self.degrees[0]
        deleted = self.degrees[length - 1]
        self.n -=1
        self.sink(0)
        return deleted

class MinPQ:
    degrees: list[Node]
    n: int
    def __init__(self, cap) -> None:
        self.degrees = [None] * cap
        self.n = 0

    def is_maxPQ_empty(self):
        return self.n == 0

    def maxPQ_size(self):
        return self.n

    def swim(self, i):
        parenti: int = (i - 1)//2
        while i > 0 and self.degrees[parenti].value > self.degrees[i].value:
            self.degrees[parenti], self.degrees[i] = self.degrees[i], self.degrees[parenti]
            i = parenti
            parenti = (i - 1)//2



    def sink(self, i):
        heapLength = self.n
        while i*2 + 1 < heapLength:
            kid: int = i*2 + 1
            if kid + 1 < heapLength and self.degrees[kid + 1].value < self.degrees[kid].value:
                kid += 1
            if self.degrees[kid].value >= self.degrees[i].value:
                break
            self.degrees[kid], self.degrees[i] = self.degrees[i], self.degrees[kid]
            i = kid

    def put(self, degree_node):
        place = self.n
        self.degrees[place] = degree_node
        self.swim(place)
        self.n +=1

    def delete_min(self):
        length = self.n
        if length < 1:
            return 0
        self.degrees[0], self.degrees[length - 1] = self.degrees[length - 1], self.degrees[0]
        deleted = self.degrees[length - 1]
        self.n -=1
        self.sink(0)
        return deleted

# class TestMaxHeapPQ(unittest.TestCase):
#     def setUp(self) -> None:
#         max_length = 5
#         self.pq = MaxPQ(max_length)
#         return super().setUp()
#     def test_put(self):
#         a = Node('a', 5)
#         b = Node('b', 1)
#         w = Node('w', 10)
#         z = Node('z', 3)
#         p = Node('p', 6)
#         self.pq.put(a)
#         self.pq.put(b)
#         self.pq.put(w)
#         self.pq.put(z)
#         self.pq.put(p)
#         pq_value = []
#         for i in range(self.pq.n):
#             pq_value.append(self.pq.degrees[i].value)
#         self.assertEqual(pq_value, [10, 6, 5, 1, 3])
#     def test_delete_max(self):
#         a = Node('a', 5)
#         b = Node('b', 1)
#         w = Node('w', 10)
#         z = Node('z', 3)
#         p = Node('p', 6)
#         self.pq.put(a)
#         self.pq.put(b)
#         self.pq.put(w)
#         self.pq.put(z)
#         self.pq.put(p)
#         max_degree = self.pq.delete_max()
#         self.assertEqual(max_degree.value, 10)
# class TestMinHeapPQ(unittest.TestCase):
#     def setUp(self) -> None:
#         max_length = 5
#         self.pq = MinPQ(max_length)
#         return super().setUp()
#     def test_put(self):
#         a = Node('a', 5)
#         b = Node('b', 1)
#         w = Node('w', 10)
#         z = Node('z', 3)
#         p = Node('p', 6)
#         self.pq.put(a)
#         self.pq.put(b)
#         self.pq.put(w)
#         self.pq.put(z)
#         self.pq.put(p)
#         pq_value = []
#         for i in range(self.pq.n):
#             pq_value.append(self.pq.degrees[i].value)
#         self.assertEqual(pq_value, [1,3,10,5,6])
#     def test_delete_min(self):
#         a = Node('a', 5)
#         b = Node('b', 1)
#         w = Node('w', 10)
#         z = Node('z', 3)
#         p = Node('p', 6)
#         self.pq.put(a)
#         self.pq.put(b)
#         self.pq.put(w)
#         self.pq.put(z)
#         self.pq.put(p)
#         max_degree = self.pq.delete_min()
#         self.assertEqual(max_degree.value, 1)


class Graph:
    v_num: int
    e_num: int
    # using hash map
    def __init__(self):
        self.v_num = 0
        self.e_num = 0
        self.graph = {}
    
    def add_ver(self, v: any):
        g_dict = self.graph
        g_dict[v] = []

    def add_vers(self, vers: list[any]):
        g_dict = self.graph
        for v in vers:
            g_dict[v] = []

    def add_edge(self, edge: list[int]):
        if isinstance(edge[0], list) or len(edge) != 2: raise ValueError("edge is of form: [a, b]")
        u = edge[0]
        v = edge[1]
        if not u in self.graph.keys():
            self.graph[u] = [v]
            self.v_num +=1
            self.e_num +=1
        elif not v in self.graph[u]:
            self.graph[u].append(v)
            self.e_num +=1
        if not v in self.graph.keys():
            self.graph[v] = [u]
            self.v_num +=1
            self.e_num +=1
        elif not u in self.graph[v]:
            self.graph[v].append(u)
            self.e_num +=1
    
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def get_edges(self):
        graph = self.graph
        edges = []
        for key in graph.keys():
            connected_list = graph[key]
            for connected in connected_list:
                edges.append([key, connected])
        return edges

    def is_vc(self, covering_v: set):
        g_dict = self.graph.copy()
        for key in g_dict.keys():
            detected = False
            if key in covering_v:
                g_dict[key] = []
                detected = True
            else:
                for item in covering_v:
                    if item in g_dict[key]:
                        g_dict[key] = []
                        detected = True
            if not detected:
                return False
        return True
        
    def approx1(self):
        g_dict = self.graph.copy()
        covering_vs = set()
        degree_pq = MaxPQ(len(g_dict.keys()))
        for key in g_dict.keys():
            degree = len(g_dict[key])
            degree_n = Node(key, degree)
            degree_pq.put(degree_n)
        while not self.is_vc(covering_vs):
            high_d_v = degree_pq.delete_max().key
            covering_vs.add(high_d_v)
        return covering_vs
    
        
    def approx3(self):
        covering_vs = set()
        edges = self.get_edges()
        length = len(edges)
        pick_i = [x for x in range(length)]
        print(edges)
        random.shuffle(pick_i)
        current_i = 0
        
        while not self.is_vc(covering_vs):
            print(current_i)
            rand_e_index = pick_i[current_i]
            rand_edge = edges[rand_e_index]
            current_i +=1

            u = rand_edge[0]
            v = rand_edge[1]
            covering_vs.add(u)
            covering_vs.add(v)
            print(covering_vs)
        return covering_vs
    
    def is_indep_set(self, ind_set: set):
        if len(ind_set) == 0: return True
        edges = self.get_edges()
        for v in ind_set:
            for u in ind_set:
                edge = [u, v]
                if edge in edges:
                    return False
        return True
    
    def find_ind_set(self):
        ind_vs = set(self.graph.keys())
        degree_pq = MaxPQ(300)
        g_dict = self.graph
        for key in g_dict.keys():
            degree = len(g_dict[key])
            d_node = Node(key, degree)
            degree_pq.put(d_node)
        while not self.is_indep_set(ind_vs):
            high_d_node = degree_pq.delete_max()
            remove_key = high_d_node.key
            ind_vs.remove(remove_key)
        return ind_vs

# class TestingGraphFuncs(unittest.TestCase):
#     def setUp(self) -> None:
#         self.g = Graph()
#         self.edge = ['a', 'b']
#         self.edges = [['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b'], ['c', 'e'], ['e', 'c']]
#         return super().setUp()
    
#     def test_add_v(self):
#         self.g.add_ver('v')
#         self.g.add_ver('m')
#         self.g.add_ver('w')
#         self.assertEqual(self.g.graph, {'v': [],
#                                         'm': [],
#                                         'w': []})
        
#     def test_add_vs(self):
#         self.g.add_vers(['v', 'm', 'w'])
#         self.assertEqual(self.g.graph, {'v': [],
#                                         'm': [],
#                                         'w': []})
        

#     def test_add_edge(self):
#         self.g.add_edge(self.edge)
#         g = self.g.graph
#         self.assertEqual(g, {'a': ['b'],
#                               'b': ['a']})
    
#     def test_add_edges(self):
#         self.g.add_edges(self.edges)
#         g = self.g.graph
#         self.assertEqual(g, {'a':['b', 'c'],
#                              'b':['a', 'c'],
#                              'c':['a', 'b', 'e'],
#                              'e':['c']})
        
#     def test_get_edges(self):
#         self.g.add_edges(self.edges)
#         edges = self.g.get_edges()
#         self.assertEqual(edges, [['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b'], ['c', 'e'], ['e', 'c']])
    
#     def test_is_vc(self):
#         self.g.add_edges(self.edges)
#         self.assertTrue(self.g.is_vc({'c'}))
#         self.assertFalse(self.g.is_vc({}))

#     def test_vc_1(self):
#         self.g.add_edges(self.edges)
#         vc = self.g.approx1()
#         self.assertTrue(self.g.is_vc(vc))

#     def test_vc_3(self):
#         self.g.add_edges(self.edges)
#         vc = self.g.approx3()
#         self.assertTrue(self.g.is_vc(vc))

#     def test_is_ind_set(self):
#         self.g.add_edges(self.edges)
#         ind = {'a', 'e'}
#         ind_n = {'a', 'b'}
#         self.assertTrue(self.g.is_indep_set(ind))
#         self.assertFalse(self.g.is_indep_set(ind_n))
    
#     def test_find_ind(self):
#         self.g.add_edges(self.edges)
#         ind_vs = self.g.find_ind_set()
#         self.assertTrue(self.g.is_indep_set(ind_vs))

# if __name__ == '__main__':
#     unittest.main()

def create_random_graph(n,e): #by Sota
    e = math.ceil(e/2)
    g_object = Graph()
    g_dict = g_object.graph
    for v in range(n):
        g_object.add_ver(v)
    for _ in range(e):
        u = random.randint(0,n-1)
        v = random.randint(0,n-1)
        while u == v or u in g_dict[v]:  # n1 and n2 are different
            u = random.randint(0,n-1)
            v = random.randint(0,n-1)
        g_object.add_edge([u, v])
    return g_object

def mvc_lens(v_num):
    trial = 20
    lens = [0 for i in range(trial)]
    for i in range(trial):
        e_num = i * 5 + 3
        g_obj = create_random_graph(v_num, e_num)
        len_mvc = g_obj.approx1()
        lens[i] = len(len_mvc)
    return lens

def mis_lens(v_num):
    trial = 20
    lens = [0 for i in range(trial)]
    for i in range(trial):
        e_num = i * 5 + 3
        g_obj = create_random_graph(v_num, e_num)
        len_mis = g_obj.find_ind_set()
        lens[i] = len(len_mis)
    return lens

def draw_2_graphs(y1, y2, title):
    if not (len(y1) == len(y2)):
        raise ValueError("y1 and y2 should have same length for plotting")
    x_values = [i for i in range(len(y1))]
    plt.figure()
    plt.plot(x_values, y1, label='mvc_scale', marker='o')
    plt.plot(x_values, y2, label='mis_scale', marker='s')
    plt.xlabel('number of edges')
    plt.ylabel('number of elements in set')
    plt.title(title)
    plt.legend()
    plt.show()

#2.6

def mvc_mis_relation(_v_num):
    v = _v_num
    mvc_scales = mvc_lens(v)
    mis_scales = mis_lens(v)
    draw_2_graphs(mvc_scales, mis_scales, "somehting")

# mvc_mis_relation(30)

# g = Graph()
# g.add_edges([[10, 14], [14, 10]])
# print(g.approx3())



#glass drop experienment problem
#any glass drop from floor x and lower intact, floor x+1 and above shatters glass
#specify what to optimize


def drop(glasses, floors, memo):
    if floors == 0 or floors == 1:
        return floors
    
    if glasses == 1:
        return floors
    
    mini:int = 99999
    
    lo = 1
    hi = floors
    while lo <= hi:
        mid = (lo + hi)//2

        if memo[glasses-1][mid-1] != -1:
            low = memo[glasses-1][mid-1]
        else:
            low = drop(glasses-1, mid-1, memo)

        low = drop(glasses-1, mid-1, memo)
        high = drop(glasses, floors-mid, memo)


        if high>low:
            lo = mid - 1
        else:
            hi = mid + 1


class binarySearchTree:
    key: int

    def __init__(self, k) -> None:
        self.key = k
        self.left = None
        self.right = None
    
    def createNode(self, k):
        return binarySearchTree(k)

    def addNode(self, k):
        if self.key == k: return
        if k < self.key and self.left == None:
            self.left = self.createNode(k)
            return
        if k > self.key and self.right == None:
            self.right = self.createNode(k)
            return
        if k < self.key:
            self.left.addNode(k)
            return
        if k > self.key:
            self.right.addNode(k)

    def search(self, k) -> bool:
        if self.key == k:
            return True
        if k < self.key:
            if self.left != None:
                return self.left.search(k)
            return False
        elif k > self.key:
            if self.right != None:
                return self.right.search(k)
            return False
        
    def delete(self, k):
        if self == None:
            return self
        
        if k < self.key:
            self.left = self.left.delete(k)
            return self
        
        if k > self.key:
            self.right = self.right.delete(k)
            return self
        
        if self.left == None and self.right == None:
            return None
        
        if self.left == None and self.right != None:
            return self.right
        
        if self.left != None and self.right == None:
            return self.left
        
        minNode = self.right
        while minNode.left != None:
            minNode = minNode.left
        
        self.key = minNode.key
        self.right = self.right.delete(minNode.key)
        return self
    


    
class binarySeearchTreeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bTree = binarySearchTree(10)
    
    def test_init(self):
        self.assertEqual(self.bTree.key, 10)

    def test_addNode(self):
        self.bTree.addNode(1)
        self.bTree.addNode(20)
        self.bTree.addNode(4)
        self.assertEqual(self.bTree.left.key, 1)
        self.assertEqual(self.bTree.right.key, 20)
        self.assertEqual(self.bTree.left.right.key, 4)
    
    def test_search(self):
        self.bTree.addNode(1)
        self.bTree.addNode(20)
        self.bTree.addNode(4)
        self.assertEqual(self.bTree.search(1), True)
        self.assertEqual(self.bTree.search(4), True)
        self.assertEqual(self.bTree.search(10), True)
        self.assertEqual(self.bTree.search(20), True)
        self.assertEqual(self.bTree.search(30), False)

    def test_delete(self):
        self.bTree.addNode(1)
        self.bTree.addNode(20)
        self.bTree.addNode(4)
        self.bTree.addNode(0)
        self.bTree.addNode(30)
        



def go_test(val):
    if val == 1:
        if __name__ == '__main__':
            unittest.main()

go_test(0)
        

