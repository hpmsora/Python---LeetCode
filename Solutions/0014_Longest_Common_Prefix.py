class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs.pop(0)

        for each_strs in strs:
            index = 0
            if len(prefix) > len(each_strs):
                prefix = prefix[:len(each_strs)]
            for each_prefix, each_str in zip(prefix, each_strs):
                if not each_prefix == each_str:
                    prefix = prefix[:index]
                index += 1
                print(prefix)
        return prefix