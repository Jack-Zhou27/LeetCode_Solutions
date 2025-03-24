class Solution {
    public int checkRecord(int n) {
        int mod = (int)Math.pow(10,9) + 7;

        int dp[][] = new int[2][3];
        dp[0][0] = 1;
        dp[0][1] = 1;
        dp[0][2] = 1;
        dp[1][0] = 1;
        dp[1][1] = 1;
        dp[1][2] = 1;

        for(int i = 1; i <= n; i++)
        {
            int newDP[][] = new int[2][3];
            for(int a = 0; a <= 1; a++)
            {
                for(int l = 0; l <= 2; l++)
                {
                    //pick p and reset l to be 2
                    newDP[a][l] += dp[a][2];
                    newDP[a][l] %= mod;

                    //pick a when we have 1 a unused. Reset l to be 2.
                    if(a == 1)
                    {
                        newDP[a][l] += dp[a - 1][2];
                        newDP[a][l] %= mod;
                    }

                    //pick l
                    if(l > 0)
                    {
                        newDP[a][l] += dp[a][l - 1];
                        newDP[a][l] %= mod;
                    }
                }
            }
            dp = newDP;
        }
        return dp[1][2];
    }
}
//code inspired by: Himanshu Malik
