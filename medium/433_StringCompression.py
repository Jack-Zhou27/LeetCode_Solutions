class Solution:
    def compress(self, chars: List[str]) -> int:
        #algorithm: two pointers
        l = 0
        r = 1
        temp = []
        while r < len(chars):
            if chars[l] != chars[r]:
                temp.append(chars[l])
                if r - l > 1:
                    for c in str(r - l):
                        temp.append(c)
                l = r
            r += 1
        
        #take into account the final append 
        temp.append(chars[l])
        if r - l > 1:
            for c in str(r - l):
                temp.append(c)
    
        #assign values of temp to chars
        i = 0
        while i < len(temp) and i < len(chars):
            chars[i] = temp[i]
            i += 1
        while i < len(chars):
            chars.pop()

        return len(chars)
       
