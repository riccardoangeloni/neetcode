class Solution:
    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        n = len(s)

        while i < n:
            delim = s.find("#", i)
            
            length = int(s[i:delim])
            
            start = delim + 1
            end = start + length
            l.append(s[start:end])
            
            i = end

        return l
