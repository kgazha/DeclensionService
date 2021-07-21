from typing import List

import pymorphy2
import config
import models
from fullname_parser import get_separated_name
from casing_manager import apply_cases
from sqlalchemy.orm import sessionmaker

morph = pymorphy2.MorphAnalyzer()
vowels = ['у', 'е', 'ы', 'а', 'э', 'я', 'и', 'ю']


class DeclensionHandler:
    """
    case - падеж (именительный: 'nomn', родительный: 'gent',
                  дательный: 'datv', винительный: 'accs',
                  творительный: 'ablt', предложный: 'loct')
    number - число (единственное: 'sing', множественное: 'plur')
    """
    def get_inflected_text(self, text: str, case: str,
                           number: str = "sing",
                           gender: str = None) -> str:
        words = text.split()
        inflected_words = []
        session = sessionmaker(bind=config.ENGINE)()
        for word in words:
            source_text = models.get_or_create(session, models.Sentence,
                                               source_text=word,
                                               case=case,
                                               gender=gender,
                                               number=number)[0]

            if source_text.result is not None:
                inflected_words.append(source_text.result)
            else:
                inflected_words.append(self._get_inflected_word(word, case, number, gender=gender))
        target_text = " ".join(inflected_words)
        session.commit()
        session.close()
        return apply_cases(text, target_text)

    def get_inflected_person_name(self, case: str, number: str = "sing",
                                  name: str = None, surname: str = None,
                                  patronymic: str = None, fullname: str = None) -> str:
        result_words = []
        _surname, _name, _patronymic = surname, name, patronymic
        if fullname:
            session = sessionmaker(bind=config.ENGINE)()
            source_text = models.get_or_create(session, models.Sentence,
                                               source_text=fullname,
                                               case=case,
                                               number=number)[0]
            if source_text.result is not None:
                return source_text.result
            _surname, _name, _patronymic = get_separated_name(fullname)
        if _name and _surname:
            gender = self._get_gender_by_name(_name)
            _name = self._get_inflected_word(_name, case, number)

            if gender == config.FEMALE and _surname[-1] not in vowels:
                _surname = _surname.lower()
            else:
                _surname = self._get_male_surname(_surname, case, number, gender)
            result_words = [_surname, _name]
            if _patronymic:
                _patronymic = self._get_inflected_word(_patronymic, case, number)
                result_words.append(_patronymic)
        result_words = [x.capitalize() for x in result_words]
        return " ".join(result_words)

    def _get_male_surname(self, surname: str, case: str, number: str = None, gender: str = None) -> str:
        _surname = self._get_inflected_word(surname, case, number, gender)
        if surname.endswith("ов"):
            normal_form = morph.parse(surname)[0].normal_form
            ending = _surname[(len(normal_form)):]
            _surname = surname + ending
        return _surname

    @staticmethod
    def _get_gender_by_name(name: str) -> str:
        _name_parse_obj = morph.parse(name)[0]
        return _name_parse_obj.tag.gender

    @staticmethod
    def _get_inflected_word(word: str, case: str, number: str = None, gender: str = None) -> str:
        _word = morph.parse(word)[0]
        options = {case}
        if number:
            options.add(number)
        if gender:
            options.add(gender)
        _inflected = _word.inflect(options)
        if _inflected:
            return _inflected.word
        else:
            return word
