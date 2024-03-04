class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sort token (ascending) O(nlogn)
        tokens.sort()

        # Score variables
        max_score = 0
        current_score = 0

        # Loop - until using all token
        while tokens:
            if tokens[0] <= power: # enough power
                # Remove front token
                front_token = tokens.pop(0)

                # Update power
                power -= front_token

                # Update score
                current_score += 1

                # Update max_score
                max_score = max(max_score, current_score)
            else: # not enough power
                if current_score == 0: # no more score
                    # RETURN - Game end
                    return max_score
                else: # have score
                    # Remove last token
                    last_token = tokens.pop()

                    # Update power
                    power += last_token
            
                    # Update score
                    current_score -= 1
        
        # RETURN - max score
        return max_score