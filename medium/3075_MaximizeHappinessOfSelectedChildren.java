class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness); //sort array

        long ans = 0;
        long time = 0;

        for(int i = 0; i < k && i < happiness.length; i++)
        {
            ans += Math.max(happiness[happiness.length - 1 - i] - time, 0); //add children backwards 
            time++;
        }
        return ans;
    }
}
