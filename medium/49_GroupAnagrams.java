class Solution {
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String word : strs)
        {
            //if the key doesn't exist, we add it and intialize a new list for the values
            if(!map.containsKey(sortedWord(word)))
                map.put(sortedWord(word), new ArrayList<>());
            
            //add the word to its corresponding key 
            map.get(sortedWord(word)).add(word);
        }
        return new ArrayList<>(map.values());
    }
    public String sortedWord(String s)
    {
        char[] temp = s.toCharArray();
        Arrays.sort(temp);
        String ans = "";
        for(int i = 0; i < temp.length; i++)
            ans += temp[i] + "";
        return ans;
    }
}
