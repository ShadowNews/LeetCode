def invert(s):
    if s == 0:
        s = 1
    else:
        s = 0
    return s
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in image:
            for j in range(len(i)):
                i[j]=invert(i[j])
        k = 0
        for i in image:
            new = i[::-1]
            image[k] = new
            k+=1
        return image



        
