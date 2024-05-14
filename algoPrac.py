import random


class SortingAlgos:
    def __init__(self) -> None:
        pass
    def randList(self, size: int):
        return [random.randint(0,size) for _ in range(size)]
    
    def isSorted(self, list: list[int]):
        for i in range(len(list) -1 ):
            if list[i] > list[i+1]:
                return False
        return True
    
    def insertionSort(self, list: list[int]):
        for i in range(1, len(list)):
            key = list[i]
            while i>=1 and list[i-1] > key:
                list[i], list[i-1] = list[i-1], list[i]
                i -=1
        return list
        

instance = SortingAlgos()
randlist = instance.randList(10)
print(instance.insertionSort(randlist))

