class Solution:
    def isNumber(self, s: str) -> bool:
        # Number only set
        num_set = {
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
        }

        # Sign check
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
            if len(s) == 0: # only sign check
                return False
            
        # Only dot check
        if s == '.':
            return False

        # Loop - each letter in s:
        isDot = False # Dot duplication check
        for index in range(len(s)):
            # Each s
            each_s = s[index]

            # Sign check (expecpt after e)
            if each_s == '+' or each_s == '-':
                return False

            # . check
            elif each_s == '.':
                if isDot: # Has dot before
                    return False
                else: # First dot
                    isDot = True
            
            # e check
            elif each_s == 'e' or each_s == 'E':
                # First e check
                if index == 0:
                    return False

                # Previous number check
                if not s[index - 1] in num_set:
                    if not s[index - 1] == ".":
                        return False
                    else:
                        if index-1 > 0:
                            if s[index-2] in num_set:
                                pass
                        else:
                            return False
                
                # last index check
                if index == len(s) - 1:
                    return False

                # Sign check (after e)
                index += 1
                if s[index] == '+' or s[index] == '-':
                    index += 1
                    # after sign last index check
                    if index > len(s) - 1:
                        return False
                
                # Loop - rest of num need to be integer
                while index < len(s):
                    each_s = s[index]
                    if not each_s in num_set:
                        return False
                    index += 1
                return True # Integer pass
            
            # Number check
            elif not each_s in num_set:
                return False

        # All pass
        return True