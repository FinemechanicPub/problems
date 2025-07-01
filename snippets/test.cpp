#include <iostream>
#include <cmath>

#include "powmod.h"

void test_pow(){
    std::cout << "pow_mod tests" << std::endl;
    const long long MOD = 11;
    int count = 0;
    int failed = 0;
    for (long long base = 1; base < 15; ++base){
        for (long long exp = 0; exp < 11; ++exp){
            auto mod_result = pow_mod(base, exp, MOD);
            auto expected = (long long)(round(pow(base, exp))) % MOD;
            if (mod_result != expected){
                std::cout << base << " ** " << exp << ": " << mod_result << " != " << expected << std::endl; 
                failed++;
            }
            count++;
    
        }
    }
    std::cout << "Test complete " << failed << "/" << count << " failed" << std::endl;
}

void test_mul(){
    std::cout << "mul_mod tests" << std::endl;
    const long long MOD = 11;
    int count = 0;
    int failed = 0;
    for (long long a = 1; a < 15; ++a){
        for (long long b = 0; b < 11; ++b){
            auto mod_result = mul_mod(a, b, MOD);
            auto expected = a * b % MOD;
            if (mod_result != expected){
                std::cout << a<< " * " << b << ": " << mod_result << " != " << expected << std::endl; 
                failed++;
            }
            count++;
    
        }
    }
    std::cout << "Test complete " << failed << "/" << count << " failed" << std::endl;
}


int main(){    
    test_pow();
    test_mul();
}