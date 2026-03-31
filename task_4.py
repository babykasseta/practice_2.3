import tkinter as tk
from tkinter import messagebox
import requests

# функция для получения профиля
def get_user():
    username = entry_username.get()  # берём username из поля ввода
    if not username:
        messagebox.showwarning("Ошибка", "Введите username")
        return

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Ошибка", "Пользователь не найден")
        return

    data = response.json()
    # обновляем текстовое поле с результатом
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Имя: {data['login']}\n")
    result_text.insert(tk.END, f"Ссылка: {data['html_url']}\n")
    result_text.insert(tk.END, f"Репозитории: {data['public_repos']}\n")
    result_text.insert(tk.END, f"Подписчики: {data['followers']}\n")
    result_text.insert(tk.END, f"Подписки: {data['following']}\n")

# создаём главное окно
root = tk.Tk()
root.title("GitHub Viewer")
root.geometry("400x300")

# надпись и поле ввода для username
label_username = tk.Label(root, text="Введите username GitHub:")
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

# кнопка для запуска функции
button_get = tk.Button(root, text="Получить профиль", command=get_user)
button_get.pack(pady=5)

# текстовое поле для вывода результата
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

# запуск главного цикла приложения
root.mainloop()