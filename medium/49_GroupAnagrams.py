class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
       #create a dictionary (a hashmap) of each key corresponding to a list of values
       map = collections.defaultdict(list)

       #''.join(sorted(s) standardizes each string to see if it is an anagram
       #we add the word (a value) to its corresponding key in the hashmap
       for s in strs:
            map[''.join(sorted(s))].append(s)
    
       return map.values()
       
