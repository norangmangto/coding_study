class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """ 
        res = []
        if not words:
            return res
        
        words_map = {}
        for w in words:
            if w in words_map:
                words_map[w] += 1
            else:
                words_map[w] = 1
        
        s_len = len(s)
        w_cnt = len(words)
        w_len = len(words[0])
            
        i = 0
        while i<s_len-w_len*w_cnt+1:
            tmp_map = dict(words_map)
            for j in range(w_cnt):
                w = s[i+j*w_len:i+j*w_len+w_len]
                if w in tmp_map:
                    if tmp_map[w] == 1:
                        del tmp_map[w]
                    else:
                        tmp_map[w] -= 1
                else:
                    break
                    
            if len(tmp_map) == 0:
                res.append(i)
                
            i += 1

        return res