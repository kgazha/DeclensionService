# Сервис склонения #
### localhost/person_name ###
Обязательные поля POST запроса: **fullname, case**

Необязательные: **gender, number**

Пример использования:
```
{
    "fullname": "Сидоров Серега Приколович",
    "case": "datv"
}
```
Результат POST запроса: 
```
{
    "result": "Сидорову Серёге Приколовичу"
}
```

# Общий сервис склонения (для различных слов) #
### localhost/ ###
Обязательные поля POST запроса: **source_text, case**

Необязательные: **gender, number**

Пример использования:
```
{
    "source_text": "кошки",
    "case": "ablt",
    "gender": "femn",
    "number": "plur"
}
```
Результат POST запроса: 
```
{
    "result": "кошками"
}
```

- Описание склонений (case): https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#russian-cases
- Число (number): https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#russian-numbers
- Род (gender): https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#russian-genders
