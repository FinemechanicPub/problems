# I. Максимум на подотрезках с добавлением на отрезке<sup>[#](https://contest.yandex.ru/contest/74966/problems/I/)</sup>

| Язык                   | Ограничение времени | Ограничение памяти | Ввод             | Вывод             |
|------------------------|---------------------|--------------------|------------------|-------------------|
| Все языки              | 1.5 секунд          | 512 Мб             | стандартный ввод | стандартный вывод |
| Kotlin 2.1.20 (JRE 21) | 5 секунд            | 512 Мб             | стандартный ввод | стандартный вывод |
| Swift 6.1              | 5 секунд            | 512 Мб             | стандартный ввод | стандартный вывод |
| Python 3.13.2          | 5 секунд            | 512 Мб             | стандартный ввод | стандартный вывод |
| Node.js 22.14.0        | 5 секунд            | 512 Мб             | стандартный ввод | стандартный вывод |

Реализуйте эффективную структуру данных для хранения массива и выполнения следующих операций: увеличение всех элементов данного интервала на одно и то же число; поиск максимума на интервале.

## Формат ввода

В первой строке вводится одно натуральное число N(1 ≤ N ≤ 100000) — количество чисел в массиве.

Во второй строке вводятся N чисел от 0 до 100000 — элементы массива.

В третьей строке вводится одно натуральное число M(1 ≤ M ≤ 30000) — количество запросов.

Каждая из следующих M строк представляет собой описание запроса. Сначала вводится одна буква, кодирующая вид запроса (*m* — найти максимум, *a* — увеличить все элементы на отрезке).

Следом за m вводятся два числа — левая и правая граница отрезка.

Следом за *a* вводятся три числа — левый и правый концы отрезка и число `add`, на которое нужно увеличить все элементы данного отрезка массива (0 ≤ `add` ≤ 100000).

## Формат вывода

Выведите в одну строку через пробел ответы на каждый запрос *m*.

## Пример

| Ввод      | Вывод     |
|-----------|-----------|
| 5         | 4 104 104 |
| 2 4 3 1 5 |           |
| 5         |           |
| m 1 3     |           |
| a 2 4 100 |           |
| m 1 3     |           |
| a 5 5 10  |           |
| m 1 5     |           |

    

