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


int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    for(int A_i = 0;A_i < N;A_i++){
       cin >> A[A_i];
    }
    // your code goes here
    int acute_count = 0, right_count = 0, obtuse_count = 0;

    // ~O(N^3)
    // Pick three sides
    // first side loop i: 0->n-2
    for (int i = 0; i < A.size()-2; i++) {
        // second side loop j: i+1->n-1
        for (int j = i+1; j < A.size()-1; j++) {
            // third side loop k: j+1->n and/or while A[k] < A[i]+A[j]
            for (int k = j+1; (k < A.size() && A[k] < A[i]+A[j]); k++) {
                cout << "A[i]: " << A[i] << ", A[j]: " << A[j] << ", A[k]: " << A[k];
                // if acute, acute_count++
                if (A[i]*A[i] + A[j]*A[j] > A[k]*A[k]) {
                  acute_count++;
                  cout << ": acute" << endl;
                }
                // else if right, right_count++
                else if (A[i]*A[i] + A[j]*A[j] == A[k]*A[k]) {
                  right_count++;
                  cout << ": right" << endl;
                }
                // else acute, obtuse_count++
                else { 
                  obtuse_count++;
                  cout << ": obtuse" << endl;
                }
            }
        }
    }
    cout << acute_count << " " << right_count << " " << obtuse_count;
    return 0;
}
