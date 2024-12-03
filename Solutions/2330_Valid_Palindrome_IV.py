class Solution:
    def makePalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s_list = list(s)
        k = 2

        while left < right:
            if s_list[left] == s_list[right]:
                left += 1
                right -= 1
            else:
                stack = collections.deque([(left+1, right-1, 1)])
                visited = set()
                visited.add((left+1, right))
                visited.add((left, right+1))
                while stack:
                    n_left, n_right, step = stack.popleft()

                    isSol = True
                    while n_left < n_right:
                        if n_right - n_left + step <= k:
                            return True
                        if s_list[n_left] == s_list[n_right]:
                            n_left += 1
                            n_right -= 1
                        else:
                            if step < k:
                                if not (n_left+1, n_right-1) in visited:
                                    stack.append((n_left+1, n_right-1, step + 1))
                                    visited.add((n_left+1, n_right-1))
                            isSol = False
                            break
                    if isSol:
                        return True
                return False
        return True