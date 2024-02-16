import math
from typing import List, Dict, Tuple
import numpy as np
import pandas as pd
import random
import time



def calc_tax(income, tax_gate, tax_rate):
    return max((income - tax_gate),0)*tax_rate
    

def after_tax_income(pre_income, tax_rate):
    return pre_income - calc_tax(pre_income, tax_rate)


def pizza_to_order(adult_num, kid_num):
    return -(-(adult_num*3 + kid_num*1)//8)

def my_and(a,b):
    result = not(not a or not b)
    return result

def circle_info(r):
    area = (math.pi) * r**2
    circum = math.pi * r * 2
    print("the area of this circle is: ", area)
    print("the circunference of this circle is: ", circum)


def in_range_1_3(num):
    return 1<=num<=3

h = "hello"

def change_at(line, t, index):
    fore = line[0:index]
    lat = line[index+1:]
    return fore + t + lat

def slice_out(s, i, j):
    return s[0:i] + s[j+1:]


def is_mult_6(x):
    return x%6 == 0

def puzzle1(n, m):
    if n > 5 and m > 0:
        return 1
    return 3


def puzzle3(x, y):
    return "A"

word = "hello"


def encode(t, key):
    return chr((ord(t)+key))

def decode(t, key):
    return chr((ord(t)-key))


def encode_str(word, key):
    after_produce = ""
    for letter in word:
        after_produce = after_produce + encode(letter, key)
    return after_produce


def count_space(line):
    flag = 0
    for t in line:
        if t == " ":
            flag += 1
    return flag

def facto(n):
    if n > 1:
        return n * facto(n - 1)
    elif n <= 0:
        return None
    else:
        return 1

def remove_space(line):
    output = ""
    for t in line:
        if t != " ":
            output += t
    return output


def reverse(line):
    output = ""
    if (len(line) <= 1):
        return line
    else:
        return reverse(line[1:]) + line[0]

def binary_value(b_value):
    power = 0
    value = 0
    for digit in reverse(b_value):
        if digit == "1" :
            value += (2 ** power)
        power += 1
    return value



def shorten_title(title):
    if len(title) != 0 and title[-1] != " ":
        title += " "
    for t in title:
        if t == " ":
            loc_of_space = title.index(" ")
            word = title[ :loc_of_space]
            if len(word) > 5:
                word = word[:4] + "."
            return word + " " + shorten_title(title[loc_of_space + 1: ])
    return title

promp_8 = "ur password should be at least 8\n"
promp_cap = "ur password should have at least one cap char\n"
promp_num = "ur password should have at least one num\n"
promp_symb = "ur password should have at least one special char\n"



def set_password():
    
    password = input("please enter your password: ")

    while not has_8(password) or not has_cap(password) or not has_symbol(password):
        total_promp = ""
        if not has_8(password):
            total_promp += promp_8
        if not has_cap(password):
            total_promp += promp_cap
        if not has_symbol(password):
            total_promp += promp_symb
        print(total_promp)
        return set_password()

    conf_password = input("please confirm your password: ")
    while password != conf_password:
        conf_password = input("Mismatch, again plz: ")
    print("Congrats!")

    

def has_symbol(s):
    special_symb = "!@#$%^&*()"
    for symble in special_symb:
        if symble in s:
            return True
    return False

def has_cap(s):
    if not s.islower():
        return True
    return False

def has_8(s):
    if len(s) >= 8:
        return True
    return False


def is_pala(word):
    if len(word) <= 1:
        return True
    return (word[0] == word[-1]) and is_pala(word[1:-1])

def sum(n):
    if n <= 1:
        return n
    return n + sum(n-1)

def sum_row(row):
    sum = 0
    for num in row:
        sum += num
    return sum
        

def max_List(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return sum_row(list[0])
    return max(sum_row(list[0]), max_List(list[1:]))

#3-4 in a group, 
#no student appears twice, 
#everyone in class has to be in a group, 
#everyone in the groups has to be in the class



def is_ok(list_groups, list_class):
    cleaned_list = clean_gl(list_groups)
    for group in cleaned_list:
        if len(group) >4 or len(group) < 3:
            return False
        for student in group:
            if not(student in list_class):
                return False


    for student in list_class:
        if count(cleaned_list, student) != 1:
            return False
    return True

def remove_dup(g):
    if len(g) == 1:
        return g
    if g[0] in g[1:]:
        return remove_dup(g[1:])
    return [g[0]] + remove_dup(g[1:])

def clean_gl(gl):
    if len(gl) == 1:
        return [remove_dup(gl[0])]
    return [remove_dup(gl[0])] + clean_gl(gl[1:])


def count(group_list, student)->int:
    # the number of groups the student is in within the group list
    count = 0
    for group in group_list:
        if student in group:
            count += 1
    return count


def ave_rate(file_name):
    total_rate = 0
    count = 0
    band_file = open(file_name, "r")
    for line in band_file:
        info = line.strip().split(",")
        total_rate += int(info[1])
        count += 1
    band_file.close()
    return total_rate/count

def creat_playlist(file_name, playlist_name, threshold):
    my_data = []
    band_file = open(file_name, "r")
    header = band_file.readline()
    for line in band_file:
        info = line.strip().split(",")
        my_data.append(info)
    band_file.close()

    playlist = open(playlist_name, "w")
    playlist.write(header)
    for bands in my_data:
        if int(bands[1]) >= threshold:
            playlist.write(",".join(bands) + "\n")
    playlist.close()


def count_vow(s):
    num_of_v = 0
    index = 0
    while index <len(s):
        if s[index] not in 'aeiou':
            num_of_v += 1
        index += 1
    return num_of_v
    




def pos_ave(l):
    total = 0
    posi_num = 0
    for sub_l in l:
        for num in sub_l:
            if num > 0:
                total += num
            posi_num += 1
    if posi_num == 0:
        return 0.0
    return total/posi_num




d = {}
d['alice'] = ['bob']
d['mark'] = 'maccio'
d["alice"].append('oliver')

alice_fri = d["alice"]
d["alice"].append('joe')

birthday = {}
birthday['march'] = {}
birthday["march"][1] = ['mark']
birthday["march"][2] = ['mineeb']
birthday['march'][2].append('maccio')

def invert(d):
    inverted = {}
    record = []
    for key in d:
        if not d[key] in record:
            inverted[d[key]] = [key]
        else:
            inverted[d[key]].append(key)
    return inverted


def collaspse(d1, d2):
    col = {}
    for key in d1:
        if d1[key] in d2:
                    # in d2 only looks for the keys in d2
            col[key] = d2[d1[key]]
    return col


#return the recommendation of friends followed by 'name''s following list except those already followed by name and name itself
def friends_of_friends(dict, name):
    rec = []
    for user in dict[name]:
        if user in dict:
            for sub_user in dict[user]:
                if (not sub_user in dict[name]) and (sub_user != name):
                    rec.append(sub_user)
    return rec

d = {'Vincent': ['Mark','Alice','Muneeb','Caleb'],
      'Alice': ['Emma','Caleb','Vincent','Mitchel'],
      'Emma': ["Mitchel", "Dave"]}

def hanoi(n, source, spare, des):
    if n == 1:
        print("move a disk from peg" + source + "to peg" + des)
    else:
        hanoi(n-1, source, des, spare)
        print("move a disk from peg" + source + "to peg" + des)
        hanoi(n-1, spare, des, source)



l = [2,6,2,6,8,356,2,34,23]

def sum(L):
    if len(L) == 0:
        return 0
    return L[0] + sum(L[1:])


def count(L, value):
    if len(L) == 0:
        return 0
    else:
        if L[0] == value:
            return 1 + count(L[1:], value)
        return count(L[1:], value)

# def inserion_sort(nums):
#     for index in range(1, len(nums)):
#         value = nums[index]
#         i = index - 1
#         while i >= 0:
#             if value < nums[i]:
#                 nums[i + 1] = nums[i]
#                 nums[i] = value
#             i -= 1

# def selection_sort(nums):
#     for i in range(len(nums) - 1):
#         mini_index = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[mini_index]:
#                 mini_index = j
#         nums[i], nums[mini_index] = nums[mini_index], nums[i]


# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-1):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]



# def insertion_sort(nums):
#     for index in range(1, len(nums)):
#         i = index - 1
#         track = index
#         while i >= 0:
#             if nums[track] < nums[i]:
#                 nums[track],nums[i] = nums[i],nums[track]
#             i -= 1
#             track -= 1


# def selection_sort(nums):
#     for i in range(len(nums) - 1):
#         mini_index = i
#         for j in range(i + 1,len(nums)):
#             if nums[j] < nums[mini_index]:
#                 mini_index = j
#         nums[mini_index],nums[i] = nums[i],nums[mini_index]


# def bubble_sort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums) -1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]







def insertion_sort(nums):
    for index in range(1, len(nums)):
        i = index - 1
        track = index
        while i>=0:
            if nums[track] < nums[i]:
                nums[track],nums[i] = nums[i],nums[track]
                track -= 1
            i -= 1

def selection_sort(nums):
    for index in range(len(nums)):
        mini_i = index
        for candi in range(index,len(nums)):
            if nums[candi] < nums[mini_i]:
                mini_i = candi
        nums[index],nums[mini_i] = nums[mini_i],nums[index]

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

romDic = {
        "" : 0,
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    

def romanToInt(s):
    if len(s) <= 1:
        return romDic[s]
    headNum = romDic[s[0]]
    afterNum = romDic[s[1]]
    if headNum < afterNum:
        return afterNum - headNum + romanToInt(s[2:])
    return headNum + romanToInt(s[1:])


def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            diff = target - nums[i]
            for j in range (i, len(nums)):
                if nums[j] == diff:
                    return [i,j]
                

a = np.array([[[1,2],
               [3,4]],

              [[5,6],
               [7,8]]])
a[0, :, 0] = [0,9]

z = np.zeros((2,3,3), dtype="int8")

r = np.random.randint(100, size=(5,5))
r2 = np.repeat(r, 2, axis=0)

def layers(nums):
    layers = len(nums)
    c = np.zeros((layers*2-1, layers*2-1))
    for i in range(layers -1, -1, -1):
        c[:, i] = nums[i]
        c[-i-1, :] = nums[i]
        c[:, -i-1] = nums[i]
        c[i, :] = nums[i]
    
    return c.astype("int32")

circle = layers([1,0,9])




#Data Structure and Algorithm

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


class NumericPriorityQueue:
    queue = []
    def __init__(self):
        self.queue = []

    def add(self, item: int):     
        if len(self.queue) == 0:
            self.queue.append(item)
            return 0
        else:
            for i in range(0, len(self.queue)):
                if item <= self.queue[i]:
                    self.queue = self.queue[:i] + [item] + self.queue[i:]
                    return 0   
            self.queue.append(item)
    def is_pq_empty(self):
        return len(self.queue) == 0

    def retrieve(self):
        if len(self.queue) == 0:
            raise Exception("Priority Queue Empty")
        highPri = self.queue[-1]
        self.queue = self.queue[:-1]
        return highPri


    

def sort(q):
    ps = NumericPriorityQueue()
    for i in q:
        ps.add(i)
    for n in range(1, len(ps.queue)+1):
        print(n)
        num = ps.retrieve()
        q[-n] = num

def infix_evaluator(expr: List[str]):
    nums = Stack()
    ops = Stack()
    numBrac = 0  
    calc = 0 
    for c in expr:
        
        if c.isnumeric():
            nums.push(c)
        elif c in "+-*/":
            ops.push(c)
        elif c == '(':
            numBrac += 1
        elif c == ')':
            numBrac -= 1
            if len(nums.s) < 2 or len(ops.s) < 1:
                raise Exception("Error format: not enough number or operator")
            num2 = int(nums.pop())
            num1 = int(nums.pop())
            operator = ops.pop()
            match operator:
                case "+":
                    calc = num1 + num2
                case "-":
                    calc = num1 - num2
                case "*":
                    calc = num1 * num2
                case "/":
                    calc = num1 / num2
            nums.push(calc)
        elif not c == " ":
            raise Exception("Error format: unidentified operator")
    if numBrac != 0:
        raise Exception("Error format: inconsistent bracket numbers")
    return calc


class FixedStack:
    cap = 0
    top = 0
    queue = []
    
    def __init__(self, n): 
        self.cap = n
        self.queue = [None] * n
        self.top = 0
        
    
    def push(self,item):
        if self.is_full():
            raise Exception("Array full, need some popping!")
        self.queue[self.top] = item
        self.top += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Array empty, no more popping!")
        topItem = self.queue[-1]
        self.queue = self.queue[:-1]
        self.top -= 1
        return topItem
    
    def is_empty(self):
        return self.top == 0
    
    def is_full(self):
        return self.top == self.cap
    
class FixedQueue:
    queue = []
    head = 0
    tail = 0
    cap = 0
    counter = 0
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.cap = n
        self.queue = [None] * n
        self.counter = 0
    
    def is_empty(self):
        return self.counter == 0
    
    def is_full(self):
        return self.counter == self.cap
    
    def enq(self, item):
        if self.is_full():
            raise Exception("queue is full, no more queing!")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.cap
        self.counter += 1
    
    def deq(self):
        if self.is_empty():
            raise Exception("empty queue, no more dequeing!")
        self.head = (self.head + 1) % self.cap
        self.counter -= 1
        return self.queue[self.head -1]
    
class Node:
    item = None
    next = None
    previous = None
    def __init__(self, i):
        self.item = i
        self.next = None
        self.previous = None   

class LinkList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return (self.head == None) and (self.tail == None)
    
    def append(self, i):
        appNode = Node(i)
        if self.is_empty():
            self.head = appNode
            self.tail = appNode
        else:
            self.tail.next = appNode
            appNode.previous = self.tail
            self.tail = appNode
        

    def prepend(self, i):
        preNode = Node(i)
        if self.is_empty():
            self.head = preNode
            self.tail = preNode
        else:
            self.head.previous = preNode
            preNode.next = self.head
            self.head = preNode
    
    def search(self, i):
        if self.is_empty():
            return False
        tarNode = self.head
        while tarNode != self.tail:
            if tarNode.item == i:
                return True
            tarNode = tarNode.next
        return tarNode.item == i
    
    def printList(self):
        current = self.head
        while current != None:
            print(current.item, end=' ')
            current = current.next
        print()
    
    def delete(self, i):
        if self.is_empty():
            return False
        
        tarNode = self.tail
        #singleton case
        if self.head == self.tail and tarNode.item == i:
            self.head = None
            self.tail = None
            return True

        #Numerous case
        while tarNode != self.head:
            if tarNode.item == i: #match before reaching the head
                if (tarNode == self.tail): #tail is to be deleted
                    self.tail = self.tail.previous
                    self.tail.next = None
                else: #middle node to be deleted
                    tarNode.previous.next = tarNode.next
                    tarNode.next.previous = tarNode.previous
                return True
            tarNode = tarNode.previous 
        if self.head.item == i:
            self.head = self.head.next
            self.head.previous = None
            return True
        return False

    def swapNodes(self, a: Node, b: Node):
        aHead: bool = self.head == a
        bTail: bool = self.tail == b            
        tempNode: Node = Node(0)
        tempNode.item = b.item
        tempNode.next = b.next
        tempNode.previous = b.previous
        AnextB: bool = a.next == b
        
        b.previous = a.previous
        if AnextB:
            b.next = a
        else:
            b.next = a.next
            a.next.previous = b

        if aHead:
            self.head = b  
        else:
            a.previous.next = b

        a.next = tempNode.next
        if AnextB:
            a.previous = tempNode
        else:
            a.previous = tempNode.previous
            tempNode.previous.next = a
        if bTail:
            self.tail = a
        else:
            tempNode.next.previous = a
        return 1
  

class NumericPQinLinkedList:
    queue = LinkList()
    def __init__(self):
        self.queue = LinkList()
    
    def is_empty(self):
        return self.queue.head == None and self.queue.tail == None
    
    def add(self, i):
        addNode = Node(i)
        if self.is_empty():
            self.queue.append(i)
            return 0
        if i <= self.queue.head.item: #add before the list
            self.queue.prepend(i)
        elif i >= self.queue.tail.item: #add after the list
            self.queue.append(i)
        else: #add in the middle
            currentNode = self.queue.head
            while i > currentNode.item: #run to the right of the list till find the first node that has an item as large or larger than i
                currentNode = currentNode.next
            addNode.previous = currentNode.previous
            addNode.next = currentNode
            currentNode.previous.next = addNode
            currentNode.previous = addNode

    def retrieve(self):
        if self.is_empty():
            raise Exception("empty linked list, no more retrieving!")
        retriNum = self.queue.tail.item
        if self.queue.head == self.queue.tail: #singleton case
            self.queue.head = None
            self.queue.tail = None
        else: #Numerous case
            self.queue.tail = self.queue.tail.previous
            self.queue.tail.next = None
        return retriNum

def insertion_sort(nums):
    if len(nums) > 1:
        for i in range(1, len(nums)):
            target = nums[i]
            sortedTill = i - 1
            while target < nums[sortedTill]:
                "todo"

def sorted2(Aarr, Barr):
    Aindex = 0
    Bindex = 0
    result = []
    for i in range(0, len(Aarr) + len(Barr)):
        
        if Aindex == len(Aarr):
            result = result + Barr[Bindex:]
            return result
        elif Bindex == len(Barr):
            result = result + Aarr[Aindex:]
            return result
        elif Aarr[Aindex] <= Barr[Bindex]:
            result.append(Aarr[Aindex])
            if Aindex < len(Aarr):
                Aindex += 1
        else:
            result.append(Barr[Bindex])
            if Bindex < len(Barr):
                Bindex += 1
    return result

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        nodeA = l1
        nodeB = l2
        sum = nodeA.val + nodeB.val
        if sum >= 10:
            sum = sum - 10
            carry = 1
        resultNode = ListNode(sum, None)
        while nodeA != None or nodeB != None:
            num1 = 0
            num2 = 0
            if nodeA != None:
                num1 = nodeA.val
            if nodeB != None:
                num2 = nodeB.val
            sum = num1 + num2 + carry
            carry = 0
            if sum >= 10:
                sum = sum - 10
                carry = 1
            resultNode.next = ListNode(sum, None)
            if nodeA != None:
                nodeA = nodeA.next
            if nodeB != None:
                nodeB = nodeB.next
        return resultNode
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        longest = 1
        for i in range(0, len(s)):
            unrepeated = s[i]
            for j in range(i + 1, len(s)):
                if not s[j] in unrepeated:
                    unrepeated = unrepeated + s[j]
                else:
                    break
            if len(unrepeated) > longest:
                longest = len(unrepeated)
        return longest
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

def selectionSort(arr: [int]):
    if len(arr) == 1:
        return 0   #successful
    for i in range(len(arr)):
        targetIndex = i
        smallestIndex = targetIndex
        for i in range(i + 1, len(arr)):
            if arr[i] <= arr[smallestIndex]:
                smallestIndex = i
        arr[targetIndex],arr[smallestIndex] = arr[smallestIndex], arr[targetIndex]
    return 0 #success


def insertionSort(arr: [int]):
    if len(arr) <= 1:
        return 0  #successful
    for i in range(1, len(arr)):
        targetIndex = i
        beforeIndex = targetIndex - 1
        while beforeIndex >= 0 and arr[targetIndex] < arr[beforeIndex]:
            arr[targetIndex], arr[beforeIndex] = arr[beforeIndex], arr[targetIndex]
            targetIndex -= 1
            beforeIndex = targetIndex - 1
    return 0 #successsful

def mergeSort(arr: [int]):
    if len(arr) < 2:
        return 0 #successful
    midIndex = len(arr) // 2
    leftHalf: [int] = arr[:midIndex]
    rightHalf: [int] = arr[midIndex: len(arr)]
    mergeSort(leftHalf)
    mergeSort(rightHalf)

    merge(arr, leftHalf, rightHalf)

def merge(inputArr: [int], leftHalf: [int], rightHalf: [int]):
    lPointer = 0
    rPointer = 0
    fPointer = 0

    while lPointer < len(leftHalf) and rPointer < len(rightHalf):
        if leftHalf[lPointer] <= rightHalf[rPointer]:
            inputArr[fPointer] = leftHalf[lPointer]
            lPointer += 1
        else:
            inputArr[fPointer] = rightHalf[rPointer]
            rPointer += 1
        fPointer += 1
    if lPointer == len(leftHalf):
        for i in range(rPointer, len(rightHalf)):
            inputArr[fPointer] = rightHalf[i]
            fPointer += 1
    else:
        for i in range(lPointer, len(leftHalf)):
            inputArr[fPointer] = leftHalf[i]
            fPointer += 1

def quickSort(arr: [int], lowIndex: int, highIndex: int):
    if lowIndex >= highIndex:
        return 0 #successful
    
    pivot = arr[highIndex]
    leftPointer = lowIndex
    rightPointer = highIndex
    while leftPointer < rightPointer:
        while arr[leftPointer] <= pivot and leftPointer < rightPointer:
            leftPointer += 1
        while arr[rightPointer] >= pivot and rightPointer > leftPointer:
            rightPointer -= 1
        arr[leftPointer],arr[rightPointer] = arr[rightPointer], arr[leftPointer]
    arr[leftPointer],arr[highIndex] = arr[highIndex],arr[leftPointer]

          
    quickSort(arr, lowIndex, leftPointer - 1)
    quickSort(arr, leftPointer + 1, highIndex)

def partition(array, low, high):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
 
# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)
l = [6,4,3,0,11]
quickSort(l, 0, len(l)-1)

print("l:", l)

def generate2dicesSortedFrequency(times):
    l: [int] = [0]*times
    for i in range(times):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        l[i] = d1 + d2
    mergeSort(l)
    for item in l:
        print(item)

def combinationsOfTwoDices():
    resultDic = {}
    for i in range(2, 13):
        resultDic[i] = []
    for d1 in range(1,7):
        for d2 in range(1,7):
            sum = d1 + d2
            resultDic[sum].append((d1, d2))
    return resultDic

def printDicOnebyOne(dic):
    for key in dic:
        l = dic[key]
        for tup in l:
            print(tup[0], '-',  tup[1], end='  ')
        print(end='\n')
        
def binarySearch(arr, key):
    if len(arr) == 0:
        raise Exception("empty arr")
    low = 0
    high = len(arr) - 1
    mid = (low + high)//2
    while mid >= low:
        if arr[mid] == key:
            return True
        if key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high)//2
    return False

def findMedianSortedArrays(nums1, nums2):
    totalLen = len(nums1) + len(nums2)
    finalArr = [0] * totalLen
    lpointer = 0
    rpointer = 0
    fpointer = 0
    while lpointer < len(nums1) and rpointer < len(nums2):
        if nums1[lpointer] <= nums2[rpointer]:
            finalArr[fpointer] = nums1[lpointer]
            lpointer += 1
        else:
            finalArr[fpointer] = nums2[rpointer]
            rpointer += 1
        fpointer += 1
    if lpointer == len(nums1):
        for i in range(rpointer, len(nums2)):
            finalArr[fpointer] = nums2[i]
            fpointer += 1
    elif rpointer == len(nums2):
        for i in range(lpointer, len(nums1)):
            finalArr[fpointer] = nums1[i]
            fpointer += 1
    midian = 0
    mid = totalLen // 2
    if totalLen % 2 == 0: #even
        return (finalArr[mid] + finalArr[mid - 1]) / 2
    else:
        return finalArr[mid]
#Symbol table
class NodeST:
    key = None
    value = None
    next = None 
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class symbolTable:
    head: NodeST
    def __init__(self) -> None:
        self.head = None

    def create_st():
        return symbolTable()
    
    def print_st(self):
        currentNode = self.head
        while currentNode is not None:
            print("<{}, {}>".format(currentNode.key, currentNode.value))
            currentNode = currentNode.next
    
    def put(self, key, value):
        newNode = NodeST(key, value)
        if self.head == None:
            self.head = newNode
            return 0

        currentNode = self.head
        if type(key) is int:
            while currentNode.next is not None and key >= currentNode.next.key:
                currentNode = currentNode.next
            if key == currentNode.key:
                currentNode.value = value
                return 1
            elif currentNode == self.head:
                newNode.next = currentNode
                self.head = newNode
            elif currentNode.next == None:
                currentNode.next = newNode
                return 2
            else:
                newNode.next = currentNode.next
                currentNode.next = newNode
                return 3

        else:
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def get(self, key):
        currentNode = self.head
        if currentNode is None:
            raise Exception("not found")
        while currentNode.next is not None and key >= currentNode.next.key:
            currentNode = currentNode.next
        if key == currentNode.key:
            return currentNode.value
        else:
            raise Exception("not found")

    def delete(self, key):
        if self.head is None:
            return True
        currentNode = self.head
        if currentNode.key == key:
            self.head = currentNode.next
        while currentNode.next is not None:
            if currentNode.next.key == key:
                currentNode.next = currentNode.next.next
                return True
            currentNode = currentNode.next
        return False

#Binary Search Tree
class NodeBST:
    key: int
    value: any
    left = None
    right = None
    n: int
    def __init__(self, key, value, n) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.n = n
def st_empty(st):
    return st == None 

def st_size(st):
    if st_empty(st):
        return 0
    return st.n

def put(st: NodeBST, key, value):
    if st_empty(st):
        newNode = NodeBST(key, value, 1)
        return newNode
    if key < st.key:
        st.left = put(st.left, key, value)
    elif key > st.key:
        st.right = put(st.right, key, value)
    else: #st.key == key
        st.value = value
    st.n = 1 + st_size(st.left) + st_size(st.right)
    return st

def treeType(st):
    sum: int = 0
    code: [bool] = [True, True]
    if traverse(st, code):
        sum += 1
        if code[0]:
            sum += 1
            if code[1]:
                sum += 1
    return sum

def traverse(st: NodeBST, c: [bool]) -> bool:
    if st.left == None and st.right == None:
        return True
    if st.right == None:
        c[0] = False
        return st.left.key <= st.key
    if st.left == None:
        c[0] = False        
        return st.right.key >= st.key
    if st.left.n != st.right.n:
        c[1] = False
    return (traverse(st.left, c) and (st.left.key <= st.key and st.key <= st.right.key) and traverse(st.right, c))

a = NodeBST(10, 'a', 1)

#should 0
# st = a
# a.left = b
# a.right = e
# b.left = d
# b.right = g

#should 1
st = a
put(st, 5, '')
put(st, 15, '')
put(st, 4, '')
put(st, 7, '')
put(st, 12, '')
put(st, 16, '')
#should 2

#should 3


 

def printBST(st: NodeBST):
    if st == None:
        return True
    printBST(st.left)
    print(st.key, ": ", st.value, " n: ", st.n)
    printBST(st.right)

def get(st: NodeBST, key):
    if st_empty(st):
        return None
    if key < st.key:
        return get(st.left, key)
    elif key > st.key:
        return get(st.right, key)
    else:
        return st.value
    
# def min(st):
#     if st_empty(st):
#         return None
#     if st_empty(st.left):
#         return st
#     return min(st.left)
    
# def max(st):
#     if st_empty(st):
#         return None
#     if st_empty(st.right):
#         return st
#     return max(st.right)

def delete(st, key):
    if st_empty(st):
        return None
    if key < st.key:
        st.left = delete(st.left, key)
    elif key > st.key:
        st.right = delete(st.right, key)
    #found the node:
    else:
        if st.left == None and st.right == None:
            return None
        elif st.left == None and st.right != None:
            return st.right
        elif st.left != None and st.right == None:
            return st.left
        minNodeRight = min(st.right)
        st.key = minNodeRight.key
        st.value = minNodeRight.value
        st.right = delete(st.right, st.key)
    st.n = 1 + st_size(st.left) + st_size(st.right)
    return st


class SymbolTable:
    keys: [int]
    values: [any] = 20 * [0]

    def __init__(self) -> None:
        self.keys = 20 * [0]
        self.values = 20 * [0]

    def printST(self):
        tableLength = len(self.keys)
        if tableLength == 0:
            return True
        for i in range(tableLength):
            print(self.keys[i], " : ", self.values[i])


    
    def delete(self, key):
        length: int = len(self.keys)
        if length == 0:
            raise Exception("empty symboltable")
        high: int = length - 1
        low: int = 0
        mid: int = (high + low) // 2
        while low <= high:
            if self.keys[mid] == key:
                item: any = self.values[mid]
                self.keys = self.keys[:mid] + self.keys[mid+1:]
                self.values = self.values[:mid] + self.values[mid+1:]
                return item
            elif key < self.keys[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = (high + low) // 2
        raise Exception("key not found")
    
# duoArrayTable = SymbolTable()
# duoArrayTable.keys = [1]
# duoArrayTable.values = ['a']
# duoArrayTable.delete(3)
# duoArrayTable.printST()

def floor(arr: [int], key: int):
    if len(arr) == 0:
        raise Exception("empty arr")
    high = len(arr) - 1
    low = 0
    mid = (high + low) // 2
    while low <= high:
        if arr[mid] == key:
            return key
        elif key <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (high + low)//2
    
    return arr[mid + 1]

class RBTNode:
    key: int
    value: any
    left = None
    right = None
    n: int
    color: bool #true is red
    def __init__(self, k, v) -> None:
        self.key = k
        self.value = v
        self.left = None
        self.right = None
        self.n = 1
        self.color = False
    def printRBT(self):
        if self == None:
            return 0
        printBST(self.left)
        print(self.key)
        printBST(self.right)

def rotate_left(st: RBTNode):
    rightNode = st.right
    st.right = rightNode.left
    rightNode.left = st
    rightNode.color = st.color
    st.color = True
    
    rightNode.n = st.n
    st.n = 1 + st_size(st.left) + st_size(st.right)
    return rightNode

def rotate_right(st: RBTNode):
    leftNode = st.left
    st.left = leftNode.right
    leftNode.right = st
    leftNode.color = st.color
    st.color = True

    leftNode.n = st.n
    st.n = 1 + st_size(st.left) + st_size(st.right)
    return leftNode

def colorFlip(st: RBTNode):
    st.color = True
    st.left.color = False
    st.right.color = False

def insertRBTNode(fst: RBTNode, fkey: int, fvalue: any):
    fst = bulkInsert(fst, fkey, fvalue)
    fst.color = False
    return fst
def bulkInsert(st, key, value):
    newNode: RBTNode = (key, value)
    if st == None:
        return newNode
    newNode.color = True
    if st.key == key:
        st.value = value
        return st
    elif key < st.key:
        st.left = insertRBTNode(st.left, key, value)
    else:
        st.right = insertRBTNode(st.right, key, value)
    
    if st.right.color and not st.left.color:
        st = rotate_left(st)
    if st.left.color and st.left.left.color:
        st = rotate_right(st)
    if st.left.color and st.right.color:
        st = colorFlip(st)
    
    st.n = 1 + st_size(st.left) + st_size(st.right)
    return st



class MaxPQ:
    keys: [int]
    n: int
    def __init__(self, cap) -> None:
        self.keys = [0] * cap
        self.n = 0
    
    def is_maxPQ_empty(self):
        return self.n == 0

    def maxPQ_size(self):
        return self.n
    
    def swim(self, i):
        parenti: int = (i - 1)//2
        while i > 0 and self.keys[parenti] < self.keys[i]:
            self.keys[parenti], self.keys[i] = self.keys[i], self.keys[parenti]
            i = parenti
            parenti = (i - 1)//2



    def sink(self, i):
        heapLength = self.n
        while i*2 + 1 < heapLength:
            kid: int = i*2 + 1
            if kid + 1 < heapLength and self.keys[kid + 1] > self.keys[kid]:
                kid += 1
            if self.keys[kid] <= self.keys[i]:
                break
            self.keys[kid], self.keys[i] = self.keys[i], self.keys[kid]
            i = kid

    def put(self, key):
        place = self.n
        self.keys[place] = key
        self.swim(place)
        self.n +=1
    
    def delete_max(self):
        length = self.n
        if length < 1:
            return 0
        self.keys[0], self.keys[length - 1] = self.keys[length - 1], self.keys[0]
        deleted = self.keys[length - 1]
        self.n -=1
        self.sink(0)
        return deleted

    def printKeys(self):
        print(self.keys[:self.n])
    
def heapSort(array):
    if len(array) < 2:
        return array
    length = len(array)
    targetSink = length//2 - 1
    auxHeap = MaxPQ(length)
    auxHeap.keys = array
    auxHeap.n = len(array)
    #heapify
    while targetSink >= 0:
        auxHeap.sink(targetSink)
        targetSink -= 1
    print(auxHeap.keys)
    #delete_maxex
    while auxHeap.n > 0:
        auxHeap.delete_max()

    print(auxHeap.keys[:len(array)])
        
            
a: Node = Node(5)
b: Node = Node(2)
c: Node = Node(0)
d: Node = Node(7)
e: Node = Node(6)
f: Node = Node(11)
g: Node = Node(9)
h: Node = Node(1)

c.next = e
h.next = g

hashTable: [Node] = [None, a, b, c, d, f, h]



class SymbolTableDuoArray:
    keys: [int]
    values: [any]

    def delete(self, key):
        length: int = len(self.keys)
        if length == 0:
            raise Exception("empty table")
        high: int = length - 1
        low: int = 0
        mid: int = (high + low)//2
        while low <= high:
            if self.keys[mid] == key:
                value = self.values[mid]
                self.keys = self.keys[:mid] + self.keys[mid+1:]
                self.values = self.values[:mid] + self.values[mid+1:]
                return value
            elif key < self.keys[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = (high + low)//2
        raise Exception("not found")

class Graph:
    V: int
    E: int
    alist: [int]
    edgeTo: [int]
    
    def __init__(self, v) -> None:
        self.V = v
        self.alist = [[]] * v
        self.edgeTo = [-1] * v

    def add_edge(self, v, w):
        self.alist[v] = self.alist[v] + [w]
        self.alist[w] = self.alist[w] + [v]
        self.E += 1
    
    def adj(self, v):
        return self.alist[v]
    
    def num_v(self):
        return self.V
    
    def num_e(self):
        return self.E
    
    def dfs(self, v):
        marked: [bool] = [False] * self.num_v()
        self.dfs_aux(v, marked)
        return marked

    def dfs_aux(self, v, markedList):
        if markedList[v]:
            return 
        markedList[v] = True
        print("visited ",v)
        for adjed in self.alist[v]:
            if not markedList[adjed]:
                self.edgeTo[adjed] = v
                self.dfs_aux(adjed, markedList)
    
    def bfs(self, v):
        marked: [bool] = [False] * self.num_v()
        breathQueue = FixedQueue(self.num_v())

        marked[v] = True
        breathQueue.enq(v)
        while not breathQueue.is_empty():
            v = breathQueue.deq()
            for adjed in self.adj(v):
                if not marked[adjed]:
                    marked[adjed] = True
                    self.edgeTo[adjed] = v
                    breathQueue.enq(adjed)
        return marked
    
    def centers_graph(self):
        def bfs_for_eccs(vertex):
            nonlocal radius
            marked: [bool] = [False] * self.num_v()
            breathQueue = FixedQueue(self.num_v())
            distance = [0] * self.num_v()
            marked[vertex] = True
            breathQueue.enq(vertex)
            ecc_of_vertex = 0
            while not breathQueue.is_empty():
                breath_ver = breathQueue.deq()
                for adjed in self.adj(breath_ver):
                    if not marked[adjed]:
                        marked[adjed] = True
                        distance[adjed] = distance[breath_ver] + 1
                        ecc_of_vertex = max(distance[adjed], ecc_of_vertex)
                        if radius != None and ecc_of_vertex > radius:
                            return ecc_of_vertex
                        self.edgeTo[adjed] = breath_ver
                        breathQueue.enq(adjed)

            if radius == None:
                radius = ecc_of_vertex
                count_for_disconnected = 0
                for i in self.edgeTo:
                    if i == -1:
                        count_for_disconnected += 1
                    if count_for_disconnected > 1:
                        raise Exception("graph is disconnected")
            else:
                radius = min(ecc_of_vertex, radius)
            return ecc_of_vertex
    
        eccentrics: [int] = [None] * self.num_v()
        radius: int= None
        for current_v in range(self.num_v()):
            eccentrics[current_v] = bfs_for_eccs(current_v)
        
        centers: [int] = []
        for i in range(self.num_v()):
            if eccentrics[i] == radius:
                centers.append(i)
        return centers

    

# test for centers_graph()
# g = Graph(5)
# g.alist = [[1,3], [0,2, 3], [1,3], [1, 2, 0], []]
# l = g.centers_graph()
# print(l)

class Digraph:
    V: int
    E: int
    aList: [int]
    edgeTo: [int]
    def __init__(self, v) -> None:
        self.V = v
        self.E = 0
        self.aList = [[]] * v
        self.edgeTo = [-1] * v
    
    def create_digraph(self, i: int):
        return Digraph(i)
    
    def adj(self, v):
        return self.aList[v]
    
    def add_edge(self, v, w):
        self.aList[v] = self.aList[v] + [w]
        self.E += 1
    
    def num_vertices(self):
        return self.V
    
    def num_edges(self):
        return self.E
    
    def reverse(self):
        rev_graph = self.create_digraph(self.num_vertices())
        for vertex in range(self.num_vertices()):
            for adjed in self.aList[vertex]:
                rev_graph.add_edge(adjed, vertex)
        return rev_graph
    
    def dfs(self, v):
        def dfs_aux(v):
            nonlocal marked
            marked[v] = True
            for pointedTo in self.adj(v):
                if not marked[pointedTo]:
                    self.edgeTo[pointedTo] = v
                    dfs_aux(pointedTo)

        marked: [bool] = [False] * self.num_vertices()
        dfs_aux(v)

        return marked

    

    def bfs(self, v):
        marked: [bool] = [False] * self.num_vertices()
        breathQueue = FixedQueue(self.num_vertices())
        breathQueue.enq(v)
        marked[v] = True
        while not breathQueue.is_empty():
            breath_ver: int = breathQueue.deq()
            marked[breath_ver] = True
            for pointedTo in self.adj(breath_ver):
                if not marked[pointedTo]:
                    self.edgeTo[pointedTo] = breath_ver
                    breathQueue.enq(pointedTo)
        return marked

    def dfs_for_Cycle(self):
        def aux_search(graph: Digraph, v):
            nonlocal has_cycle
            marked[v] = True
            stack[v] = True

            for pointedTo in graph.adj(v):
                if has_cycle:
                    return None
                if not marked[pointedTo]:
                    aux_search(graph, pointedTo)
                elif stack[pointedTo]:
                    has_cycle = True
                    
            stack[v] = False
        marked: [bool] = [False] * self.num_vertices()
        stack: [bool] = [False] * self.num_vertices()
        has_cycle: bool = False

        for vertex in range(self.num_vertices()):
            if not marked[vertex]:
                aux_search(self, vertex)

        return has_cycle
    
    def topoSort(self):
        def dfs(v):
            nonlocal marked
            nonlocal sorted
            if marked[v]:
                return 
            marked[v] = True
            for pointedTo in self.adj(v):
                if not marked[pointedTo]:
                    dfs(pointedTo)
            sorted.append(v)
        marked: [int] = [False] * self.num_vertices()
        sorted: [int] = []
        for v in range(self.num_vertices()):
            if not marked[v]:
                dfs(v)
        return sorted
        

    def is_topo(self, permutation: [int]):
        #construct topoList
        topoList: [int] = [0] * self.num_vertices()
        for rank in range(self.num_vertices()):
            v = permutation[rank]
            topoList[v] = rank
        
        for v in range(self.num_vertices()):
            edgeList: [int] = self.adj(v)
            for pointedTo in edgeList:
                vRank: int = topoList[v]
                pointedToRank: int = topoList[pointedTo]
                if vRank < pointedToRank: #in the case of v comes before it's pointedTo vertex
                    return False
        return True



class Edge:
    v: int
    w: int
    weight: float
    
    def __init__(self, v, w, weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight
    
    def create_edge(v, w, weight):
        return Edge(v, w, weight)
    
    def weight(self):
        return self.weight
    
    def either(self):
        return self.v
    
    def other(self, vertex: int):
        if self.v == vertex:
            return self.w
        return self.v
    
class MinPQ_forEdges:
    edges: [Edge]
    n: int
    def __init__(self, cap) -> None:
        self.keys = [None] * cap
        self.n = 0
    
    def is_minPQ_empty(self):
        return self.n == 0

    def minPQ_size(self):
        return self.n
    
    def swim(self, i):
        parenti: int = (i - 1)//2
        while i > 0 and self.keys[parenti].weight > self.keys[i].weight:
            self.keys[parenti], self.keys[i] = self.keys[i], self.keys[parenti]
            i = parenti
            parenti = (i - 1)//2

    def sink(self, i):
        heapLength = self.n
        while i*2 + 1 < heapLength:
            kid: int = i*2 + 1
            if kid + 1 < heapLength and self.keys[kid + 1].weight < self.keys[kid].weight:
                kid += 1
            if self.keys[kid].weight >= self.keys[i].weight:
                break
            self.keys[kid], self.keys[i] = self.keys[i], self.keys[kid]
            i = kid

    def put(self, key: Edge):
        place = self.n
        self.keys[place] = key
        self.swim(place)
        self.n +=1
    
    def delete_min(self):
        length = self.n
        if length < 1:
            return 0
        self.keys[0], self.keys[length - 1] = self.keys[length - 1], self.keys[0]
        deleted = self.keys[length - 1]
        self.n -=1
        self.sink(0)
        return deleted

    def printKeys(self):
        for edge in self.keys[:self.n]:
            print(edge.weight)
        
# minPQ = MinPQ_forEdges(10)
# minPQ.put(Edge(0, 0, 5))
# minPQ.put(Edge(0, 0, 4))
# minPQ.put(Edge(0, 0, 9))
# minPQ.put(Edge(0, 0, 1))
# minPQ.put(Edge(0, 0, 0))
# minPQ.put(Edge(0, 0, 3))
# minPQ.put(Edge(0, 0, -6))
# minPQ.printKeys()
class unionFind:
    parents: List[int]
    size: List[int]
    
    def __init__(self, n) -> None:
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
        self.size = [1] * n
    
    def find(self, x):
        current = x
        while self.parents[current] != current:
            current = self.parents[current]
        return current

    def connect(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        if self.connect(a, b):
            return
        a_group_size = self.size[a]
        b_group_size = self.size[b]
        a_id = self.find(a)
        b_id = self.find(b)
        if a_group_size >= b_group_size:
            self.parents[b_id] = a_id
            self.size[a_id] = self.size[a_id] + self.size[b_id]
        else:
            self.parents[a_id] = b_id
            self.size[b_id] = self.size[a_id] + self.size[b_id]

# unions: unionFind = unionFind(4)
# unions.union(0,1)
# unions.union(2,3)
# unions.union(1,3)
# print(unions.parents)
# print(unions.size)


    

class EdgeWeightedGraph:
    V: int
    E: int
    aList: [Edge]

    def __init__(self, v) -> None:
        self.V = v
        self.aList = [[]] * self.V

    def add_edge(self, e: Edge):
        v = e.either()
        w = e.other(v)
        self.aList[v] = self.aList[v] + e
        self.aList[w] = self.aList[w] + e
        self.E += 1
    
    def adj(self, v):
        return self.aList[v]
    
    def num_vertices(self):
        return self.V
    
    def num_edges(self):
        return self.E
    
    def mstPrim(self):
        def visite(v):
            nonlocal marked
            nonlocal pq
            marked[e] = True

            for e in self.adj(v):
                if not marked[e.other(v)]:
                    pq.put(e)
    
        pq = MinPQ_forEdges(self.E)
        marked: [bool] = [False] * self.num_vertices()
        mst: FixedQueue = FixedQueue(self.num_edges())
        visite(0)
        while not pq.is_minPQ_empty():
            min_weighted_edge: Edge = pq.delete_min()
            v = min_weighted_edge.either()
            w = min_weighted_edge.other(v)
            if not marked[v] or not marked[w]:
                mst.enq(min_weighted_edge)
                if not marked[v]: visite(v)
                if not marked[w]: visite(w)
        return mst
    
    def mstKrus(self):
        pq: MinPQ_forEdges = MinPQ_forEdges(self.num_edges)
        for v in range(self.num_vertices()):
            for e in self.adj(v):
                pq.put(e)
        mst: FixedQueue = FixedQueue(self.num_vertices - 1)
        uf: unionFind = unionFind(self.num_vertices)

        while not pq.is_minPQ_empty and mst.counter < self.num_vertices - 1:
            mini_edge: Edge = pq.delete_min()
            v = mini_edge.either()
            w = mini_edge.other(v)
            if not uf.connect(v, w):
                mst.enq(mini_edge)
                uf.union(v, w)
        
        return mst


    def mstKrusPreSet(self, S: [Edge]):
        mst: FixedQueue = FixedQueue(self.num_vertices - 1)
        uf: unionFind = unionFind(self.num_vertices())
        for e in S:
            v: Edge = e.either()
            w: Edge = e.other(w)
            mst.enq(e)
            uf.union(v, w)
        
        pq: MinPQ_forEdges = MinPQ_forEdges(self.num_edges())
        for v in range(self.num_vertices()):
            for e in self.adj(v):
                pq.put(e)
        while not pq.is_minPQ_empty() and mst.counter < self.num_vertices() - 1:
            min_weighted_edge: Edge = pq.delete_min()
            v = min_weighted_edge.either()
            w = min_weighted_edge.other(v)
            if not uf.connect(v, w):
                mst.enq(min_weighted_edge)
                uf.union(v, w)
        return mst


def longestPalindrome(s):
    if len(s) <= 1:
        return s
    max_palin = s[0]
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left+1: right]
    
    for i in range(len(s)-1):
        odd = expand(i, i)
        even = expand(i, i+1)
        if len(odd) > len(max_palin):
            max_palin = odd
        if len(even) > len(max_palin):
            max_palin = even
    return max_palin
def convert(s, numRow):
    length = len(s)
    numCol = length
    matrix = [[0]*numCol for i in range(numRow)]
    flag = True
    row_i = 0
    col_i = 0
    result = ''
    for i in range(length):
        matrix[row_i][col_i] = s[i]
        if flag:
            row_i+=1
        else:
            row_i -=1
            col_i +=1
        if row_i == numRow - 1  or row_i == 0:
            flag = not flag
    for row in matrix:
        for item in row:
            if item != 0:
                result += item
    return result

class QuickSort:
    def __init__(self, items_to_sort):
        self.items = items_to_sort
        self.sorted_items=[]
        self.list = self.items[:]
        self.quickSort(self.list, 0, len(self.list)-1)
        self.sorted_items = self.list

    def quickSort(self, arr: [int], lowIndex: int, highIndex: int):
        if lowIndex >= highIndex:
            return 0 #successful
        
        pivot = arr[highIndex]
        leftPointer = lowIndex
        rightPointer = highIndex
        while leftPointer < rightPointer:
            while arr[leftPointer] <= pivot and leftPointer < rightPointer:
                leftPointer += 1
            while arr[rightPointer] >= pivot and rightPointer > leftPointer:
                rightPointer -= 1
            arr[leftPointer],arr[rightPointer] = arr[rightPointer], arr[leftPointer]
        arr[leftPointer],arr[highIndex] = arr[highIndex],arr[leftPointer]

            
        self.quickSort(arr, lowIndex, leftPointer - 1)
        self.quickSort(arr, leftPointer + 1, highIndex)
        

    def get_sorted(self,):
        return self.sorted_items
    




class MergeSort:
    def __init__(self, items_to_sort):
        self.items = items_to_sort
        self.sorted_items=[]
        self.list = self.items[:]
        self.mergeSort(self.list)
        self.sorted_items = self.list

    def mergeSort(self, nums):
        if len(nums) < 2:
            return 0 #ending recursion
        mid_i = len(nums)//2
        lefthalf = nums[:mid_i]
        righthalf = nums[mid_i:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(nums, lefthalf, righthalf)

    def merge(self, result: [int], lhalf: [int], rhalf: [int]):
        lpointer = 0
        rpointer = 0
        fpointer = 0
        while lpointer < len(lhalf) and rpointer < len(rhalf):
            if lhalf[lpointer] < rhalf[rpointer]:
                result[fpointer] = lhalf[lpointer]
                lpointer +=1
            else:
                result[fpointer] = rhalf[rpointer]
                rpointer +=1
            fpointer +=1
        if lpointer >= len(lhalf):
            for i in range(rpointer, len(rhalf)):
                result[fpointer] = rhalf[i]
                fpointer +=1
        else:
            for i in range(lpointer, len(lhalf)):
                result[fpointer] = lhalf[i]
                fpointer +=1
        

    def get_sorted(self,):
        return self.sorted_items
    
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
    

t = Tree(5)
t.add_num(4)
t.add_num(6)
t.add_num(0)
t.add_num(10)
t.add_num(6)


t.print_bt()