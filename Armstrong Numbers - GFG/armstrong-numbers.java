//{ Driver Code Starts
//Initial Template for Java
import java.util.*;
import java.io.*;
class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(read.readLine());
            Solution ob = new Solution();

            System.out.println(ob.armstrongNumber(n));
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution {
    static String armstrongNumber(int n){
        // code here
        String s= Integer.toString(n);
        int len=s.length();
        int len_outer=s.length();
        int num=n;
        int digit=0;
        int cube=1;
        int sum=0;
        
        while(len_outer>0){
            digit=num%10;
            num=num/10;
            int start=0;
            cube=1;
            while(start<len){
                cube=digit*cube;
                start++;
            }
            sum=sum+cube;
            len_outer--;
        }
        if(sum==n){
            return "Yes";
        }
        else{
            return "No";
        }
    }
    
}