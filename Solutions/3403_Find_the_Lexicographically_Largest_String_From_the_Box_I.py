class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        heap = []
        heapq.heapify(heap)

        for index, char in enumerate(word):
            char_num = ord(char) * -1
            heapq.heappush(heap, (char_num, index))

        max_length = len(word) - numFriends + 1

        sol = []
        prev_char = heap[0][0]

        while heap:
            char_num, index = heapq.heappop(heap)
            if not char_num == prev_char:
                break
            
            if len(word) - index < max_length:
                new_sub = word[index:]
            else:
                new_sub = word[index:index+max_length]

            #if sol and len(sol[0]) > len(new_sub):
            #    break
            #else:
            sol.append(new_sub)
        return max(sol)