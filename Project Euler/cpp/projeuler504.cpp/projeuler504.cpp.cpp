// projeuler504.cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
int gcd(int a, int b) {
    while (b > 0){
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
int withinTriangle0xy(int x, int y) {
    int out = x * y - x - y - gcd(x, y) + 2;
    return out / 2;
}

int withinQuad(int a, int b, int c, int d) {
    int out = a + b + c + d - 3;
    out += withinTriangle0xy(a, b);
    out += withinTriangle0xy(a, d);
    out += withinTriangle0xy(c, b);
    out += withinTriangle0xy(c, d);
    return out;
}
int possSquares[150];

void init_squares() {
    for (int i = 0; i < 150; i++) {
        possSquares[i] = (i + 1) * (i + 1);
    }
}
bool isSquare(int x) {
    if (x == 1) {
        return true;
    }
    //binary search the array of squares
    int min = 0;
    int max = 149;
    while (max - min > 1) {
        int mid = (max + min) / 2;
        if (x > possSquares[mid]) {
            int min = mid;
        }
        else if (x < possSquares[mid]) {
            int max = mid;
        }
        else {
            return true;
        }
    }
    return false;

        
}
int main()
{
    int count = 0;
    init_squares();
    int m = 4;
    for (int a = 1; a <= m; a++) {
        for (int b = 1; b <= m; b++) {
            for (int c = 1; c <= m; c++) {
                for (int d = 1; d <= m; d++) {
                    if (isSquare(withinQuad(a, b, c, d))) {
                        count++;
                    }
                }
            }
        }
    }
    std::cout << count;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
