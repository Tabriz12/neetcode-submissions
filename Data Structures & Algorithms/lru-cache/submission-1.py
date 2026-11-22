
class DoubleLinkedList:

    def __init__(self, key:int = 0, val: int = 0, prev: DoubleLinkedList = None, nxt: DoubleLinkedList = None):

        self.val = val
        self.prev = prev
        self.nxt = nxt
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        self.lp_table = {}
        
        self.start = DoubleLinkedList()

        self.end = DoubleLinkedList(prev=self.start)

        self.start.nxt = self.end

    def get(self, key: int) -> int:


        if key in self.lp_table:


            self.move_forward(key)

            return self.lp_table[key].val
        
        else:
            return -1
        
    

    def move_forward(self, key: int, value = None):

        cur = self.lp_table[key]

        if value is not None:

            cur.val = value
        

        cur.prev.nxt, cur.nxt.prev = cur.nxt, cur.prev

        cur.prev, cur.nxt = self.start, self.start.nxt

        self.start.nxt.prev = self.start.nxt = cur        

    def put(self, key: int, value: int) -> None:

        

        if key in self.lp_table:

            self.move_forward(key, value)
        
        else:


            cur = DoubleLinkedList(key, value, prev = self.start, nxt=self.start.nxt)

            cur.nxt.prev = cur

            self.start.nxt = cur


            self.lp_table[key] = cur

            if self.capacity > 0:

                self.capacity -= 1

            else:

                lru = self.end.prev

                second_last = self.end.prev.prev

                second_last.nxt,  self.end.prev= self.end, second_last
                del self.lp_table[lru.key]         
















        






        
