from tkinter import *
from tkinter import ttk
import subprocess
from sortfunctions import *
from tkinter import filedialog

# создаем виджеты и меняем их в функциях
root = Tk()
root.title("Сортировщик")
root.geometry("680x360")
main_lbl = ttk.Label(root)
main_entry = ttk.Entry(root)
main_button = ttk.Button(root)
info_button = ttk.Button(root)
path_button = ttk.Button(root)
main_combobox = ttk.Combobox(root)

# указываем глобальные переменные тк я с функции в функцию несу
file_path = ""
selected_method = ""
lines = []
sorted_lines = ""

# первое окно указываем путь к файлу, формат: textdata/file.txt
def show_file_window():
    main_lbl.config(text="Введите путь к файлу:", font=("Arial Bold", 24))
    main_lbl.place(relx=0.5,
                   rely=0.3,
                   anchor="center")

    main_entry.place(relx=0.5,
                     rely=0.6,
                     anchor="center")

    main_button.config(command=lambda: check_and_continue(),
                       text="Продолжить")
    main_button.place(relx=0.5,
                      rely=0.7,
                      anchor="center")

    path_button.config(command=lambda: open_file_dialog(),
                       text="...")
    path_button.place(relx=0.64,
                     rely=0.6,
                      width=20,
                     anchor="center",)

    root.mainloop()

# сохраняем имя и проверяем есть ли файл
def check_and_continue():
    global file_path
    file_path = main_entry.get()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            _ = f.read()  # можешь не сохранять, если не нужно
        show_method_window()
    except FileNotFoundError:
        main_lbl.config(text="Такого файла нет!")
    except UnicodeDecodeError:
        main_lbl.config(text="Неверная кодировка файла.")
    except PermissionError:
        main_lbl.config(text="Нет доступа к файлу.")


# можно выбрать
def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename(title="Выберите файл",
                                           filetypes=[("Text files", ".txt")])
    if file_path:
        show_method_window()
    else:
        main_lbl.config(text="Файл не выбран!")

# второе окно - выбор сортировки и сортировка файла
def show_method_window():
    main_entry.destroy()
    path_button.destroy()

    main_lbl.config(text="Выберите метод сортировки")
    main_lbl.place(relx=0.5,
                   rely=0.3,
                   anchor="center")

    main_combobox.config(values=["Bubble", "Quick", "Shaker", "Comb", "Selection"], state="readonly")
    main_combobox.place(relx=0.47,
                        rely = 0.5,
                        width=200,
                        anchor="center")

    info_button.config(text="?", command=lambda: show_info())
    info_button.place(relx=0.64,
                      rely=0.5,
                      width=20,
                      anchor="center")

    main_button.config(command=lambda: [save_method_and_continue(), create_sorted_file()],
                       text="Продолжить")

# инфа о методах
def show_info():
    subprocess.Popen(["notepad", "textdata/info.txt"])

# сохраняем метод также как имя
def save_method_and_continue():
    global selected_method
    selected_method = main_combobox.get()
    if selected_method:
        file_method_window()
    else:
        main_lbl.config(text="Вы не выбрали метод!")

# создаем новый файл чтобы не срать исходник
def create_sorted_file():
    global lines, sorted_lines
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # убираем пробелы и переводим строки в числа
        lines = [int(x.strip()) for x in content.replace("\n", ",").split(",") if x.strip()]

    sorted_func()

    with open("textdata/output.txt", "w", encoding="utf-8") as f:
        f.write(", ".join(map(str, sorted_lines)))  # записываем обратно в строку

# вывод
def file_method_window():
    info_button.destroy()

    main_lbl.config(text=f'Текст отсортирован {selected_method} методом')

    main_button.config(command=lambda: open_file(),
                       text = "Открыть файл")
    main_button.place_configure(width=120, height=60)

    main_combobox.destroy()

def open_file():
    subprocess.Popen(["notepad", "textdata/output.txt"])

def sorted_func():
    global sorted_lines
    if selected_method == "Bubble":
        sorted_lines = bubble_sort(lines[:])
    if selected_method == "Quick":
        sorted_lines = quick_sort(lines[:])
    if selected_method == "Shaker":
        sorted_lines = shaker_sort(lines[:])
    if selected_method == "Comb":
        sorted_lines = combination_sort(lines[:])
    if selected_method == "Selection":
        sorted_lines = selection_sort(lines[:])

if __name__ == "__main__":
    show_file_window()