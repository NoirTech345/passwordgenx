import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
from PIL import Image, ImageTk
import pystray
import locale
import ctypes
windll = ctypes.windll.kernel32

messages = {
    'en_US': {
        'length_prompt': "Enter the desired length of the password:",
        'incorrect_input': "Incorrect input. Please enter an integer.",
        'generated_password': "Generated password: ",
        'copied_to_clipboard': "The generated password has been copied to the clipboard.",
        'change_language': "Change Language",
        'generate_password': "Generate Password",
        'password_length_note': "Password length should be between 6 and 45 characters.",
        'select_language': "Select Language",
        'minimize_to_tray': "Minimize to Tray"
    },
     'en_GB': {
        'length_prompt': "Enter the desired length of the password:",
        'incorrect_input': "Incorrect input. Please enter an integer.",
        'generated_password': "Generated password: ",
        'copied_to_clipboard': "The generated password has been copied to the clipboard.",
        'change_language': "Change Language",
        'generate_password': "Generate Password",
        'password_length_note': "Password length should be between 6 and 45 characters.",
        'select_language': "Select Language",
        'minimize_to_tray': "Minimize to Tray"
    },
    'ua_UA': {
        'length_prompt': "Введіть бажану довжину пароля:",
        'incorrect_input': "Неправильний ввід. Будь ласка, введіть ціле число.",
        'generated_password': "Згенерований пароль: ",
        'copied_to_clipboard': "Згенерований пароль був скопійований у буфер обміну.",
        'change_language': "Змінити мову",
        'generate_password': "Згенерувати пароль",
        'password_length_note': "Довжина пароля повинна бути від 6 до 45 символів.",
        'select_language': "Виберіть мову",
        'minimize_to_tray': "Згорнути в трей"
    },
    'ru_RU': {
        'length_prompt': "Введите желаемую длину пароля:",
        'incorrect_input': "Некорректный ввод. Пожалуйста, введите целое число.",
        'generated_password': "Сгенерированный пароль: ",
        'copied_to_clipboard': "Сгенерированный пароль был скопирован в буфер обмена.",
        'change_language': "Сменить язык",
        'generate_password': "Сгенерировать пароль",
        'password_length_note': "Длина пароля должна быть от 6 до 45 символов.",
        'select_language': "Выберите язык",
        'minimize_to_tray': "Свернуть в трей"
    },
    'be_BY': {
        'length_prompt': "Увядзіце жаданую даўжыню пароля:",
        'incorrect_input': "Няправільны ўвод. Калі ласка, увядзіце цэлае лік.",
        'generated_password': "Згенераваны пароль: ",
        'copied_to_clipboard': "Згенераваны пароль быў скопіяваны ў буфер абмену.",
        'change_language': "Змяніць мову",
        'generate_password': "Згенераваць пароль",
        'password_length_note': "Даўжыня пароля павінна быць ад 6 да 45 знакаў.",
        'select_language': "Выберыце мову",
        'minimize_to_tray': "Згарнуць у трэй"
    },
    'kk_KZ': {
        'length_prompt': "Пароль ұзындығын көрсетіңіз:",
        'incorrect_input': "Дұрыс емес кіру. Толық сан енгізіңіз.",
        'generated_password': "Жасалған пароль: ",
        'copied_to_clipboard': "Жасалған пароль буферге көшірілді.",
        'change_language': "Тілді өзгерту",
        'generate_password': "Парольді жасау",
        'password_length_note': "Парольдың ұзындығы 6-ден 45 таңбадан аз болмауы керек.",
        'select_language': "Тілді таңдау",
        'minimize_to_tray': "Лақтырғышқа түсіру"
    },
    'pl_PL': {
        'length_prompt': "Podaj żądaną długość hasła:",
        'incorrect_input': "Niepoprawne dane. Proszę podać liczbę całkowitą.",
        'generated_password': "Wygenerowane hasło: ",
        'copied_to_clipboard': "Wygenerowane hasło zostało skopiowane do schowka.",
        'change_language': "Zmień język",
        'generate_password': "Generuj hasło",
        'password_length_note': "Długość hasła powinna wynosić od 6 do 45 znaków.",
        'select_language': "Wybierz język",
        'minimize_to_tray': "Minimalizuj do zasobnika"
    }
}

def generate_password(length):
    if length < 6 or length > 45:
        return None

    characters = string.ascii_letters + string.digits + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length < 6 or length > 45:
            raise ValueError(messages[language]['password_length_note'])
        password = generate_password(length)
        if password:
            label_generated.config(text=messages[language]['generated_password'] + password)
            pyperclip.copy(password)
            label_copied.config(text=messages[language]['copied_to_clipboard'])
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def change_language():
    global language
    previous_language = language
    language = variable_language.get()
    if previous_language != language:
        messagebox.showinfo(messages[language]['change_language'], f"{messages[language].get('language_changed', 'Language changed')}: {language.upper()}.")
        update_interface(language)

def minimize_to_tray():
    root.withdraw()
    icon = pystray.Icon("")
    icon.icon = Image.open("icon.png")
    icon.visible = True
    icon.run()

def update_interface(language):
    label_length.config(text=messages[language]['length_prompt'])
    button_generate.config(text=messages[language]['generate_password'])
    label_generated.config(text="")
    label_copied.config(text="")
    password_note_label.config(text=messages[language]['password_length_note'])
    button_language.config(text=messages[language]['change_language'])
    button_minimize.config(text=messages[language]['minimize_to_tray'])

root = tk.Tk()
root.title("PasswordGenX (created by noirtech)")
root.geometry("400x250")
root.resizable(0, 0)

label_length = tk.Label(root, text=messages['en_US']['length_prompt'])
label_length.pack(fill='both', expand=True)

entry_length = tk.Entry(root)
entry_length.pack(fill='both', expand=True)

button_generate = tk.Button(root, text=messages['en_US']['generate_password'], command=generate_and_display_password)
button_generate.pack(fill='both', expand=True)

label_generated = tk.Label(root, text="")
label_generated.pack(fill='both', expand=True)

label_copied = tk.Label(root, text="")
label_copied.pack(fill='both', expand=True)

variable_language = tk.StringVar(root)
variable_language.set(locale.windows_locale[windll.GetUserDefaultUILanguage()])
option_menu = tk.OptionMenu(root, variable_language, 'en_US', 'ua_UA', 'ru_RU', 'be_BY', 'kk_KZ', 'pl_PL')
option_menu.pack(fill='both', expand=True)

button_language = tk.Button(root, text=messages['en_US']['change_language'], command=change_language, font=("Arial", 10))
button_language.pack(fill='both', expand=True)

button_minimize = tk.Button(root, text=messages['en_US']['minimize_to_tray'], command=minimize_to_tray, font=("Arial", 10))
button_minimize.pack(fill='both', expand=True)

password_note_label = tk.Label(root, text=messages['en_US']['password_length_note'], fg="red")
password_note_label.pack(fill='both', expand=True)

language = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]
update_interface(language)

root.mainloop()