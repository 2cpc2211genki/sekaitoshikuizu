# -*- coding: utf-8 -*-
import tkinter as tk
import requests
import random

# 都市リスト
cities = ["Tokyo", "New York", "London", "Paris", "Sydney", "Moscow", "Rio de Janeiro", "Cairo"]

API_KEY = "あなたのAPIキー"  # OpenWeatherMapのAPIキーに置き換えてください

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return temp, weather
    else:
        return None, None

def start_quiz():
    global answer_city
    answer_city = random.choice(cities)
    temp, weather = get_weather(answer_city)
    if temp is not None:
        hint_label.config(text=f"気温: {temp}°C / 天気: {weather}")
    else:
        hint_label.config(text="データ取得に失敗しました。再試行してください。")

def check_answer():
    user_guess = entry.get()
    if user_guess.lower() == answer_city.lower():
        result_label.config(text="正解！")
    else:
        result_label.config(text=f"不正解… 正解は {answer_city}")

root = tk.Tk()
root.title("世界の都市クイズ")

hint_label = tk.Label(root, text="スタートを押してクイズ開始", font=("Arial", 14))
hint_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

check_button = tk.Button(root, text="回答する", command=check_answer, font=("Arial", 12))
check_button.pack(pady=5)

start_button = tk.Button(root, text="クイズスタート", command=start_quiz, font=("Arial", 12))
start_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
