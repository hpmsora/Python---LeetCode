class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26
        res = len(s)
        z = 25
        
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            res = (res + cnt[z]) % MOD
            cnt[(z + 1) % 26] = (cnt[(z + 1) % 26] + cnt[z]) % MOD
            z = (z + 25) % 26
        
        return res