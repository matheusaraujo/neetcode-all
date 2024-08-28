#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def getWordPatterns(self, word: str) -> List[str]:
        result = []
        for i in range(len(word)):
            result.append(word[:i] + "*" + word[i+1:])
        return result

    def createNeighbors(self, wordList: List[str]) -> dict:
        neighbors = {}
        for word in wordList:
            for pattern in self.getWordPatterns(word):
                if pattern not in neighbors: neighbors[pattern] = []
                neighbors[pattern].append(word)
        return neighbors

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.append(beginWord)

        neighbors = self.createNeighbors(wordList)

        visited, queue, result = set([beginWord]), deque([beginWord]), 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return result

                for pattern in self.getWordPatterns(word):
                    for newWord in neighbors[pattern]:
                        if newWord not in visited:
                            visited.add(newWord)
                            queue.append(newWord)
            result += 1

        return 0

# @lc code=end

