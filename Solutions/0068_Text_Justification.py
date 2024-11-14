class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Special Case
        if len(words) == 1:
            return [''.join(words[0]) + " "* (maxWidth - len(words[0]))]
        first_word = words.pop(0)
        line_stack = [first_word]
        line_stack_len = len(first_word)
        sol = []
        while words:
            curr_words = words.pop(0)
            if line_stack_len + len(line_stack)//2 + 1 + len(curr_words) > maxWidth:
                # Make line
                if len(line_stack) == 1:
                    line_stack.append(" "*(maxWidth - line_stack_len))
                else:
                    diff = maxWidth - (line_stack_len + len(line_stack)//2)
                    fixed_extra_spaces = diff // (len(line_stack)//2)
                    diff_remainder = diff % (len(line_stack)//2)

                    each_line = ""
                    index = 0
                    while index < len(line_stack):
                        # Space index
                        if index % 2 == 1:
                            # Fixed extra space
                            line_stack[index] += " "*fixed_extra_spaces
                            if diff_remainder > 0:
                                line_stack[index] += " "
                                diff_remainder -= 1
                        index += 1
                sol.append(''.join(line_stack))

                line_stack = [curr_words]
                line_stack_len = len(curr_words)
            else:
                line_stack += [" ", curr_words]
                line_stack_len += len(curr_words)
        # Last line
        if line_stack:
            # Make line
            line_stack.append(" "*(maxWidth - (line_stack_len + len(line_stack)//2)))
            
            sol.append(''.join(line_stack))
        return sol