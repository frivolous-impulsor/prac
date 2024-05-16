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
                    
        
    
solution = Solution()
