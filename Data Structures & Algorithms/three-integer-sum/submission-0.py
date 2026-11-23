class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            target = - nums[i]

            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]: 
                        left += 1

                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1

                else:
                    right -= 1

        return ans
