import random
import unittest

class Stack:
    s = []
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)
    
    def pop(self):
        if len(self.s) == 0:
            raise Exception("stack empty! No more popping.")
        upper = self.s[-1]
        self.s = self.s[:-1]
        return upper
    
    def is_stack_empty(self):
        return len(self.s) == 0


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


class TestMaxHeapPQ(unittest.TestCase):
    def setUp(self) -> None:
        max_length = 5
        self.pq = MaxPQ(max_length)
        return super().setUp()
    def test_put(self):
        a = Node('a', 5)
        b = Node('b', 1)
        w = Node('w', 10)
        z = Node('z', 3)
        p = Node('p', 6)
        self.pq.put(a)
        self.pq.put(b)
        self.pq.put(w)
        self.pq.put(z)
        self.pq.put(p)
        pq_value = []
        for i in range(self.pq.n):
            pq_value.append(self.pq.degrees[i].value)
        self.assertEqual(pq_value, [10, 6, 5, 1, 3])
    def test_delete_max(self):
        a = Node('a', 5)
        b = Node('b', 1)
        w = Node('w', 10)
        z = Node('z', 3)
        p = Node('p', 6)
        self.pq.put(a)
        self.pq.put(b)
        self.pq.put(w)
        self.pq.put(z)
        self.pq.put(p)
        max_degree = self.pq.delete_max()
        self.assertEqual(max_degree.value, 10)
class TestMinHeapPQ(unittest.TestCase):
    def setUp(self) -> None:
        max_length = 5
        self.pq = MinPQ(max_length)
        return super().setUp()
    def test_put(self):
        a = Node('a', 5)
        b = Node('b', 1)
        w = Node('w', 10)
        z = Node('z', 3)
        p = Node('p', 6)
        self.pq.put(a)
        self.pq.put(b)
        self.pq.put(w)
        self.pq.put(z)
        self.pq.put(p)
        pq_value = []
        for i in range(self.pq.n):
            pq_value.append(self.pq.degrees[i].value)
        self.assertEqual(pq_value, [1,3,10,5,6])
    def test_delete_min(self):
        a = Node('a', 5)
        b = Node('b', 1)
        w = Node('w', 10)
        z = Node('z', 3)
        p = Node('p', 6)
        self.pq.put(a)
        self.pq.put(b)
        self.pq.put(w)
        self.pq.put(z)
        self.pq.put(p)
        max_degree = self.pq.delete_min()
        self.assertEqual(max_degree.value, 1)


class Graph:
    v_num: int
    e_num: int
    # using hash map
    def __init__(self):
        self.v_num = 0
        self.e_num = 0
        self.graph = {}

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
        random.shuffle(pick_i)
        current_i = 0
        
        while not self.is_vc(covering_vs):
            rand_edge = edges[pick_i[current_i]]
            current_i +=1
            u = rand_edge[0]
            v = rand_edge[1]
            covering_vs.add(u)
            covering_vs.add(v)
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
        degree_pq = MaxPQ(self.e_num)
        g_dict = self.graph
        for key in g_dict.keys():
            degree = len(g_dict[key])
            d_node = Node(key, degree)
            degree_pq.put(d_node)
        while not self.is_indep_set(ind_vs):
            high_d_node = degree_pq.delete_max()
            remove_key = high_d_node.key
            ind_vs.remove(remove_key)
        print(ind_vs)
        return ind_vs
    
        



class TestingGraphFuncs(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Graph()
        self.edge = ['a', 'b']
        self.edges = [['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b'], ['c', 'e'], ['e', 'c']]
        return super().setUp()
    def test_add_edge(self):
        self.g.add_edge(self.edge)
        g = self.g.graph
        self.assertEqual(g, {'a': ['b'],
                              'b': ['a']})
    
    def test_add_edges(self):
        self.g.add_edges(self.edges)
        g = self.g.graph
        self.assertEqual(g, {'a':['b', 'c'],
                             'b':['a', 'c'],
                             'c':['a', 'b', 'e'],
                             'e':['c']})
        
    def test_get_edges(self):
        self.g.add_edges(self.edges)
        edges = self.g.get_edges()
        self.assertEqual(edges, [['a', 'b'], ['a', 'c'], ['b', 'a'], ['b', 'c'], ['c', 'a'], ['c', 'b'], ['c', 'e'], ['e', 'c']])
    
    def test_is_vc(self):
        self.g.add_edges(self.edges)
        self.assertTrue(self.g.is_vc({'c'}))
        self.assertFalse(self.g.is_vc({}))

    def test_vc_1(self):
        self.g.add_edges(self.edges)
        vc = self.g.approx1()
        self.assertTrue(self.g.is_vc(vc))

    def test_vc_3(self):
        self.g.add_edges(self.edges)
        vc = self.g.approx3()
        self.assertTrue(self.g.is_vc(vc))

    def test_is_ind_set(self):
        self.g.add_edges(self.edges)
        ind = {'a', 'e'}
        ind_n = {'a', 'b'}
        self.assertTrue(self.g.is_indep_set(ind))
        self.assertFalse(self.g.is_indep_set(ind_n))
    
    def test_find_ind(self):
        self.g.add_edges(self.edges)
        ind_vs = self.g.find_ind_set()
        self.assertTrue(self.g.is_indep_set(ind_vs))

    
if __name__ == '__main__':
    unittest.main()
