class Solution {
   public List<List<Integer>> subsets(int[] nums) {
       List<Integer> currArray = new ArrayList<>();
       List<List<Integer>> ans = new ArrayList<>();
       backtracking(nums, 0, currArray, ans);
       return ans;
   }
   public static void backtracking(int[] nums, int start, List<Integer> currArray, List<List<Integer>> ans )
   {
       List<Integer> temp = new ArrayList<>(currArray);
       ans.add(temp);
       for(int i = start; i < nums.length; i++)
       {
           currArray.add(nums[i]);
           backtracking(nums, i + 1, currArray, ans);
           currArray.remove(currArray.size() - 1); //remove the last element (the one you put in)
       }
   }
}
