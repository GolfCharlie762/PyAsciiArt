
# AsciiArtConverter

## Описание
`AsciiArtConverter` — это Python-библиотека для преобразования изображений в ASCII-арт. Она позволяет изменять параметры ширины, детализации, набора символов и просматривать результат в текстовом окне.

## Возможности
- Конвертация изображений в ASCII-арт.
- Настройка параметров (ширина, детализация, набор символов и т. д.).
- Сохранение ASCII-арта в файл.
- Просмотр результата в графическом интерфейсе.

---

# AsciiArtConverter

## Description
`AsciiArtConverter` is a Python library for converting images into ASCII art. It allows customization of width, detail level, character set, and provides a preview window.

## Features
- Convert images to ASCII art.
- Adjustable parameters (width, detail, character set, etc.).
- Save ASCII art to a file.
- Preview results in a graphical interface.

---

## Зависимости / Dependencies
- Python 3.7+
- `numpy`
- `Pillow`
- `tkinter` (встроен в стандартную библиотеку Python)

Установите зависимости с помощью команды:

```
pip install numpy pillow
```

---

## Пример использования / Usage Example

### Python-скрипт
```python
from ascii_art_converter import AsciiArtConverter

converter = AsciiArtConverter()
ascii_art = converter.convert("example.jpg")
print(ascii_art)
converter.save_to_file(ascii_art, "output.txt")
```

### Предпросмотр в графическом интерфейсе / GUI Preview
```python
converter.preview_in_window("example.jpg")
```

---

## Автор / Author
Создано для обучения и демонстрации работы с изображениями в Python.

---
