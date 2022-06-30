import collections

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque() #list-like container with fast appends and pops on either end
        self.size = size

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.queue.popleft() #if size of max -> pop left
            self.queue.append(val) #append the new value
        else:
            self.queue.append(val) #else just append
        return sum(self.queue)/len(self.queue) #return the sum of the que divided by the number.