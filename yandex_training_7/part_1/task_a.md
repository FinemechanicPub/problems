# A. Каждому по компьютеру<sup>[#](https://contest.yandex.ru/contest/74964/problems/A/)</sup>

| | |
|---|---|
|Ограничение|времени 1 секунда|
|Ограничение|памяти	64 Мб|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|


В новом учебном году во Дворец Творчества Юных для занятий в компьютерных классах пришли учащиеся, которые были разбиты на N групп. В i-й группе оказалось X<sub>i</sub>​ человек. Тут же перед директором встала серьезная проблема: как распределить группы по аудиториям. Во дворце имеется M ≥ N аудиторий, в j-й аудитории имеется Y<sub>i</sub>​ компьютеров. Для занятий необходимо, чтобы у каждого учащегося был компьютер и еще один компьютер был у преподавателя. Переносить компьютеры из одной аудитории в другую запрещается. Помогите директору!

Напишите программу для поиска максимального количества групп, которое удастся одновременно распределить по аудиториям, чтобы всем учащимся в каждой группе хватило компьютеров, и при этом остался хотя бы один для учителя.

## Формат ввода

На первой строке входного файла расположены числа N и M (1 ≤ N ≤ M ≤ 1000). На второй строке расположено N чисел — X<sub>1</sub>​, ... , X<sub>N</sub>​ (1 ≤ X<sub>*i*</sub> ≤ 1000 для всех 1 ≤ *i* ≤ N). На третьей строке расположено M чисел Y<sub>1</sub>​, ... , Y<sub>M</sub>​ (1 ≤ Y<sub>*i*</sub>​ ≤ 1000 для всех 1 ≤ *i* ≤ M).

## Формат вывода

Выведите на первой строке число P — количество групп, которое удастся распределить по аудиториям. На второй строке выведите распределение групп по аудиториям — N чисел, i-е число должно соответствовать номеру аудитории, в которой должна заниматься i-я группа. Нумерация как групп, так и аудиторий, начинается с 1. Если i-я группа осталась без аудитории, i-е число должно быть равно 0. Если допустимых распределений несколько, выведите любое из них.

## Пример 1
|Ввод|Вывод|
|---|---|
|1 1| 1 |
|1  | 1 |
|2  |   |


## Пример 2
|Ввод|Вывод|
|---|---|
|1 1| 0 |
|1  | 0 |
|1  |   |
	

