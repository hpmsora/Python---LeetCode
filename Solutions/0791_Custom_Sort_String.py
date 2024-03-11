class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # s letter frequency dictionary declare
        s_freq_dict = {}

        # s_freq_dict initialize by order
        for letter_order in order:
            s_freq_dict[letter_order] = 0

        # Remainder letter reserve
        remainder = ""

        # Loop - all letter in s
        for letter in s:
            if letter in s_freq_dict: # order letter
                s_freq_dict[letter] += 1
            else: # non-order letter
                remainder += letter

        # solution declare
        sol = ""

        # Loop - order
        for order_letter in order:
            if order_letter in s_freq_dict: # letter exist
                # Update solution - letter and freqeuncy
                sol += order_letter * s_freq_dict[order_letter]

        # RETURN - solution add with remainder
        return sol + remainder