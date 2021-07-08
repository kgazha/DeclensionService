def get_separated_name(fullname: str) -> [str, str, str]:
    _surname = ""
    _name = ""
    _patronymic = ""
    words = fullname.split()
    words_count = len(words)
    if words_count >= 2:
        _surname = words[0]
        _name = words[1]
        if words_count >= 3:
            _patronymic = words[2]
    return [_surname, _name, _patronymic]
