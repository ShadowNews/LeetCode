class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        for i in range(len(colors)):
            if (colors[i%len(colors)]==0 and colors[(i+1)%len(colors)]==1 and colors[(i+2)%len(colors)]==0) or (colors[i]%len(colors)==1 and colors[(i+1)%len(colors)]==0 and colors[(i+2)%len(colors)]==1):
                res += 1
        return res
