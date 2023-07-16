//{ Driver Code Starts
//Initial Template for Java


import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            int N = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.evenlyDivides(N));
        }
    }
}
// } Driver Code Ends


//User function Template for Java


class Solution{
    public static int evenlyDivides(int N){
        // code here
        String s=Integer.toString(N);
        int len= s.length();
        int digit=0;
        int num=N;
        int count=0;
        
        while(len>0){
            digit=num%10;
            num=num/10;
            if(digit!=0 && N%digit==0){
                count++;
            }
            len--;
        }
        return count;
    }
}