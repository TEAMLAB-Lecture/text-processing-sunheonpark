#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    copy_string = input_string
    lower_string = copy_string.lower()
    string_list = lower_string.split(" ")
    result_string = []
    for string in string_list:
        if string != "":
            result_string.append(string.strip())

    normalized_string = " ".join(result_string)
    return normalized_string


def no_vowels(input_string):
    no_vowel_string = ""
    for string_char in input_string:
        if string_char not in ["a", "e", "i", "o", "u"]:
            no_vowel_string += string_char

    return no_vowel_string
