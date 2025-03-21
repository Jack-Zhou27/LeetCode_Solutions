class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        def heapify(i, arr, size): #max heap
            root = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < size and arr[l] > arr[root]:
                root = l
            if r < size and arr[r] > arr[root]:
                root = r
            
            if root != i:
                arr[i], arr[root] = arr[root], arr[i]
                heapify(root, arr, size)
        
        def heapSort(arr):
            n = len(arr)
            
            #build heap
            for i in range(n // 2 - 1, -1, -1):
                heapify(i, arr, n)

            #sort array
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(0 , arr, i)
            
            return arr
        
        #algo
        
        sortedArray = heapSort(nums.copy())
        hashMap = defaultdict(list)
        for i in range(len(nums)):
            if sortedArray[i] in hashMap:
                continue
            else:
                hashMap[sortedArray[i]] = i

        ans = []
        for i in nums:
            ans.append(hashMap[i])
        return ans

            
