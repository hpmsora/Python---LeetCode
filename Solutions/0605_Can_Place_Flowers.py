class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(1,len(flowerbed)-1):
            if n==0:
                return True
            else: 
                if flowerbed[i]+flowerbed[i+1]==0 and flowerbed[i-1]!=1:
                    flowerbed[i]=1
                    n-=1
        return n<=0