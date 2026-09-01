class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [4] * n

        last = -n

        for i in range(n):
            if s[i] == c:
                last = i
            ans[i] = i - last

        last = 2 * n

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last = i
            ans[i] = min(ans[i], last - i)

        return ans
