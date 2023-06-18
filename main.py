from tkinter import *  # We are using lots of classes from tkinter module that's why we are importing all the classes using *(asterisk).
import time     # Importing time module
import math
# ---------------------------------------- NOTES ------------------------------------


# Pomodoro means Tomato in Italian.
# To select color combination, visit colorhunt.co   -> Used by many professional developers.
# fg means Foreground color. (Mainly, used in labels)
# bg means background color.
# We'll use grid instead of pack.


# -------------------------------- CONSTANTS ---------------------------------------
PINK = "e2979c"
RED = "e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 25, "bold")
WORK_MIN = 1
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer_on = None

# -------------------------------- TIMER RESET ---------------------------------------
def reset_timer():
    checkmark_label.config(text="")
    title_label.config(text="Timer")
    window.after_cancel(timer_on);  # To cancel the window.after() timer you should pass the object variable of window.after() and then pass here as a parameter.
    canvas.itemconfig(timer, text = "00:00")
    global reps
    reps = 0
    
# -------------------------------- TIMER MECHANISM ---------------------------------------
def start_timer():
    global reps 
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 2 != 0:        # if reps == 1 or reps == 3 or reps == 5 or reps == 7
        countdown(work_sec)
        title_label.config(text = "WORK", fg = "green");
    elif reps % 2 == 0:      # if reps == 2 or reps == 4 or reps == 6
        countdown(short_break_sec)
        title_label.config(text = "SHORT BREAK", fg = "pink");
    elif reps % 8 == 0:     # if reps == 8
        countdown(long_break_sec);
        title_label.config(text = "LONG BREAK", fg = "red");

# -------------------------------- COUNTDOWN MECHANISM ---------------------------------------
def countdown(count):
    # if(count < 10):       # for displaying always in two significant figures.
    #     count = f"0{count}";      # f string is being used here.
    
    time = str(math.floor(count / 60)).zfill(2)+":"+str(count % 60).zfill(2)       # zfill() method us used to add leading zeroes to match with the length of the number. The parameter passed is the length of the number to be displayed on the screen.
    canvas.itemconfig(timer, text = time)       # itemconfig() is used to update the configuration of a canvas.
    if count > 0:
        global timer_on    # to select the global timer variable or else if we don't mention the global keyword then local variable of name timer will be created.
        timer_on = window.after(1000, countdown, count-1)      # Here, 1000ms is the delay time which is equal to 1 second, countdown is the function passed and (count-1) is the actual parameter of the countdown() function .
        # When we want to cancel/ reset the timer then this timer variable is passed as a parameter inside [window.after_cancel(timer)]

    else:
        start_timer()       # if count == 0, then start_timer() function will get triggered.
        work_session = math.floor(reps/2)   # Counting the number of reps (1 reps = 1 work session + 1 break).
        tick = ""       # Empty variable to store the check marks.
        for _ in range(work_session):   # Loop to count the total number of checkmarks.
            tick += CHECKMARK;  # appending checkmark to the variable tick.
        checkmark_label["text"] = tick;     # updating the label with the tick variable value.

# -------------------------------- UI SETUP ---------------------------------------
window = Tk()   # Creating object.
window.title("Pomodoro App")        # Window title.
# window.minsize(width = 500, height = 500)

# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# window.after(1000, say_something, 10, 20, 30)      # after command execute a command after a time delay. Amount in time is passed in milliseconds(1000ms = 1 second)
# The passed arguments in the above function are: (time_in_milliseconds, function_name_that_is_to_be_executed, *args)
# *args allows us to pass unlimited number of positional arguments.
# In the above args*, the actual parameter, which of the argument of the function is being passed . We can have infinite amount of positional arguments.



title_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = FONT)    # here fg means foreground color.
title_label.grid(column = 1, row = 0)

window.config(padx = 140, pady = 100, bg = YELLOW)   # Adding Padding and Background color to the window.
# window["bg"] = YELLOW       # OR window.configure(bg = YELLOW)  [Either of the two syntax can be used for background colors.]

# Setting up the Image on the Tkinter window using Canvas()
canvas = Canvas(width = 200, height = 223, bg = YELLOW, highlightthickness = 0)      # Canvas object with size of the image is created along with the background color and highlightthickness setting up to 0 and then stored inside canvas variable.

tomato_img = PhotoImage(file = "tomato.png")     # This helps to read from a file and get hold to a particular image file location.

canvas.create_image(100, 112, image = tomato_img)       # Creating the image by passing the x and y coordinates of the image where it is to be placed and the variable that read the image file from PhotoImage() class.
# In the above syntax, 100 and 112 are the cand y coordinates of the place where the image to be placed. It is half of the width and height of the canvas set earlier.

timer = canvas.create_text(100, 130, text = "00:00", fill = "white", font = FONT)    # Adding text on the middle of the Tomato / Pomodoro with all its specification specified as a parameter.

canvas.grid(row = 1, column = 1)       # putting the canvas on the main window.

start_button = Button(text = "Start", command = start_timer, highlightthickness = 0)   # Start Button.
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", command = reset_timer, highlightthickness = 0)   # Reset Button.
reset_button.grid(row = 2, column = 2)

checkmark_label = Label(fg = GREEN, bg = YELLOW)      # Checkmark label.
checkmark_label.grid(row = 3, column = 1)

window.mainloop()   # mainloop i.e., the whole code is inside the infinite while loop.





# ---------------------------------------- Dynamic Typing in Python -----------------------------------------------

# a = "Hello"     # String is stored in variable a of type <str>
# print(type(a))
# if we again initialize this variable to any integer value than the variable type will get converted to <int>
# This is Dynamic Typing in Python.
# a = 5;
# print(type(a))
