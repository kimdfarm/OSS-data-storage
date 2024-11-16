from deep_translator import GoogleTranslator
from langdetect import detect
import random
from concurrent.futures import ThreadPoolExecutor


def mixString(sentence):
    # 번역할 문장
    lam = sentence.split(" ")

    # 지원되는 언어 코드 리스트 (목표 언어 목록)
    languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW',
                 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu',
                 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km',
                 'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn',
                 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si',
                 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'uz',
                 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

    # 입력 문장의 각 단어의 소스 언어 자동 감지
    source_languages = []
    for word in lam:
        # 단어가 한 글자이거나 특수 문자일 경우 감지 제외
        if len(word) > 1 and any(c.isalpha() for c in word):
            detected_language = detect(word)
        else:
            detected_language = 'org'
        source_languages.append(detected_language)

    # 단어별로 무작위 언어로 번역하기
    translated_lankey = []
    translated_value = []
    for index, word in enumerate(lam):
        # 무작위 목표 언어 선택
        target_language = random.choice(languages)

        # 번역 시도
        try:
            if source_languages[index] != 'org':  # 감지된 언어가 있는 경우에만 번역
                translated_word = GoogleTranslator(source=source_languages[index], target=target_language).translate(word)
                translated_lankey.append(f"{target_language}")
                translated_value.append(f"{translated_word}")
            else:
                translated_lankey.append("org")
                translated_value.append(word)

        except Exception as e:
            print("")
    # 결과 반환
    return translated_lankey, translated_value, source_languages

# 리스트 아닌 문자열 추출
def mixStr(S):
    translated_lankey, translated_value, source_languages = mixString(S)
    summix = " ".join(translated_value)
    return summix

# 리스트 형식의 믹싱된 문자 추출
def mixStList(S):
    translated_lankey, translated_value, source_languages = mixString(S)
    return translated_value

# 리스트의 어느 나라 언어인지 알림
def mixStLan(S):
    translated_lankey, translated_value, source_languages = mixString(S)
    return translated_lankey
