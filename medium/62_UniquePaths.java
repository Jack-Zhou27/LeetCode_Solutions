class Solution {
    public int uniquePaths(int m, int n) {
        return (int)nCr((long)(n - 1 + m - 1), (long)(n - 1));
    }
    public long nCr (long n, long r)
    {
        if(r == 0)
            return 1;

        return (n * nCr(n - 1, r - 1) ) / r; //also realize that: (n/r) (nCr(n - 1, r - 1)) won't work because n/r might give us a decimal that will screw things up
        //return  (factorial(n)) / (factorial(r) * factorial(n - r)); //note we can't use factorial because doing like 100! is way too large.
    }
    public long factorial(long n) //we don't need to use this function
    {
        if(n == 0)
            return 1;
        return n * factorial(n-1);
    }
}
