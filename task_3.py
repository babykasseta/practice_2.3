import tkinter as tk
import requests



root = tk.Tk()
root.title("Курсы валют")
root.geometry("700x500")
text_output = tk.Text(root, width=30, height=15)
text_output.pack(pady=10)


def show_all(data):
    text_output.delete(1.0, tk.END)
    for code, val in data["Valute"].items():
        text_output.insert(tk.END, f"{code} - {val['Value']}\n")

entry = tk.Entry(root)
entry.pack(pady=5)

def show_one(data):
    code = entry.get().upper()
    text_output.delete(1.0, tk.END)

    if code in data["Valute"]:
        text_output.insert(tk.END, f"{code} - {data['Valute'][code]['Value']}\n")
    else:
        text_output.insert(tk.END, "Валюта не найдена")

def get_data():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url)
        return response.json()
    except:
        print("Ошибка при получении данных")
        return {"Valute": {}}

data = get_data()
groups= {}
btn_all = tk.Button(root, text = "Все валюты", command=lambda: show_all(data))
btn_all.pack()

btn_one = tk.Button(root, text = "Найти валюту", command=lambda: show_one(data))
btn_one.pack()

def create_group():
    name = entry.get()

    if name in groups:
        text_output.insert(tk.END, "Такая группа уже есть\n")
    else:
        groups[name]=[]
        text_output.insert(tk.END, f"{name}: пусто\n")

def show_group():
    text_output.delete(1.0, tk.END)

    if not groups:
        text_output.insert(tk.END, "Групп нет\n")
        return

    for name, currencies in groups.items():
        if currencies:
            text_output.insert(tk.END, f"{name}:{', '.join(currencies)}\n")
        else:
            text_output.insert(tk.END, f"{name}: пусто\n")


#добавляем валюту в группу
def add_group():
    text_output.delete(1.0, tk.END)
    parts = entry.get().split()  # разделяем по пробелу

    if len(parts) != 2:
        text_output.insert(tk.END, "Формат: <название_группы> <код_валюты>\n")
        return

    name, cur = parts
    cur = cur.upper()  # делаем код валюты в верхнем регистре

    if name not in groups:
        text_output.insert(tk.END, "Группы не найдено\n")
        return

    if cur not in data["Valute"]:
        text_output.insert(tk.END, "Валюта не найдена\n")
        return

    if cur in groups[name]:
        text_output.insert(tk.END, "Валюта уже добавлена\n")
    else:
        groups[name].append(cur)
        text_output.insert(tk.END, f"Валюта {cur} успешно добавлена в группу: {name}\n")

#кнопки добавление групп
btn_create = tk.Button(root, text = "Создать группу", command=create_group)
btn_create.pack()

btn_show = tk.Button(root, text = "Показать группы", command=show_group)
btn_show.pack()

btn_add = tk.Button(root, text = "Добавить в группу", command=add_group)
btn_add.pack()

root.mainloop()

