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
    text = pytesseract.image_to_string(gray, lang="eng")
    return  text
