class Solution:
    def frequencySort(self, s: str) -> str:
        # s_dict (key: letter(string) / value: freq(int))
        s_dict = {}
        for each_s in s:
            if each_s in s_dict:
                s_dict[each_s] += 1
            else:
                s_dict[each_s] = 1

        # [(freq(int), key(string)]
        s_list = []

        # dict -> list
        for key, freq in s_dict.items():
            s_list.append((freq, key))

        # list -> sorted list
        s_list.sort(reverse=True)

        # sorted list -> string
        sol = ""
        for freq, key in s_list:
            sol += key * freq
        
        # RETURN
        return sol