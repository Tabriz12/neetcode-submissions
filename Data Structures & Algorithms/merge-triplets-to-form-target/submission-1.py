class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        x,y,z= target


        u, v, w = False, False, False
        for a,b,c in triplets:

            if any((a > x, b > y, c > z)):
                continue
            
            if a == x:
                u = True

            if b==y:
                v = True

            if z == c:
                w= True


            if u and v and w:

                return True
            
        return False        