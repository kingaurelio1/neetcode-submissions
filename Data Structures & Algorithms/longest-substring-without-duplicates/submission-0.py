class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated = set()
        left = ans = 0
        for right, letter  in enumerate(s):
            while letter in repeated:
                repeated.remove(s[left])
                left += 1
            
            repeated.add(letter)
            ans = max(ans, right - left + 1)

        return ans