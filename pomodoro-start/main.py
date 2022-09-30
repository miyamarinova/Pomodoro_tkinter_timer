from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label_timer.config(text='Timer')
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED, highlightthickness=0)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=RED)
        count_down(work_sec)


def count_down(count):

    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_minute < 10:
        count_minute = f'0{count_minute}'

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg="#F3E9DD")


canvas = Canvas(width=200, height=224, bg="#F3E9DD", highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(100, 113, image=img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label_timer = Label(text="Timer", fg="#3E7C17", bg="#F3E9DD", font=(FONT_NAME, 50))
label_timer.grid(column=1, row=0)

check_marks = Label(fg="#3E7C17", bg="#F3E9DD")
check_marks.grid(column=1, row=3)

start_button = Button(text='Start', fg="#3E7C17", bg="#F3E9DD", highlightthickness=0, font=(FONT_NAME, 20), command=start_timer)
start_button.grid(column=0, row=2)

start_button = Button(text='Reset', fg="#3E7C17", bg="#F3E9DD", highlightthickness=0, font=(FONT_NAME, 20), command=reset_timer)
start_button.grid(column=2, row=2)




window.mainloop()