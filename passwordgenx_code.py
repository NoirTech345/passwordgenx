import tkinter as tk
from tkinter import messagebox, Toplevel, Listbox
import random
import string
import pyperclip
import json
import os



password_history = []
messages = {
    'en': {
        'length_prompt': "Enter the desired length of the password:",
        'incorrect_input': "Incorrect input. Please enter an integer.",
        'generated_password': "Generated password: ",
        'copied_to_clipboard': "The generated password has been copied to the clipboard.",
        'change_language': "Change Language",
        'generate_password': "Generate Password",
        'password_length_note': "Password length should be between 6 and 45 characters.",
        'select_language': "Select Language",
        'minimize_to_tray': "Minimize to Tray",
        'copy_warning': "Do you really want to copy the password?",
        'show_password_history': "Show Password History",
        'password_not_copied': "Password was not copied",
        'clear_all': "Clear all",
        'delete': "Delete",
        'copy': "Copy",

    },
    'ua': {
        'length_prompt': "Введіть бажану довжину пароля:",
        'incorrect_input': "Неправильний ввід. Будь ласка, введіть ціле число.",
        'generated_password': "Згенерований пароль: ",
        'copied_to_clipboard': "Згенерований пароль був скопійований у буфер обміну.",
        'change_language': "Змінити мову",
        'generate_password': "Згенерувати пароль",
        'password_length_note': "Довжина пароля повинна бути від 6 до 45 символів.",
        'select_language': "Виберіть мову",
        'minimize_to_tray': "Згорнути в трей",
        'copy_warning': "Ви дійсно хочете скопіювати пароль?",
        'show_password_history': "Показати історію паролів",
        'password_not_copied': "Пароль не було скопійовано",
        'clear_all': "Очистити все",
        'delete': "Видалити",
        'copy': "Копіювати",

    },
    'ru': {
        'length_prompt': "Введите желаемую длину пароля:",
        'incorrect_input': "Некорректный ввод. Пожалуйста, введите целое число.",
        'generated_password': "Сгенерированный пароль: ",
        'copied_to_clipboard': "Сгенерированный пароль был скопирован в буфер обмена.",
        'change_language': "Сменить язык",
        'generate_password': "Сгенерировать пароль",
        'password_length_note': "Длина пароля должна быть от 6 до 45 символов.",
        'select_language': "Выберите язык",
        'minimize_to_tray': "Свернуть в трей",
        'copy_warning': "Вы действительно хотите скопировать пароль?",
        'show_password_history': "Показать историю паролей",
        'password_not_copied': "Пароль не был скопирован",
        'clear_all': "Очистить все",
        'delete': "Удалить",
        'copy': "Копировать",
    },
    'by': {
        'length_prompt': "Увядзіце жаданую даўжыню пароля:",
        'incorrect_input': "Няправільны ўвод. Калі ласка, увядзіце цэлае лік.",
        'generated_password': "Згенераваны пароль: ",
        'copied_to_clipboard': "Згенераваны пароль быў скопіяваны ў буфер абмену.",
        'change_language': "Змяніць мову",
        'generate_password': "Згенераваць пароль",
        'password_length_note': "Даўжыня пароля павінна быць ад 6 да 45 знакаў.",
        'select_language': "Выберыце мову",
        'minimize_to_tray': "Згарнуць у трэй",
        'copy_warning': "Вы сапраўды хочаце скапіяваць пароль?",
        'show_password_history': "Паказаць гісторыю пароляў",
        'password_not_copied': "Пароль не быў скапіяваны",
        'clear_all': "Ачысціць усё",
        'delete': "Выдаліць",
        'copy': "Капіяваць",

    },
    'kz': {
        'length_prompt': "Пароль ұзындығын көрсетіңіз:",
        'incorrect_input': "Дұрыс емес кіру. Толық сан енгізіңіз.",
        'generated_password': "Жасалған пароль: ",
        'copied_to_clipboard': "Жасалған пароль буферге көшірілді.",
        'change_language': "Тілді өзгерту",
        'generate_password': "Парольді жасау",
        'password_length_note': "Парольдың ұзындығы 6-ден 45 таңбадан аз болмауы керек.",
        'select_language': "Тілді таңдау",
        'minimize_to_tray': "Лақтырғышқа түсіру",
        'copy_warning': "Сіз шынымен парольді көшірмекші ме?",
        'show_password_history': "Құпия сөз тарихын көрсету",
        'password_not_copied': "Құпия сөз көшірілмеді",
        'clear_all': "Барлығын Тазалаңыз",
        'delete': "Жою",
        'copy': "Көшіру",
    },
    'pl': {
        'length_prompt': "Podaj żądaną długość hasła:",
        'incorrect_input': "Niepoprawne dane. Proszę podać liczbę całkowitą.",
        'generated_password': "Wygenerowane hasło: ",
        'copied_to_clipboard': "Wygenerowane hasło zostało skopiowane do schowka.",
        'change_language': "Zmień język",
        'generate_password': "Generuj hasło",
        'password_length_note': "Długość hasła powinna wynosić od 6 do 45 znaków.",
        'select_language': "Wybierz język",
        'minimize_to_tray': "Minimalizuj do zasobnika",
        'copy_warning': "Czy na pewno chcesz skopiować hasło?",
        'show_password_history': "Pokaż historię haseł",
        'password_not_copied': "Hasło nie zostało skopiowane",
        'clear_all': "Wyczyść wszystko",
        'delete': "Usuwać",
        'copy': "Kopiuj",
    }
}


