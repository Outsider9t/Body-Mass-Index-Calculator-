from tkinter import *
import math


def cal():
    while True:
        try:
            global entry_weight
            global entry_height

            getting_weight = entry_weight.get()
            getting_height = entry_height.get()

            float_weight = float(getting_weight)
            float_height = float(getting_height)

            # Calculating BMI
            squaring_height = float_height ** 2
            calculating_bmi = float_weight / squaring_height

            # print("{:.1f}".format(calculating_bmi))

            # Calculating stones
            cal_stones = float_weight / 6.35
            rounding_stones = round(cal_stones)

            if calculating_bmi < 18.5:
                stats = ("Underweight!\n"
                         "Eat more!")

            elif 18.5 <= calculating_bmi <= 24.9:
                stats = ("Healthy\n"
                         "Hurray!")

            elif 25 <= calculating_bmi <= 29.9:
                stats = ("Overweight!\n"
                         "Please reduce how you eat!")

            elif calculating_bmi >= 30:
                stats = ("Obese!\n"
                         "Seek medical help fast!")

            else:
                pass

            answer_label = Label(window,
                                 text="Body Mass Index: {:.1f}\n"
                                      "Stones: {}\n"
                                      "Status: {}".format(calculating_bmi, rounding_stones, stats),
                                 justify="center",
                                 font=("comic sans", 10, "bold"),
                                 width=50,
                                 height=5)
            answer_label.place(x=0, y=420)
            entry_height.delete(0, END)
            entry_weight.delete(0, END)
            break
        except ValueError:
            print("Invalid entry!!!!")
            entry_height.delete(0, END)
            entry_weight.delete(0, END)
            break




window = Tk()

window.configure(background="#903cd3")
window.geometry("400x500")
window.resizable(0, 0)
window.title("Body Mass Index")

label_weight = Label(window,
                     text="Weight(KG):",
                     font=("comic sans", 20, "bold"),
                     background="#903cd3",
                     foreground="white"

                     )
label_weight.place(x=10, y=30)

entry_weight = Entry(window,
                     width=25,
                     font=("comic sans", 20, "bold"))
entry_weight.place(x=10, y=70)

#####
label_height = Label(window,
                     text="Height(M):",
                     font=("comic sans", 20, "bold"),
                     background="#903cd3",
                     foreground="white"

                     )
label_height.place(x=10, y=180)

entry_height = Entry(window,
                     width=25,
                     font=("comic sans", 20, "bold"))
entry_height.place(x=10, y=220)

button = Button(window,
                text="Calculate",
                font=("comic sans", 15, "bold"),
                width=10,
                background="#7281dd",
                foreground="white",
                relief="sunken",
                command=cal,
                activebackground="#ec2984",
                activeforeground="white",
                state=ACTIVE,
                )
button.place(x=135, y=320)

window.mainloop()
