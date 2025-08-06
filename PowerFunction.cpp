// Description: Compute x^n using recursive halving

#include <iostream>
using namespace std;

double power(double x, int n) {
    if (n == 0) return 1.0;

    double half = power(x, n/2);

    if(n % 2 == 0) return half * half;
    else return x * half * half;

}

int main(){
    double x;
    int n;

    cout << "Enter the base number: ";
    cin >> x;

    cout << "Enter the power value: ";
    cin >> n;

    double result = power(x , n);
    cout << "Result: "<<result << endl;

}



// Input:
// Enter the base number: 2
// Enter the power value: 10

// Output:
// Result: 1024