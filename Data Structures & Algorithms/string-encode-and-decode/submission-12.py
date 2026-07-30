class Solution:

    def encode(self, strs: List[str]) -> str:
        temp=""
        for i in strs:
            length=str(len(i))
            temp = temp + length
            temp+='#'
            temp+=i
        return temp
    
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            nums=""
            while s[i] !='#':
                nums  =nums + s[i]
                i+=1
            s_len=int(nums)
            i+=1
            res.append(s[i : s_len + i])
            i= i + s_len
        return res



                