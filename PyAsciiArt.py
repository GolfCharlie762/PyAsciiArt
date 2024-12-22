import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog, Text

class AsciiArtConverter:
    def __init__(self):
        # Инициализация настроек по умолчанию
        self.settings_dict = {
            "width": 100,             # Ширина ASCII-арта
            "height_ratio": 0.55,    # Коэффициент высоты (для компенсации разного размера символов)
            "charset": "@%#*+=-:. ", # Набор символов для генерации
            "detail": 1.0            # Уровень детализации изображения
        }

    def settings(self, **kwargs):
        """
        Метод для настройки параметров преобразования изображения в ASCII.
        :param kwargs: передаваемые параметры (width, height_ratio, charset, detail)
        """
        for key, value in kwargs.items():
            if key in self.settings_dict:
                self.settings_dict[key] = value
            else:
                raise ValueError(f"Unknown setting: {key}")

    def _resize_image(self, image):
        """
        Приватный метод для изменения размера изображения согласно настройкам.
        :param image: исходное изображение (PIL.Image)
        :return: измененное изображение (PIL.Image)
        """
        width = self.settings_dict["width"]
        height_ratio = self.settings_dict["height_ratio"]
        aspect_ratio = image.height / image.width
        new_height = int(width * aspect_ratio * height_ratio * self.settings_dict["detail"])
        return image.resize((int(width * self.settings_dict["detail"]), new_height))

    def _image_to_grayscale(self, image):
        """
        Приватный метод для перевода изображения в градации серого.
        :param image: исходное изображение (PIL.Image)
        :return: изображение в градациях серого (PIL.Image)
        """
        return image.convert("L")

    def _map_pixels_to_ascii(self, pixels):
        """
        Приватный метод для преобразования пикселей в ASCII-символы.
        :param pixels: массив пикселей (numpy.ndarray)
        :return: строка ASCII-арта
        """
        charset = self.settings_dict["charset"]
        scale = (len(charset) - 1) / 255
        ascii_art = "".join([charset[int(pixel * scale)] for pixel in pixels])
        return ascii_art

    def convert(self, image_path):
        """
        Основной метод для преобразования изображения в ASCII-арт.
        :param image_path: путь к изображению
        :return: ASCII-арт (строка)
        """
        image = Image.open(image_path)
        resized_image = self._resize_image(image)
        grayscale_image = self._image_to_grayscale(resized_image)

        pixels = np.array(grayscale_image).flatten()
        ascii_art = self._map_pixels_to_ascii(pixels)

        # Разделяем ASCII-арт на строки по ширине изображения
        width = int(self.settings_dict["width"] * self.settings_dict["detail"])
        ascii_art_lines = [ascii_art[i:i + width] for i in range(0, len(ascii_art), width)]
        return "\n".join(ascii_art_lines)

    def save_to_file(self, ascii_art, file_path):
        """
        Метод для сохранения ASCII-арта в файл.
        :param ascii_art: строка ASCII-арта
        :param file_path: путь для сохранения файла
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(ascii_art)

    def preview_in_window(self, image_path):
        """
        Метод для предварительного просмотра ASCII-арта в окне с быстрыми настройками.
        :param image_path: путь к изображению
        """
        def update_preview():
            try:
                self.settings(width=int(width_entry.get()), detail=float(detail_entry.get()))
                ascii_art = self.convert(image_path)
                preview_text.delete(1.0, tk.END)
                preview_text.insert(tk.END, ascii_art)
            except Exception as e:
                preview_text.delete(1.0, tk.END)
                preview_text.insert(tk.END, f"Error: {e}")

        window = tk.Tk()
        window.title("ASCII Art Preview")

        frame = tk.Frame(window)
        frame.pack(pady=10)

        tk.Label(frame, text="Width:").grid(row=0, column=0, padx=5)
        width_entry = tk.Entry(frame)
        width_entry.insert(0, str(self.settings_dict["width"]))
        width_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Detail:").grid(row=1, column=0, padx=5)
        detail_entry = tk.Entry(frame)
        detail_entry.insert(0, str(self.settings_dict["detail"]))
        detail_entry.grid(row=1, column=1, padx=5)

        preview_button = tk.Button(frame, text="Update Preview", command=update_preview)
        preview_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        preview_text = tk.Text(window, wrap=tk.WORD, width=80, height=25)
        preview_text.pack(pady=10)

        # Initial preview
        update_preview()

        window.mainloop()