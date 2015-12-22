#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

// returns the index of the first number closest to x using binary search from A[i] to A[N]

int closest(int A[], int N, int i, int x) {
    int low = i, mid, high = N-1;
    while (high - low > 1) {
        mid = (int) floor((high + low)/2);
        if (A[mid] < x) low = mid;
        else high = mid;
    }
    if (x - A[low] <= A[high] - x) {
        return low;
    }
    return high;
}

int upperLim(int A[], int N, int i, int x) {
    int low = i, mid, high = N-1;
    while (high - low > 1) {
        mid = (int) floor((high + low)/2);
        if (A[mid] < x) low = mid;
        else high = mid;
    }
    return high-1;
}


int main(){
    int N;
    cin >> N;
    int A[N];
    for(int A_i = 0;A_i < N;A_i++){
       cin >> A[A_i];
    }
    // your code goes here
    int acute_count = 0, right_count = 0, obtuse_count = 0;

    // O((N^2)log(N))?
    // Pick three sides
    // first side loop i: 0->n-2
    for (int i = 0; i < N-2; i++) {
        // second side loop j: i+1->n-1
        for (int j = i+1; j < N-1; j++) {
            int c = closest(A, N, j+1, sqrt(A[i]*A[i] + A[j]*A[j]));
            // cout << "Closest element to " << A[i]*A[i] << " & " << A[j]*A[j] << " is " << A[c]*A[c] << " at index " << c;
            int limit = 0;
            if (A[N-1] < A[i] + A[j]) {
                limit = N-1;
            }
            else {
                limit = upperLim(A, N, j, A[i]+A[j]);
            }
            double a2b2sum = sqrt(A[i]*A[i] + A[j]*A[j]);
            // Case 1: closest element is hypotenuse of right
            if ((double)A[c] == a2b2sum) {
                // cout << ": Case 1";
                right_count++;
                acute_count += c-j-1;
                obtuse_count += limit-c;
                // cout << " limit, c: " << limit << ", " << c;
                // cout << "; added " << limit-c << " to obtuse_count" <<endl;
            }
            // Case 2: closest element is less than hypotenuse
            else if ((double)A[c] < a2b2sum) {
                // cout << ": Case 2";
                acute_count += c-j;
                obtuse_count += limit-c;
                // cout << " limit, c: " << limit << ", " << c;
                // cout << "; added " << limit-c << " to obtuse_count" <<endl;
            }
            else {
                // cout << ": Case 3";
                acute_count += c-j-1;
                obtuse_count += limit-c+1;
                // cout << " limit, c: " << limit << ", " << c;
                // cout << "; added " << limit-c << " to obtuse_count" <<endl;
            }
        }
    }
    cout << acute_count << " " << right_count << " " << obtuse_count;
    return 0;
}
