class Solution:
    def isPalindrome(self, s: str) -> bool:

        #convert all to numbers or lowercase letters using ascii
        charstemp = list(s)
        chars = []
        for c in charstemp:
            if(ord(c) >= 48 and ord(c) <= 57):
                chars.append(c)
            elif(ord(c) >= 97 and ord(c) <= 122):
                chars.append(c)
            elif(ord(c) >= 65 and ord(c)<= 90):
                chars.append(chr(ord(c) + 32))

        #check if the new chars array is a palindrome
        for i in range(0, len(chars) // 2):
            if(ord(chars[i]) != ord(chars[len(chars) - i - 1])):
                return False
                
        return True
