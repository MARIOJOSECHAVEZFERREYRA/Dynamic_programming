class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        n1, n2 = len(word1), len(word2)
        n = min(n1, n2)
        for i in range(n):
            result += word1[i] + word2[i]
            if n1 == n2:
                return result
            elif n1 > n2:
                return result + word1[n:]
            else:
                return result + word2[n:]

sol = Solution()
print(sol.mergeAlternately("hello", "world"))