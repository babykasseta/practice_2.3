import tkinter as tk
import requests

root = tk.Tk()
root.title("Проверка сайтов")
root.geometry("500x400")

def get_status(code):
    if 200 <= code < 300:
        return "доступен"
    elif code == 403:
        return "вход запрещен"
    elif code == 404:
        return "не найден"
    elif code >= 500:
        return "ошибка сервера"
    else:
        return f"статус {code}"

def check_url(url):
    global text_output

    try:
        response = requests.get(url, timeout=10)
        code = response.status_code
        status = get_status(code)
        text_output.insert(tk.END, f"{url} - {status} - {code}\n")
    except:
        text_output.insert(tk.END, f"{url} – не доступен – ошибка соединения\n")

def on_click():
    text_output.delete(1.0, tk.END)
    urls= [
        "https://github.com/",
        "https://www.binance.com/en",
        "https://tomtit.tomsk.ru/",
        "https://jsonplaceholder.typicode.com/",
        "https://moodle.tomtit-tomsk.ru/",
        "https://metanit.com/python/tkinter/2.1.php"
    ]
    for url in urls:
        check_url(url)
button = tk.Button(root, text = "Проверить сайты", command=on_click)
button.pack(pady=20)

text_output = tk.Text(root, height=50, width=50)
text_output.pack()

root.mainloop()