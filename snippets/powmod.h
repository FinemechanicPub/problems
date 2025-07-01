/// @brief Умножение по модулю с защитой от переполнения
/// @tparam T тип чисел
/// @param a первый множитель
/// @param b второй множитель
/// @param mod модуль
/// @return эквивалентно a * b % mod
template<class T = unsigned long long>
T mul_mod(T a, T b, T mod) {    
    if (a > b) std::swap(b, a);
    T result = 0;
    while (a) {
        if (a & 1) result = (result + b) % mod;
        b = 2 * b % mod;
        a >>= 1;
    }
    return result;
}


/// @brief Возведение в целую степень по модулю
/// @tparam T  тип чисел
/// @param base число 
/// @param exp степень
/// @param mod модуль
/// @return экивалентно pow(base, exp) % mod
template<class T = unsigned long long>
T pow_mod(T base, T exp, T mod) {
    T result = 1;
    while (exp) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}