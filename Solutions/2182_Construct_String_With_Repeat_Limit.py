class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count frequencies of each character
        freq = Counter(s)
        
        # Use a max heap (negative frequencies for max heap simulation)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))  # Store (negative ASCII value, count)
        
        result = []  # Final result list
        while max_heap:
            # Extract the largest character
            neg_char, count = heapq.heappop(max_heap)
            char = chr(-neg_char)
            
            # Determine how many times we can use this character (up to repeatLimit)
            use_count = min(count, repeatLimit)
            result.extend([char] * use_count)
            
            count -= use_count  # Remaining count after usage
            
            if count > 0:  # If there are more of this character left
                if not max_heap:
                    break  # No other characters to use, we are done
                    
                # Extract the second largest character to "break" the sequence
                neg_next_char, next_count = heapq.heappop(max_heap)
                next_char = chr(-neg_next_char)
                
                # Use the second largest character once to break the sequence
                result.append(next_char)
                next_count -= 1  # Update the count
                
                # Push both characters back into the heap if they still have remaining counts
                heapq.heappush(max_heap, (neg_char, count))
                if next_count > 0:
                    heapq.heappush(max_heap, (neg_next_char, next_count))
        
        # Join the list into the final string
        return "".join(result)