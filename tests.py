import unittest
from handlers.declension_handler import DeclensionHandler
from casing_manager import get_words_casing, apply_words_cases, apply_cases


class DeclensionHandlerTest(unittest.TestCase):

    def test_inflected_text(self):
        text_handler = DeclensionHandler()
        source_text = "Иванов Иван Иванович"
        case = "gent"
        result = text_handler.get_inflected_text(source_text, case)
        expected_result = "Иванова Ивана Ивановича"
        self.assertEqual(expected_result, result)

    def test_complex_name(self):
        text_handler = DeclensionHandler()
        source_text = "Южно-Уральский торгово-промышленный"
        case = "datv"
        number = "plur"
        result = text_handler.get_inflected_text(source_text, case=case, number=number)
        expected_result = "Южно-Уральским торгово-промышленным"
        self.assertEqual(expected_result, result)

    def test_inflected_person_name_by_fullname(self):
        text_handler = DeclensionHandler()
        source_text = "Иванов Иван Иванович"
        case = "datv"
        result = text_handler.get_inflected_person_name(case, fullname=source_text)
        expected_result = "Иванову Ивану Ивановичу"
        self.assertEqual(expected_result, result)

    def test_female_case(self):
        text_handler = DeclensionHandler()
        fullname = "Шишь Алёна Алексеевна"
        case = "datv"
        result = text_handler.get_inflected_person_name(case, fullname=fullname)
        expected_result = "Шишь Алёне Алексеевне"
        self.assertEqual(expected_result, result)

        fullname = "Сидорова Ольга Ларисовна"
        result = text_handler.get_inflected_person_name(case, fullname=fullname)
        expected_result = "Сидоровой Ольге Ларисовне"
        self.assertEqual(expected_result, result)

    def test_inflected_person_separated_name_parts(self):
        text_handler = DeclensionHandler()
        name = "Алёна"
        surname = "Охременко"
        case = "datv"
        result = text_handler.get_inflected_person_name(case, name=name, surname=surname)
        expected_result = "Охременко Алёне"
        self.assertEqual(expected_result, result)

    def test_empty_name(self):
        text_handler = DeclensionHandler()
        case = "datv"
        result = text_handler.get_inflected_person_name(case)
        expected_result = ""
        self.assertEqual(expected_result, result)


class CaseTests(unittest.TestCase):

    def test_get_words_casing(self):
        text = "HelLo WoRlD"
        result = get_words_casing(text.split())
        expected_result = [[False, True, True, False, True],
                           [False, True, False, True, False]]
        self.assertEqual(expected_result, result)

    def test_apply_words_cases(self):
        text = "HelLo WoRlD"
        new_text = "hello, world!"
        words_cases = get_words_casing(text.split())
        expected_result = ["HelLo,", "WoRlD!"]
        result = apply_words_cases(new_text.split(), words_cases)
        self.assertEqual(expected_result, result)

    def test_apply_cases(self):
        source_text = "ООО Пельмень Иван"
        target_text = "ооо пельменю ивану"
        expected_result = "ООО Пельменю Ивану"
        result = apply_cases(source_text, target_text)
        self.assertEqual(expected_result, result)
