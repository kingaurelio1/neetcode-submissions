class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for word in strs:
            string +=  str(len(word)) + "#" + word
        return string
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            length = word = ''

            while s[i] != '#':
                length += s[i]
                i += 1

            curr = int(length)
            i+=1

            for _ in range(curr):
                word += s[i]
                i += 1

            ans.append(word)

        return ans
