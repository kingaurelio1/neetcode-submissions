class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        def helper(s):
            freq = [0] * 26

            for char in s:
                freq[ord(char) - ord('a')] += 1

            return tuple(freq)

        for word in strs:
            hashmap[helper(word)].append(word)

        return list(hashmap.values())