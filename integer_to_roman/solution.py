class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ITOR_MAP = {
            0: {
                1: 'I',
                4: 'IV',
                5: 'V',
                9: 'IX'
            },
            1: {
                1: 'X',
                4: 'XL',
                5: 'L',
                9: 'XC'
            },
            2: {
                1: 'C',
                4: 'CD',
                5: 'D',
                9: 'CM'
            },
            3: {
                1: 'M'
            }
        }
        
        num = str(num)
        len_num = len(num)
        roman_num = ""
        for i in range(len_num):
            cur_num = int(num[len_num-i-1])
            if cur_num in ITOR_MAP[i]:
                roman_num = ITOR_MAP[i][cur_num] + roman_num
            else:
                tmp = ""
                if cur_num > 5:
                    tmp = ITOR_MAP[i][5]
                    cur_num -= 5
                tmp += ITOR_MAP[i][1] * cur_num
                roman_num = tmp + roman_num
                
        return roman_num
