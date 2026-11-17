class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return None
        res = []
        dic = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            dic[key].append(word)
        return list(dic.values())

  