'''
你应该把 Trie 结构分成两层：
一个 TrieNode 类 —— 表示树的一个节点；
一个 PrefixTree 类（或者叫 Trie)—— 表示整棵树。
TrieNode = 一个节点,负责“存数据”,有children,endOfWord
PrefixTree / Trie = 整棵树,负责“提供操作”,有:root(TrieNode)有:insert / search / startsWith 方法
'''
class TrieNode:    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()   # 只初始化一个根节点

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:  
            if char not in cur.children:
                cur.children[char] = TrieNode()  # 如果当前字符不存在，就创建一个子节点
            cur = cur.children[char]   # 指针往下走
        cur.endOfWord = True     

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord    # 只有走到最后，并且这个节点是结尾，才算找到完整单词
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True      # 能走完 prefix，就说明有这个前缀 
