class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        res=0
        while(l<r):
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)

            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return res
