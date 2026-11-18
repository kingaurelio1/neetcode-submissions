class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        def aux(s):
            freq = [0] * 26
            
            for i in s:
                freq[ord(i) - ord('a')] += 1

            return tuple(freq)

        for word in strs:
            hashmap[aux(word)].append(word)

        return list(hashmap.values())