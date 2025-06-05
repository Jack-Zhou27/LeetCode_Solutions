class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {

        //init
        vector<char> alphabet(26); //alphabet[0] = 'a' ... alphabet[25] = 'z'
        for(int i = 0; i < 26; i++){
            alphabet[i] = char(97 + i);
        }

        for(int i = 0 ; i < s1.size(); i++){
            int indx1 = int(s1[i] - 97);
            int indx2 = int(s2[i] - 97);

            //update
            char newChar = min(alphabet[indx1], alphabet[indx2]);
            char oldChar = max(alphabet[indx1], alphabet[indx2]);
            for(int j = 0; j < 26; j++){
                if(alphabet[j] == oldChar){
                    alphabet[j] = newChar;
                }
            }
        }

        //algo 
        string ans = "";
        for(int i = 0; i < baseStr.size(); i++){
            ans += alphabet[int(baseStr[i] - 97)];
        }

        return ans;
    }
};
