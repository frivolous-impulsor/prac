import random


class SortingAlgos:
    def __init__(self) -> None:
        pass
    def randList(self, size: int):
        return [random.randint(0,size**2) for _ in range(size)]
    
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
    
    def quickSort(self, arr, lo, hi):
        if lo >= hi:
            return 
        pivot = arr[hi]
        lp = lo
        rp = hi
        while lp < rp:
            while arr[lp] <= pivot and lp < rp:
                lp +=1

            while arr[rp] >= pivot and lp < rp:
                rp -=1
            arr[lp], arr[rp] = arr[rp], arr[lp]
        arr[lp], arr[hi] = arr[hi], arr[lp]
        #the pivot is now at the final location of index lo
        #recursively sort subarray before pivot and after pivot
        self.quickSort(arr, lo, lp-1)
        self.quickSort(arr, lp+1, hi)           

instance = SortingAlgos()
randlist = instance.randList(1000)
#randlist = [8,2,6,3,9,5]
instance.quickSort(randlist, 0, len(randlist)-1)
print(instance.isSorted(randlist))