#hi?


def save_password_history():
    os.makedirs(os.path.expanduser('~/Мои Документы/passwordgenxfiles'), exist_ok=True)

    with open(os.path.expanduser('~/Мои Документы/passwordgenxfiles/password_history.json'), 'w') as f:
        json.dump(password_history, f)

def load_password_history():
    try:
        with open(os.path.expanduser('~/Мои Документы/passwordgenxfiles/password_history.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
password_history = load_password_history()

def generate_password(length):
    if length < 6 or length > 45:
        return None

    characters = string.ascii_letters + string.digits + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password





def delete_selected_password(listbox):
    selected_index = listbox.curselection()[0]
    del password_history[selected_index]
    save_password_history()
    listbox.delete(selected_index)




def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length < 6 or length > 45:
            raise ValueError(messages[language]['password_length_note'])
        password = generate_password(length)
        if password:
            password_history.append(password)
            save_password_history()
            update_password_history()
            label_generated.config(text=messages[language]['generated_password'] + password)
            if messagebox.askyesno("Предупреждение", messages[language]['copy_warning']):
                pyperclip.copy(password)
                label_copied.config(text=messages[language]['copied_to_clipboard'])
                root.after(5000, lambda: label_copied.config(text=""))  
            else:
                label_copied.config(text=messages[language]['password_not_copied'])
                root.after(5000, lambda: label_copied.config(text="")) 
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def show_password_history():
    history_window = Toplevel(root)
    history_window.title("Password History")
    history_window.geometry("320x380")  
    history_window.resizable(True, True) 
    history_listbox = Listbox(history_window)
    history_listbox.pack(fill='both', expand=True)
    for password in password_history:
        history_listbox.insert(tk.END, password)
    copy_button = tk.Button(history_window, text=messages[language]['copy'], command=lambda: pyperclip.copy(history_listbox.get(history_listbox.curselection())))
    copy_button.pack(fill='both', expand=True)
    delete_button = tk.Button(history_window, text=messages[language]['delete'], command=lambda: delete_selected_password(history_listbox))
    delete_button.pack(fill='both', expand=True)
    clear_button = tk.Button(history_window, text=messages[language]['clear_all'], command=lambda: clear_password_history(history_listbox))
    clear_button.pack(fill='both', expand=True)

def clear_password_history(listbox):
    password_history.clear()
    save_password_history()  
    listbox.delete(0, tk.END)

def update_password_history():
    if 'history_listbox' in globals():
        history_listbox.delete(0, END)
        for password in password_history:
            history_listbox.insert(END, password)

def change_language():
    global language
    previous_language = language
    language = variable_language.get()
    if previous_language != language:
        messagebox.showinfo(messages[language]['change_language'], f"{messages[language].get('language_changed', 'Language changed')}: {language.upper()}.")
        update_interface(language)


def update_interface(language):
    label_length.config(text=messages[language]['length_prompt'])
    button_generate.config(text=messages[language]['generate_password'])
    label_generated.config(text="")
    label_copied.config(text="")
    password_note_label.config(text=messages[language]['password_length_note'])
    button_language.config(text=messages[language]['change_language'])
    button_history.config(text=messages[language]['show_password_history'])


root = tk.Tk()
root.title("PasswordGenX (created by noirtech)")
root.geometry("400x250")
label_length = tk.Label(root, text=messages['en']['length_prompt'])
label_length.pack(fill='both', expand=True)
entry_length = tk.Entry(root)
entry_length.pack(fill='both', expand=True)
button_generate = tk.Button(root, text=messages['en']['generate_password'], command=generate_and_display_password)
button_generate.pack(fill='both', expand=True)
label_generated = tk.Label(root, text="")
label_generated.pack(fill='both', expand=True)
label_copied = tk.Label(root, text="")
label_copied.pack(fill='both', expand=True)
variable_language = tk.StringVar(root)
variable_language.set('en')
option_menu = tk.OptionMenu(root, variable_language, 'en', 'ua', 'ru', 'by', 'kz', 'pl')
option_menu.pack(fill='both', expand=True)
button_language = tk.Button(root, text=messages['en']['change_language'], command=change_language, font=("Arial", 10))
button_language.pack(fill='both', expand=True)
button_history = tk.Button(root, text=messages['ru']['show_password_history'], command=show_password_history)
button_history.pack(fill='both', expand=True)
password_note_label = tk.Label(root, text=messages['en']['password_length_note'], fg="red")
password_note_label.pack(fill='both', expand=True)
language = 'en'
update_interface(language)

root.mainloop()


















