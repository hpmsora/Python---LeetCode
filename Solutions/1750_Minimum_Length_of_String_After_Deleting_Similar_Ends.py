class Solution:
    def minimumLength(self, s: str) -> int:
        def find_prefix(s: str) -> (str, str):
            prefix = s[0]
            cut_index = 1
            for each_s in s[1:]:
                if each_s == prefix:
                    cut_index += 1
                else:
                    break
            return (prefix * cut_index, s[cut_index:])
        
        def find_suffix(s: str, prefix: str) -> (str, str):
            cut_index = 0

            for each_s in reversed(s):
                if prefix == each_s:
                    cut_index += 1
                else:
                    break
            return (prefix * cut_index, s[:len(s) - cut_index])
        
        while len(s) >= 2:
            prefix, s = find_prefix(s)

            prefix_letter = prefix[0]

            if not s:
                return 0

            suffix, s = find_suffix(s, prefix_letter)

            if not suffix:
                return len(s) + len(prefix)
            
        return len(s)