class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st_dict = {}

        st_dict[t[0]] = -1

        for each_s, each_t in zip(s, t[1:]):
            if not each_s == each_t:
                if each_s in st_dict:
                    st_dict[each_s] += 1
                else:
                    st_dict[each_s] = 1
                
                if each_t in st_dict:
                    st_dict[each_t] -= 1
                else:
                    st_dict[each_t] = -1
                
                if st_dict[each_t] == 0:
                    del st_dict[each_t]
                if st_dict[each_s] == 0:
                    del st_dict[each_s]
        
        for key in st_dict.keys():
            return key