// projeuler145.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<string>
using namespace std;
bool has_even_digit(long long n) {
    while (n > 0) {
        int digit = n % 10;
        if (digit % 2 == 0) {
            return true;
        }
        n = n / 10;
    }
    return false;

}
long long reverse(long long n) {
    long long out = 0;
    while (n > 0) {
        out *= 10;
        out += n % 10;
        n = n / 10;
    }
    return out;
}
int main()
{
    long long count = 0;
    long long limit = pow(10, 9);
    long long timer = 10000000;
    for (long long i = 10; i < limit; i++) {
        if (i % timer == 0) {
            std::cout << i;
            std::cout << "\n";
        }
        if (i % 10 != 0) {
            long long r = reverse(i);
            long long x = i + r;
            if (!has_even_digit(x)) {
                count++;
            }
        }
    }

    std::cout << count;
    std::cout << "\n";
    return 0;
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
