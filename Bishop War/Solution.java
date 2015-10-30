import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static int getNumOfPossibilities(int board[][], int r, int c) {
       int possibilities = 1;
       for (int i = 0; i < r; i++) {
          int emptiesInRow = 0;
          for (int j = 0; j < c; j++) {
             emptiesInRow += board[i][j];
          }
          possibilities*=emptiesInRow; // works assuming there is always one open spot in each row
       }
       return possibilities;
    }

    public static int getNumOfBadConfigs(int board[][], int emptiesInRow[], int r, int c) {

       int numOfBadConfigs = 0;
       int diags = 0;
       for (int i = 0; i < r-1; i++) {
           int badConfigsForDiag = 1;
           // left diags
           for (int j = 0; j < c-1; j++) {
               if (board[i][j] * board[i+1][j+1] == 1) {
               // add the number of possibilities with bishops in this diagonal to the number of possibilities we will remove
               // determined by the product of uninvolved rows' empty spaces

               for (int k = 0; k < r; k++) {
                   if (k != i && k != i+1) badConfigsForDiag*=emptiesInRow[k];
               }
               numOfBadConfigs+=badConfigsForDiag-diags;
               diags++;
               badConfigsForDiag = 1;
               }
           }
           // right diags
           for (int j = 1; j < c; j++) {
               if (board[i][j] * board[i+1][j-1] == 1) {

               for (int k = 0; k < r; k++) {
                   if (k != i && k != i+1) {
                       badConfigsForDiag*=emptiesInRow[k];
                   }
               }
               numOfBadConfigs+=badConfigsForDiag-diags;
               diags++;
               badConfigsForDiag = 1;
               }
           }
       }
       return numOfBadConfigs;
    }

    public static void main(String[] args) throws IOException {

       /* convert input to boolean (represented by int) matrix
       / true/1 represents an empty space
       / false/0 represents an obstacle */

       Scanner s = new Scanner(System.in);
       int r = s.nextInt(), c =  s.nextInt();
       String temp = s.nextLine(); // ensures for loop starts at second line of input
       int[][] board = new int[r][c];
       int[] emptiesInRow = new int[r];
       for (int i = 0; i < r; i++) {
           temp = s.nextLine();
           for (int j = 0; j < c; j++) {
              board[i][j] = temp.charAt(j)=='.' ? 1 : 0;
              emptiesInRow[i] += board[i][j];
           }
       }

       // get number of possible bishop configurations
       System.out.println(getNumOfPossibilities(board, r, c) - getNumOfBadConfigs(board, emptiesInRow, r, c));


    }
}
