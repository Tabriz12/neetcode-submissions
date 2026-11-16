class DynamicArray:
    
    def __init__(self, capacity: int):

        self.arr = [None] * capacity

        self.length = 0


    def get(self, i: int) -> int:

        return self.arr[i]


    def set(self, i: int, n: int) -> None:

        self.arr[i] = n


    def pushback(self, n: int) -> None:

        if self.length == len(self.arr):

            self.resize()

        self.arr[self.length] = n
        self.length +=1



    def popback(self) -> int:

        val = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1

        return val

 
    def resize(self) -> None:

        self.arr += len(self.arr)*[None]


    def getSize(self) -> int:

        return self.length
        
    
    def getCapacity(self) -> int:

        return len(self.arr)