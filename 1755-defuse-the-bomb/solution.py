class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res=[]
        window = 0
        n = len(code)
        if k>0:
            for i in range(abs(k)):
                window += code[i]
            for i in range(k,k+n):
                window += code[i%n]
                window -= code[(i-k)%n]
                res.append(window)
        elif k == 0:
            for i in range(n):
                res.append(0)
        else:
            window = sum(code[(n-abs(k)):n])
            for i in range(k,k+n):
                res.append(window) 
                window -= code[i%n]
                window += code[(i-k)%n]
                
        return res
