class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        heapq.heapify(heap)

        ignore_set = set()

        s_list = list(s)

        for index, each_s in enumerate(s):
            if each_s == "*":
                letter_num, n_index = heapq.heappop(heap)
                s_list[index] = ""
                s_list[n_index * -1] = ""
            else:
                letter_num = ord(each_s)
                heapq.heappush(heap, (letter_num, index * -1))
        
        return ''.join(s_list)