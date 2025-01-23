import tkinter as tk

# Создание основного окна
root = tk.Tk()

# Установка размера и положения главного окна
root.geometry("800x600")  # ширина x высота в пикселях

# Добавление заголовка к главному окну
root.title("CoreHub")

# Создание кнопки "Открыть другое окно"
def open_new_window():
    new_root = tk.Tk()
    new_root.geometry("400x300")  # ширина x высота в пикселях для нового окна
    label = tk.Label(new_root, text="Это новое окно!")
    label.pack(padx=10, pady=10)  # добавление расстояния между элементами

button = tk.Button(root, text="Открыть другое окно", command=open_new_window)
button.pack(padx=10, pady=10)  # добавление расстояния между элементами

# Запуск основного цикла Tkinter
root.mainloop()