class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #edge case
        if(len(flowerbed) == 1):
            if(flowerbed[0] == 0):
                return bool(1 >= n)
            return bool(0 >= n)

        #solution
        count = 0
        i = 0
        while(i < len(flowerbed)):
            if(i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0): #index = 0, just check the right pos
                count += 1
                i += 1
            elif(i + 1 < len(flowerbed) and flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0): #index is in-between, check left and right pos
                count += 1
                i += 1
            elif(i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0): #index = len(flowerbed) - 1, then just check the left pos
                count += 1
                i += 1
                
            i += 1
        return bool(count >= n)
