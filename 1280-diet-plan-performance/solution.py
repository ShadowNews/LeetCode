class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res=0
        window = 0
        for i in range(k):
            window += calories[i]
        if window > upper: 
            res+=1
        elif window < lower:
            res-=1

        for r in range(k,len(calories)):
            window -= calories[r-k]
            window += calories[r]
            if window > upper: 
                res+=1
            elif window < lower:
                res-=1
        return res
