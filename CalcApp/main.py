import tkinter as tk
from tkinter import font


class IPhoneCalculator:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("iPhone Calculator")
        self.parent.configure(bg='#000000')
        self.parent.resizable(False, False)
        self.current_input = "0"
        self.previous_value = None
        self.operation = None
        self.reset_input = False
        self.display_var = tk.StringVar()
        self.display = None

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.parent, height=200, bg='#000000')
        display_frame.pack(expand=True, fill='both')
        self.display_var.set(self.current_input)
        display_font = font.Font(family="Helvetica", size=48, weight="normal")
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=display_font,
            anchor='e',
            bg='#000000',
            fg='#FFFFFF',
            padx=20
        )
        self.display.pack(expand=True, fill='both', side='bottom')

    def create_buttons(self):
        button_font = font.Font(family="Helvetica", size=24, weight="normal")
        common_button_config = {
            'font': button_font,
            'bd': 0,
            'highlightthickness': 0,
            'height': 2
        }

        grid_config = {
            'sticky': 'nsew',
            'padx': 2,
            'pady': 2
        }

        buttons = [
            ('C', 1, 0, '#A5A5A5', '#000000', 1),
            ('±', 1, 1, '#A5A5A5', '#000000', 1),
            ('%', 1, 2, '#A5A5A5', '#000000', 1),
            ('÷', 1, 3, '#FF9F0A', '#FFFFFF', 1),

            ('7', 2, 0, '#333333', '#FFFFFF', 1),
            ('8', 2, 1, '#333333', '#FFFFFF', 1),
            ('9', 2, 2, '#333333', '#FFFFFF', 1),
            ('×', 2, 3, '#FF9F0A', '#FFFFFF', 1),

            ('4', 3, 0, '#333333', '#FFFFFF', 1),
            ('5', 3, 1, '#333333', '#FFFFFF', 1),
            ('6', 3, 2, '#333333', '#FFFFFF', 1),
            ('-', 3, 3, '#FF9F0A', '#FFFFFF', 1),

            ('1', 4, 0, '#333333', '#FFFFFF', 1),
            ('2', 4, 1, '#333333', '#FFFFFF', 1),
            ('3', 4, 2, '#333333', '#FFFFFF', 1),
            ('+', 4, 3, '#FF9F0A', '#FFFFFF', 1),

            ('0', 5, 0, '#333333', '#FFFFFF', 2),
            ('.', 5, 2, '#333333', '#FFFFFF', 1),
            ('=', 5, 3, '#FF9F0A', '#FFFFFF', 1),
        ]

        button_frame = tk.Frame(self.parent, bg='#000000')
        button_frame.pack(expand=True, fill='both')

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

        for text, row, col, bg_color, fg_color, span in buttons:
            btn_config = common_button_config.copy()
            btn_config.update({
                'bg': bg_color,
                'fg': fg_color,
                'command': lambda t=text: self.on_button_click(t),
                'text': text,
                'master': button_frame
            })

            if text == '0':
                btn_config['width'] = 8
            else:
                btn_config['width'] = 4

            btn = tk.Button(**btn_config)
            btn.grid(row=row, column=col, columnspan=span, **grid_config)

    def on_button_click(self, button_text):
        if button_text in '0123456789':
            self.input_digit(button_text)
        elif button_text == '.':
            self.input_decimal()
        elif button_text == 'C':
            self.clear()
        elif button_text == '±':
            self.toggle_sign()
        elif button_text == '%':
            self.percentage()
        elif button_text in ['+', '-', '×', '÷']:
            self.set_operation(button_text)
        elif button_text == '=':
            self.calculate()

    def input_digit(self, digit):
        if self.reset_input or self.current_input == "0":
            self.current_input = digit
            self.reset_input = False
        else:
            self.current_input += digit

        self.update_display()

    def input_decimal(self):
        if self.reset_input:
            self.current_input = "0."
            self.reset_input = False
        elif "." not in self.current_input:
            self.current_input += "."

        self.update_display()

    def clear(self):
        self.current_input = "0"
        self.previous_value = None
        self.operation = None
        self.reset_input = False
        self.update_display()

    def toggle_sign(self):
        if self.current_input != "0":
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        self.update_display()

    def percentage(self):
        try:
            value = float(self.current_input) / 100
            self.current_input = self.format_result(value)
            self.update_display()
        except (ValueError, TypeError):
            self.current_input = "Error"
            self.update_display()

    def set_operation(self, op):
        if self.operation and not self.reset_input:
            self.calculate()

        try:
            self.previous_value = float(self.current_input)
            self.operation = op
            self.reset_input = True
        except (ValueError, TypeError):
            self.current_input = "Error"
            self.update_display()

    def calculate(self):
        if self.operation is None or self.previous_value is None:
            return

        try:
            current_value = float(self.current_input)
            result = None

            if self.operation == '+':
                result = self.previous_value + current_value
            elif self.operation == '-':
                result = self.previous_value - current_value
            elif self.operation == '×':
                result = self.previous_value * current_value
            elif self.operation == '÷':
                if current_value == 0:
                    self.current_input = "Error"
                    self.update_display()
                    return
                result = self.previous_value / current_value

            if result is not None:
                self.current_input = self.format_result(result)
                self.update_display()

        except (ValueError, TypeError, ZeroDivisionError):
            self.current_input = "Error"
            self.update_display()
        finally:
            self.operation = None
            self.previous_value = None
            self.reset_input = True

    def format_result(self, value):
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    def update_display(self):
        if len(self.current_input) > 12:
            if '.' in self.current_input:
                self.current_input = self.current_input[:12]
            else:
                self.current_input = self.current_input[:12] + "..."

        self.display_var.set(self.current_input)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("320x480")
    calc = IPhoneCalculator(root)
    root.mainloop()