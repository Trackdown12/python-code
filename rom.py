
def romanToInt(self, s: str) -> int:
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    a=0
    for i in range(len(s)):
        if (i<len(s)-1 and d[s[i+1]]>d[s[i]]):
            a-=d[s[i]]
        else:
            a+=d[s[i]]
    return a

        