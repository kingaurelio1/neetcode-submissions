class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = m = len(nums)
        freq1 = Counter(nums)
        freq2 = [[] for _ in range(n)]
        ans = [] 

        for key, value in freq1.items():
            freq2[value-1].append(key)

        while k > 0:
            for i in range(len(freq2[m-1])):
                ans.append(freq2[m-1][i])
                k -= 1
            m -= 1

        return ans 
