import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

def set_dark_theme():
    # Основные цвета
    dark_bg = "#2d2d2d"
    dark_fg = "#ffffff"
    darker_bg = "#1e1e1e"
    accent_color = "#3f3f3f"
    hover_color = "#4f4f4f"

    # Настройка стилей для ttk виджетов
    style = ttk.Style()
    style.theme_use("alt")

    # Общие настройки
    style.configure(".", background=dark_bg, foreground=dark_fg)
    root.configure(bg=dark_bg)

    # Настройка Treeview
    style.configure("Treeview",
                    background=darker_bg,
                    fieldbackground=darker_bg,
                    foreground=dark_fg,
                    rowheight=30,
                    bordercolor=dark_bg,
                    lightcolor=dark_bg,
                    darkcolor=dark_bg)
    style.map("Treeview",
              background=[('selected', accent_color)],
              foreground=[('selected', dark_fg)])

    # Настройка кнопок
    style.configure("TButton",
                    background=accent_color,
                    foreground=dark_fg,
                    borderwidth=1,
                    focusthickness=3,
                    focuscolor=accent_color)
    style.map("TButton",
              background=[('active', hover_color)],
              foreground=[('active', dark_fg)])

    # Настройка фреймов
    style.configure("TFrame", background=dark_bg)

    # Настройка меток
    style.configure("TLabel",
                    background=dark_bg,
                    foreground=dark_fg,
                    font=('Arial', 12))


# Создаем окно
root = tk.Tk()
root.title("Календарь")
root.geometry("800x600")
set_dark_theme()  # Применяем темную тему

# Список дней недели
week = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")

# Получаем текущие данные
current_date = datetime.now()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

# Создаем Treeview с настройками
calendar_days = ttk.Treeview(root, columns=week, show='headings', selectmode="none")

# Настраиваем заголовки
for day in week:
    calendar_days.heading(day, text=day)
    calendar_days.column(day, width=100, anchor='center')

calendar_days.pack(expand=True, fill="both", padx=10, pady=10)

# Фрейм для элементов управления
control_frame = ttk.Frame(root)
control_frame.pack(pady=10)

# Метка месяца и года
month_label = ttk.Label(control_frame, font=('Arial', 12, 'bold'))


# Функция отображения календаря
def show_calendar(year, month):
    for row in calendar_days.get_children():
        calendar_days.delete(row)

    month_calendar = calendar.monthcalendar(year, month)

    for week_days in month_calendar:
        formatted_days = [str(day) if day != 0 else "" for day in week_days]
        calendar_days.insert("", "end", values=formatted_days)

    month_label.config(text=f"{month}/{year}")


show_calendar(current_year, current_month)


# Функции навигации
def prev_month():
    global current_year, current_month
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    show_calendar(current_year, current_month)


def next_month():
    global current_year, current_month
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    show_calendar(current_year, current_month)


# Кнопки управления
prev_button = ttk.Button(control_frame, text="◀", command=prev_month)
next_button = ttk.Button(control_frame, text="▶", command=next_month)

# Размещение элементов
prev_button.pack(side="left", padx=10)
month_label.pack(side="left", padx=10)
next_button.pack(side="left", padx=10)

# Запуск приложения
root.mainloop()