

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
LAPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
        window.after_cancel(timer)
        canvas.itemconfig(timer_text,text = "00:00")
        title.config(text="Timer")
        check_marks.config(text="")
        global LAPS
        LAPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global LAPS
    LAPS+=1
    work_seconds = WORK_MIN*60
    short_break_seconds = SHORT_BREAK_MIN*60
    long_break_seconds = LONG_BREAK_MIN*60
        
    if LAPS%8 ==0:
        countdown(long_break_seconds) #8th laps only ie: 20 mins break
        title.config (text="BREAK", fg= RED)
    
    elif LAPS%2 == 0:
        countdown(short_break_seconds) #2,4,6th laps respectively ie:5 mins breaks
        title.config(text="BREAK" , fg= PINK)
    else:
        countdown(work_seconds) #1,3,5,7th laps respectively.ie: 25 mins work
        title.config(text="WORK" , fg= GREEN)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minute = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}" # to make sure that counter starts as 25:00 and not 25:0


    canvas.itemconfig(timer_text,text = f"{count_minute}:{count_seconds}")
    if count>0:
      global timer
      timer =  window.after(1000, countdown, count-1) #after 1000 ms ie 1 sec, decrement the count by 1.
    else:
        start_timer() #so that we dont have to keep on pressing start, after timer reaches 0 it'll go to start_timer to figure out which lap to run.
        mark = ""
        work_sessions =  math.floor(LAPS/2)
        for i in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import math

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME,50,), bg=YELLOW)
title.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="./day 28 python - pomodoro/pomodoro-start/tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start", bg=RED, highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", bg=RED, highlightthickness=0, command=reset)
reset_button.grid(column=2,row=2)

check_marks = Label(bg=YELLOW,fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()