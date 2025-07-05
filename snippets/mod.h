#pragma once

#include <cassert>

#include "powmod.h"


/// @brief Обратный элемент по модулю
/// @tparam T тип чисел
/// @param a число
/// @param mod модуль
/// @return обратный элемент по модулю для _a_
template<class T = long long>
T inv_mod(T x, T mod){
    assert(x < mod);
    return pow_mod(x, mod - 2, mod);
}


/// @brief Деление в поле по модулю
/// @tparam T тип чисел
/// @param a делимое
/// @param b делитель
/// @param mod модуль
/// @return эквиалент (a / b) % mod
template<class T = long long>
T div_mod(T a, T b, T mod) {
    return a * inv_mod(b, mod) % mod;
}