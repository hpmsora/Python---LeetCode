class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                stack = collections.deque()
                stack.append((left + 1, right, 1))
                stack.append((left, right - 1, 1))
                visited = set()
                visited.add((left + 1, right))
                visited.add((left, right - 1))

                while stack:
                    n_left, n_right, step= stack.popleft()
                    isSol = True

                    while n_left < n_right:
                        if s[n_left] == s[n_right]:
                            n_left += 1
                            n_right -= 1
                        else:
                            isSol = False
                            if step < k:
                                if n_left + 1 <= n_right and not (n_left + 1, n_right) in visited:
                                    visited.add((n_left + 1, n_right))
                                    stack.append((n_left + 1, n_right, step+1))
                                if n_left <= n_right - 1 and not (n_left, n_right - 1) in visited:
                                    visited.add((n_left, n_right - 1))
                                    stack.append((n_left, n_right - 1, step+1))
                                break
                            else:
                                break
                    if isSol:
                        return True
                return False
        return True

                            
