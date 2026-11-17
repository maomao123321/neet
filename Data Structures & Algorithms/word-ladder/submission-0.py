class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        l = len(beginWord)
        pattern_map = defaultdict(list) # 创建一个空列表

        for word in wordList:
            for i in range(l):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word) #...

        dq = deque()
        dq.append((beginWord,1))
        visited = set([beginWord])    
        while dq:
            word, level = dq.popleft()
            for i in range(l):
                pattern = word[:i] + "*" + word[i+1:]  # 通过 pattern_map[pattern] 找到所有邻居单词
                neighbors = pattern_map[pattern]
                for nei in neighbors:
                    if nei == endWord:
                        return level+1
                    if nei not in visited:
                        visited.add(nei)
                        dq.append((nei, level+1))

        return 0     