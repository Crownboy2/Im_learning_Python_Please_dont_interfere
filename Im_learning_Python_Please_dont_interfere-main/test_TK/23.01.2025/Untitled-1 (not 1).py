from tkinter import *

# Создание главного окна
root = Tk()

# Установка прозрачности и цвета фона для окна
root.attributes("-transparentcolor", "white")
root.configure(bg="#ADD8E6")  # какой-то голубой цвет

# Установка размера и позиции главного окна
root.geometry("400x400")

# Запуск основного цикла Tkinter для управления интерфейсом пользователя.
root.mainloop()