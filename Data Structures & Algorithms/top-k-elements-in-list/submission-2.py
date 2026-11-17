class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) 
        counter = Counter(nums)
        buckets = [[] for _ in range(n+1)] 
        ans = []

        for key in counter:
            buckets[counter[key]].append(key)

        for i in range(n,-1,-1):
            if len(ans) == k:
                break

            if buckets[i]:
                for t in buckets[i]:
                    ans.append(t)


        return ans

