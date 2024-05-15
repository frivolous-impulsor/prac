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
        
        
    
solution = Solution()
print(solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*c"))