class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        counter_s1 = {}
        counter_s2 = {}
        k = len(s1)
        if len(s1) > len(s2):
            return False
    
        # count the frequency of s1
        for char in s1:
            counter_s1[char] = counter_s1.get(char, 0) + 1

        # count the fre of s2
        for right in range(len(s2)):
            char_in = s2[right]
            counter_s2[char_in] = counter_s2.get(char_in, 0) + 1

            if right - left + 1 > k:
                counter_s2[s2[left]] -= 1
                if counter_s2[s2[left]] == 0:
                    del counter_s2[s2[left]] # 当等于0的时候要删掉！！！！
                left += 1
            
            if right - left + 1 == k:
                if counter_s1 == counter_s2:
                    return True

        return False
         