import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        String originalTime = s.nextLine();
        String newTime;
        if (originalTime.substring(0,2).equals("12"))
            originalTime = "00" + originalTime.substring(2);
        if (originalTime.charAt(8) == 'A')
            newTime = originalTime.substring(0,8);
        else {
            int hours = Integer.parseInt(originalTime.substring(0,2));
            newTime = (hours+12) + originalTime.substring(2,8);
        }
        System.out.println(newTime);
        s.close();

    }
}
