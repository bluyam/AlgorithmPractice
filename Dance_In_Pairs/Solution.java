import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        int n = 0, maxPairs = 0, numRem = 0;
        long k = 0;
        Scanner s = new Scanner(System.in);
        n = s.nextInt();
        k = s.nextLong();
        ArrayList<Long> boyHeights = new ArrayList<Long>(n);
        for (int i = 0; i < n; i++) {
            boyHeights.add(s.nextLong());
        }
        ArrayList<Long> girlHeights = new ArrayList<Long>(n);
        for (int i = 0; i < n; i++) {
            girlHeights.add(s.nextLong());
        }
        Collections.sort(boyHeights);
        Collections.sort(girlHeights);
        for (int i = 0, j = 0; i < n && j < n;) {
            if (Math.abs(boyHeights.get(i)-girlHeights.get(j))<=k) {
                i++;
                j++;
                maxPairs++;
            }
            else if (boyHeights.get(i)-girlHeights.get(j)<0) {
                i++;
            }
            else j++;
        }
        System.out.println(maxPairs);
    }
}
