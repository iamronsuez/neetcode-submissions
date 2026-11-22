from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        length = 0
        words = set(wordList)

        if endWord not in words:
            return length
        
        queue = deque([beginWord])

        while queue:
            length += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return length
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]: continue
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in words:
                            words.remove(newWord)
                            queue.append(newWord)

        return 0