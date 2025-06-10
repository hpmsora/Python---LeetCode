class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if not endWord in wordList:
            return 0

        visited = {}

        def isNext(_curr, _next):
            index = 0
            while index < len(_curr):
                if not _curr[index] == _next[index]:
                    return _curr[index+1:] == _next[index+1:]
                index += 1
            return True

        queue = collections.deque([(beginWord, 0)])

        while queue:
            curr_str, step = queue.popleft()
            if curr_str == endWord:
                return step + 1

            for word in wordList:
                if word in visited:
                    visited[word] = min(visited[word], step + 1)
                    continue
                if isNext(curr_str, word):
                    queue.append((word, step+1))
                    visited[word] = step+1
        if endWord in visited:
            return visited[endWord] + 1
        return 0