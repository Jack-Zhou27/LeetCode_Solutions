class Solution {
    public int[] visited;
    public boolean canReach(int[] arr, int start) {
        visited = new int[arr.length];
        dfs(start, arr); //our dfs builds our visited array, marking which indexes can be reached

        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] == 0 && visited[i] == 1) //as soon as we see one "0" value on the array being reachable, return true like the question asks for 
                return true;
        }
        return false;
    }
    public void dfs(int index, int[] arr)
    {
        if(index >= arr.length || index < 0 || visited[index] == 1) //make sure we don't visit out of bounds or already visited indexes
            return;

        visited[index] = 1; //mark our current index as visited

        dfs(index + arr[index], arr); //go right
        dfs(index - arr[index], arr); //go left
    }
}
