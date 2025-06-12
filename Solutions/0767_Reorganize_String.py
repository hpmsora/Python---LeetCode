class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Find freq each letter
        freq_dict = {}
        for letter in s:
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1
        # 2. Sort by freq
        heap = []
        heapq.heapify(heap)
        for key, freq in freq_dict.items():
            heapq.heappush(heap, (-1 * freq, key))
        
        # 3. Reorganize
        sol = []
        
        while len(heap) > 1:
            freq_1, letter_1 = heapq.heappop(heap)
            freq_2, letter_2 = heapq.heappop(heap)

            sol += [letter_1, letter_2]

            if freq_1 + 1 < 0:
                heapq.heappush(heap, (freq_1 + 1, letter_1))
            if freq_2 + 1 < 0:
                heapq.heappush(heap, (freq_2 + 1, letter_2))
        
        # No more left
        if not heap:
            return "".join(sol)

        # 4. Last letter
        freq, last_letter = heap[0]
        freq *= -1
        if freq > 2:
            return ""
        if freq == 2:
            if not sol:
                return ""
            if sol[-1] != last_letter and sol[0] != last_letter:
                return last_letter + "".join(sol) + last_letter
            else:
                return ""
        if freq == 1:
            if not sol:
                return last_letter
            if sol[-1] != last_letter:
                return "".join(sol) + last_letter
            elif sol[0] != last_letter:
                return last_letter + "".join(sol)
        return ""
