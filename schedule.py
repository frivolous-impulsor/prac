from indexed_priority_queue import IndexedPriorityQueue

class Task:
    def __init__(self, tid: int, deadline: int, capacity: int) -> None:
        self.tid = tid
        self.deadline = deadline
        self.capacity = capacity


class ReadyQueue:
    def __init__(self) -> None:
        self.queue = IndexedPriorityQueue()
    
    def addTask(self, t: Task):
        self.queue.push(t, t.deadline)
    
    def isEmpty(self):
        return self.queue.__len__ == 0

    def popTask(self):
        if not self.isEmpty():
            return self.queue.pop()
        else:
            raise Exception("ready queue currently empty")
        
    
class EarliestDeadlineSchedule:
    def __init__(self) -> None:
        self.readyQueue = ReadyQueue()
    
    def 