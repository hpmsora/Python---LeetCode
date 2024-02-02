class Solution:
    def compress(self, chars: List[str]) -> int:
        edit_index = 0
        index = 1
        prev = chars[0]
        count = 1
        while index < len(chars):
            cur_char = chars[index]
            if prev == cur_char:
                count += 1
            else:
                chars[edit_index] = prev
                edit_index += 1
                if count > 1:
                    for digit in str(count):
                        chars[edit_index] = digit
                        edit_index += 1
                count = 1
                prev = cur_char
            index += 1
        chars[edit_index] = prev
        edit_index += 1
        if count > 1:
            for digit in str(count):
                chars[edit_index] = digit
                edit_index += 1
        del chars[edit_index:]
        
        return len(chars)