class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = m = len(nums)
        freq1 = Counter(nums)
        freq2 = [[] for _ in range(n)]
        ans = [] 

        for key, value in freq1.items():
            freq2[value-1].append(key)

        for i in range(len(nums)-1, -1, -1):
            for num in freq2[i]:
                ans.append(num)
                
                if len(ans) == k:
                    return ans
        return ans 
