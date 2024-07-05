class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def aux(ps, pp):
            try: headP = p[pp]
            except IndexError: headP = ''
            try: nextP = p[pp+1] 
            except IndexError: nextP = ''
            if len(s) - ps < 1:
                if len(p) - pp < 1:
                    return True
                if nextP == '*':
                    return aux(ps, pp+2)
                else:
                    return False

            headS = s[ps]
            if nextP == '*':
                return ((headS == headP or headP == '.') and aux(ps+1, pp))    or      ((headS == headP or headP == '.') and aux(ps+1, pp+2))       or      (aux(ps, pp+2))
            else:
                return (headS == headP or headP == '.') and aux(ps+1, pp+1)
        return aux(0, 0)

    
    def evaluateTree(self, root: list[int]) -> bool:   
        maxL = len(root)     
        if maxL == 1:
            return root[0]
        def aux(mid):
            leftIdx = mid*2 + 1
            rightIdx = leftIdx + 1
            vLeft = root[leftIdx]
            vRight = root[rightIdx]
            v = root[mid]
            if v < 2:
                return v
            if vLeft < 2:
                if v == 2:
                    return vLeft or vRight
                else:
                    return vLeft and vRight
            else:
                if v == 2:
                    return aux(leftIdx) or aux(rightIdx)
                else:
                    return aux(leftIdx) and aux(rightIdx)
                
        return aux(0)
    
    def minDifference(self, nums: list[int]) -> int:
        def move(trial: int, array):
            array.sort()
            mini: int = array[0]
            maxi: int = array[-1]
            if trial == 0:
                return (maxi - mini)
            listA = [x for x in array]
            listA[0] = listA[-1]
            listB = [x for x in array]
            listB[-1] = listB[0]
            return min(move(trial-1, listA), move(trial-1, listB))
            
        if len(nums) < 5:
            return 0
        return move(3, nums)

    def intToRoman(self, num: int) -> str:
        result: str = ""
        while num >= 1000:
            result = result+'M'
            num -=1000
        #smaller than 1000
        if num >= 900:
            result += "CM"
            num -= 900
        elif num >= 500:
            result += "D"
            num -= 500
        elif num >= 400:
            result += "CD"
            num -= 400
        while num >= 100:
            result += "C"
            num -=100
        #smaller than 100
        if num >= 90:
            result += "XC"
            num -= 90
        elif num >=50:
            result +='L'
            num -=50
        elif num >=40:
            result +='XL'
            num -=40
        while num >= 10:
            result += 'X'
            num -=10
        #smaller than 10
        if num >= 9:
            result += "IX"
            num -= 9
        elif num >=5:
            result +='V'
            num -=5
        elif num >=4:
            result +='IV'
            num -=4
        while num >= 1:
            result += 'I'
            num -=1
        return result
    
    def romanToInt(self, s: str) -> int:
        pointer: int = 0
        result: int = 0
        while pointer < len(s):
            match s[pointer]:
                case 'M':
                    result +=1000
                    pointer +=1
                case 'D':
                    result +=500
                    pointer +=1
                case 'L':
                    result +=50
                    pointer +=1
                case 'V':
                    result +=5
                    pointer +=1
                case 'C':
                    if pointer+1 < len(s):
                        if s[pointer+1] == 'D':
                            result +=400
                            pointer +=2
                        elif s[pointer+1] == 'M' :
                            result +=900
                            pointer +=2
                        else:
                            result +=100
                            pointer +=1
                    else:
                        result +=100
                        pointer +=1
                case 'X':
                    if pointer+1 < len(s):
                        if s[pointer+1] == 'L':
                            result +=40
                            pointer +=2
                        elif s[pointer+1] == 'C' :
                            result +=90
                            pointer +=2
                        else:
                            result +=10
                            pointer +=1
                    else:
                        result +=10
                        pointer +=1
                case 'I':
                    if pointer+1 < len(s):
                        if s[pointer+1] == 'V':
                            result +=4
                            pointer +=2
                        elif s[pointer+1] == 'X' :
                            result +=9
                            pointer +=2
                        else:
                            result +=1
                            pointer +=1
                    else:
                        result +=1
                        pointer +=1
        return result

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        leadStr = strs[0]
        pointer: int = len(leadStr) - 1
        for str in strs:
            prob: int = 0
            while prob <= pointer and prob < len(str) and prob < len(leadStr) and str[prob] == leadStr[prob]:
                prob +=1
            pointer = min(pointer, prob-1)
        if prob == -1:
            return ''
        return leadStr[:pointer+1]


    
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)