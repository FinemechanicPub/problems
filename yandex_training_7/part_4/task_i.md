# I. Снеговики[#](https://contest.yandex.ru/contest/74968/problems/I/)

| | |
|---|---|
|Ограничение времени| 4 секунда|
|Ограничение памяти|	64 Мб|
|Ввод|стандартный ввод или input.txt|
|Вывод|стандартный вывод или output.txt|




Зима. 2012 год. На фоне грядущего Апокалипсиса и конца света незамеченной прошла новость об очередном прорыве в областях клонирования и снеговиков: клонирования снеговиков. Вы конечно знаете, но мы вам напомним, что снеговик состоит из нуля или более вертикально поставленных друг на друга шаров, а клонирование — это процесс создания идентичной копии (клона).

В местечке Местячково учитель Андрей Сергеевич Учитель купил через интернет-магазин «Интернет-магазин аппаратов клонирования» аппарат для клонирования снеговиков. Теперь дети могут играть и даже играют во дворе в следующую игру. Время от времени один из них выбирает понравившегося снеговика, клонирует его и:

    либо добавляет ему сверху один шар;
    либо удаляет из него верхний шар (если снеговик не пустой).

Учитель Андрей Сергеевич Учитель записал последовательность действий и теперь хочет узнать суммарную массу всех построенных снеговиков.

## Формат ввода

Первая строка содержит количество действий *n* (1 ≤ *n* ≤ 200 000). В строке номер *i* + 1 содержится описание действия *i*:

t m — клонировать снеговика номер *t* (0 ≤ *t* < *i*) и добавить сверху шар массой *m* (0 < *m* ≤ 1000);

t 0 — клонировать снеговика номер *t* (0 ≤ *t* < *i*) и удалить верхний шар. Гарантируется, что снеговик *t* не пустой.

В результате действия *i*, описанного в строке *i* + 1 создается снеговик номер *i*. Изначально имеется пустой снеговик с номером ноль.

Все числа во входном файле целые.

## Формат вывода

Выведите суммарную массу построенных снеговиков.

## Пример

|Ввод|Вывод|
|---|---|
|   8 | 74 |
| 0 1 |    |
| 1 5 |    |
| 2 4 |    |
| 3 2 |    |
| 4 3 |    |
| 5 0 |    |
| 6 6 |    |
| 1 0 |    |

    
