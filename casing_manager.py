from typing import List


def get_words_casing(words: List[str]) -> List[List[bool]]:
    words_cases = []
    for word in words:
        letter_cases = []
        for letter in word:
            if letter.islower():
                letter_cases.append(True)
            else:
                letter_cases.append(False)
        words_cases.append(letter_cases)
    return words_cases


def apply_words_cases(words: List[str], words_cases: List[List[bool]]) -> List[str]:
    new_words = []
    for (w_idx, word) in enumerate(words):
        new_word = ""
        word_cases = None
        for (l_idx, letter) in enumerate(word):
            if w_idx < len(words_cases):
                word_cases = words_cases[w_idx]
            if word_cases and l_idx < len(word_cases):
                new_word += letter.lower() if word_cases[l_idx] else letter.upper()
            else:
                new_word += letter
        new_words.append(new_word)
    return new_words


def apply_cases(source_text: str, target_text: str, sep: str = " ") -> str:
    words_cases = get_words_casing(source_text.split(sep))
    result = apply_words_cases(target_text.split(sep), words_cases)
    return sep.join(result)
