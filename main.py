from tkinter import *

import time

words_list = []


def get_text():
    t_timer = 5 * 60
    count_down(t_timer)
    word_textarea.config(state="normal")
    # words = word_textarea.get("1.0", "end")
    # if words in words_list:
    #     word_textarea.delete("1.0", "end")
    # else:
    #     words_list.append(words)
    # window.after(1000, get_text)
    # window.after(180000, save_text)


def save_text():
    words = word_textarea.get("1.0", "end")
    with open("words.text", "a") as file:
        file.write(words)


def count_down(count):
    global timer
    # this will get the count time in minutes
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_label.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        words = word_textarea.get("1.0", "end")
        if words in words_list:
            word_textarea.delete("1.0", "end")
        else:
            words_list.append(words)
        timer = window.after(5000, count_down, count - 5)
    else:
        word_textarea.config(state="disabled")
        words = word_textarea.get("1.0", "end")
        print(words)
        save_text()


window = Tk()

window.title("Disappearing Text Writing App")
window.minsize(width=800, height=700)


title = Label(text="Keep Typing for 5 Mins. Words would disappear if you stop typing ", font=("ariel", 50, "bold"))
title.pack()


word_textarea = Text(width=70, height=10, font=("ariel", 15, "bold"), state="disabled")
word_textarea.pack()

start_button = Button(text="Start", command=get_text or save_text)
start_button.pack()

timer_label = Label(text="Timer", font=("ariel", 15, "bold"))
timer_label.pack()
window.mainloop()


