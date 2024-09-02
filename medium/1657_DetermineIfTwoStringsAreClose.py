class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        #deternmine if the words have the same alphabet
        alphabet1 = set(word1)
        for c in word2:
            if c not in alphabet1:
                return False
                
        #deternmine the frequency of each elements
        freq1 = {}
        for c in word1:
            if c in freq1:
                freq1[c] += 1
            else:
                freq1[c] = 1

        freq2 = {}
        for c in word2:
            if c in freq2:
                freq2[c] += 1
            else:
                freq2[c] = 1
        
        #check if the frequency of word1 and word2 are equal 
        w1 = freq1.values()
        w2 = freq2.values()
        freq = {}
        for i in w1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for i in w2:
            if i not in freq or freq[i] == 0:
                return False
            else:
                freq[i] -= 1
        return True
        
        
