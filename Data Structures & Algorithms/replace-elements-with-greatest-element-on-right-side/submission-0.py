class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        mas = arr[-1]

        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):

            cur = arr[i]

            arr[i] = mas

            mas = max(mas, cur)
        
        return arr
        



        