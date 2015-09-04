import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        // Uses two runners to determine the left sum and right sum at each index
        // if they match, return "YES"; if they never match, return "NO"
        // Memory and runtime are O(n)
        Scanner s = new Scanner(System.in);
        int i = 0, cases = s.nextInt();
        while (i < cases) {
            String result = "NO";
            int size = s.nextInt(), leftSumRunner = 0, rightSumRunner = 0;
            int[] array = new int[size], leftSums = new int[size], rightSums = new int[size];
            // Step 1: Get input
            for (int j = 0; j < size; j++) {
                array[j] = s.nextInt();
            }
            // Step 2: Start runners
            for (int k = 0; k < size; k++) {
                leftSumRunner+=array[k];
                rightSumRunner+=array[size-1-k];
                leftSums[k] = leftSumRunner;
                rightSums[size-1-k] = rightSumRunner;
            }
            // Step 3: Check for index with matching sums
            for (int l = 0; l < size; l++) {
                if (leftSums[l]==rightSums[l])
                    result = "YES";
            }
            System.out.println(result);
            i++;
        }
    }
}
