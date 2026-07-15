def gcd(a,b):
    while a!=0 and b != 0:
        if a>b:
            a = a%b
        else: 
            b = b%a
    return (a+b)    

class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        M = max(nums)
        
        # dp[g1][g2] = number of ways seq1 has GCD g1, seq2 has GCD g2
        # g=0 means "empty subsequence"
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1  # base case: nothing picked yet, both empty
        
        for x in nums:
            new_dp = [row[:] for row in dp]  # copy = "skip x" case

            for g1 in range(M + 1):
                for g2 in range(M + 1):
                    if dp[g1][g2] == 0:
                        continue
                    
                    # Choice 2: x joins seq1
                    ng1 = gcd(g1, x) if g1 > 0 else x
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + dp[g1][g2]) % MOD
                    
                    # Choice 3: x joins seq2
                    ng2 = gcd(g2, x) if g2 > 0 else x
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + dp[g1][g2]) % MOD

            dp = new_dp           
        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[g][g]) % MOD
        
        return ans
