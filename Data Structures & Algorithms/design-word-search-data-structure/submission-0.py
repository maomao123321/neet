class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
        
    def search(self, word: str) -> bool:
        def dfs(j,node):
            for i in range(j,len(word)):
                ch = word[i]
                if ch == '.': # 尝试所有分支
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.isEnd
        return dfs(0, self.root)
        
'''
search(word)
如果字符是普通字母：沿着字典树往下走；
如果字符是 '.'：递归尝试所有可能分支；
若能找到某条路径且结尾 isEnd == True, 返回 True。
'''

        
