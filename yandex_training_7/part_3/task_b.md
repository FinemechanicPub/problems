# B. Миссия джедая Ивана[#](https://contest.yandex.ru/contest/74967/problems/B/)

| | |
|---|---|
|Ограничение времени| 1 секунда|
|Ограничение памяти|	256 Мб|
|Ввод|стандартный ввод|
|Вывод|стандартный вывод|

Юный джедай Иван был заброшен на Звезду Смерти с заданием уничтожить её. Для того, чтобы уничтожить Звезду Смерти, ему требуется массив неотрицательных целых чисел *a*<sub>*i*</sub>​ длины N. К сожалению, у Ивана нет этого массива, но есть секретный документ с требованиями к этому массиву, который ему передал его старый друг Дарт Вейдер.

В этом документе содержится квадратная матрица *m* размера N, где элемент в *i*-й строке в *j*-м столбце равен побитовому "И" чисел *a*<sub>*i*</sub>​ и *a*<sub>*j*</sub>​. Для повышения безопасности главная диагональ матрицы была уничтожена и вместо чисел на ней были записаны нули. Помогите Ивану восстановить массив a и выполнить свою миссию.

Гарантируется, что решение всегда существует. Если решений несколько, выведите любое.

## Формат ввода

В первой строке содержится число N (1 ≤ N ≤ 1000) — размер матрицы.

Каждая из последующих N строк содержит по N целых чисел *m*<sub>*ij*</sub>​ (0 ≤ *m*<sub>*ij*</sub> ≤ 9) — элементы матрицы.

## Формат вывода

В единственной строке выведите N целых неотрицательных чисел, не превышающих 100100 — требуемый массив *a*.

## Пример 1
|Ввод|Вывод|
|---|---|
|     3 | 1 1 1  |
| 0 1 1 |        |
| 1 0 1 |        |
| 1 1 0 |        |

## Пример 2
|Ввод|Вывод|
|---|---|
|         5 | 1 2 3 1 3  |
| 0 0 1 1 1 |            |
| 0 0 2 0 2 |            |
| 1 2 0 1 3 |            |
| 1 0 1 0 1 |            |
| 1 2 3 1 0 |            |

    


