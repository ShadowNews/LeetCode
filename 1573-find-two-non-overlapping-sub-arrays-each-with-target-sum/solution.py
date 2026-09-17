class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        window = 0
        best_len = float("inf")
        best = [float("inf")] * len(arr)
        ans = float("inf")
        l = 0
        for r in range(len(arr)):
            window += arr[r]

            while window > target:
                window -= arr[l]
                l+=1

            if window == target:
                len_string = r-l+1
                
                if l > 0 and best[l - 1] != float("inf"):
                    ans = min(ans, len_string + best[l - 1])
                best_len = min(best_len, len_string)
            best[r] = best_len
        if ans == float("inf"):
            return -1
        return ans
                






    
