class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n, s_set = len(s), set()
        PRIME, MOD = 11, int(1e9+7)
        for i in range(n):
            cnt = [0] * 10
            unique = max_cnt = s_hash = 0
            for j in range(i, n):
                digit = ord(s[j]) - ord('0')
                unique += 1 if cnt[digit] == 0 else 0
                cnt[digit] += 1
                max_cnt = max(max_cnt, cnt[digit])
                s_hash = (s_hash * PRIME + digit + 1) % MOD
                if max_cnt * unique == j - i + 1:
                    s_set.add(s_hash)
        return len(s_set)