class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_res = ""
        for s in strs:
            encode_res += str(len(s)) + '#' + s
        return encode_res
        4#need4#code4#love3#you

    def decode(self, s: str) -> List[str]:
        decode_res = []
        i = 0
        while i < len(s):
            j = i
            while j<len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j+1
            end = j+length
            string = s[j+1:j+length+1] #python是开右区间
            decode_res.append(string)
            i = end + 1 
        return decode_res
                



