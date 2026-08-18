from heapq import heapify, heappop, heappush
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        heapify(hand)

        while hand:

            try:
                equals = []
                last = None
                i = 0
                while i < groupSize:

                    val = heappop(hand)


                    if last == None:
                        last = val
                        i+=1
                        
                    
                    elif val == last:
                        equals.append(val)
                        
                    
                    elif val == last+1:
                        last = val
                        i+=1
                    
                    else:
                        return False
                

                
                for item in equals:
                    heappush(hand,item)
            
            except IndexError as e:
                return False
        
        return True
            
            
                    
                    