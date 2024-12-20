from googletrans import Translator

translator = Translator()

import cv2
import pytesseract


def image_render(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path)

    # Конвертируем в черно-белое изображение
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Увеличиваем контраст
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Сохраняем предварительно обработанное изображение
    cv2.imwrite("../processed_image.png", gray)

    # Распознаем текст
    words = pytesseract.image_to_string(gray, lang="eng")

    translated_words = []

    if words:
        translation = translator.translate(words, src="en", dest="ru").text
        return f"{words} - {translation}"
    # for word in words:
    #     word = word.strip()  # Убираем лишние пробелы
    #     if word:
    #         translation = translator.translate(word, src="en", dest="ru").text
    #         translated_words.append(f"{word} - {translation}")
    #
    # return translated_words



def translate_func(file_path : str):
# Скачиваем файл
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.readlines()

    # Переводим слова
    translated_words = []
    for word in words:
        word = word.strip()  # Убираем лишние пробелы
        if word:
            translation = translator.translate(word, src="en", dest="ru").text
            translated_words.append(f"{word} - {translation}")

    return translated_words

def translate_text(words ):
    # Переводим слова
    translated_words = []

    if words in " ":
        translation = translator.translate(words, src="en", dest="ru").text
        return f"{words} - {translation}"
    for word in words:
        word = word.strip()  # Убираем лишние пробелы
        if word:
            translation = translator.translate(word, src="en", dest="ru").text
            translated_words.append(f"{word} - {translation}")

    return translated_words

