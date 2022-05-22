from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("python project")


def botonat(iteams):
    global expression
    expression = expression + str(iteams)
    input_text.set(expression)


def delete_all():
    global expression
    expression = ""
    input_text.set("")


def equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""

input_text = StringVar()

the_screen = Frame(win, width=312, height=50, bd=0,
                   highlightbackground="#9400D3", highlightcolor="skyblue", highlightthickness=5)

the_screen.pack(side=TOP)

the_screen = Entry(the_screen, font=('arial', 18, 'bold'),
                   textvariable=input_text, width=50, bg="black", bd=0, fg="white", justify=RIGHT)

the_screen.pack(ipady=10)

buttons_display = Frame(win, width=312, height=272.5, bg="#9400D3")

buttons_display.pack()

mhi = Button(buttons_display, text="delete_all", fg="gold", width=32, height=3, bd=0, bg="black",
             cursor="hand2", command=lambda: delete_all()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(buttons_display, text="/", fg="gold", width=10, height=3, bd=0, bg="black",
                cursor="hand2", command=lambda: botonat("/")).grid(row=0, column=3, padx=1, pady=1)

seven = Button(buttons_display, text="7", fg="gold", width=10, height=3, bd=0, bg="black",
               cursor="hand2", command=lambda: botonat(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(buttons_display, text="8", fg="gold", width=10, height=3, bd=0, bg="black",
               cursor="hand2", command=lambda: botonat(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(buttons_display, text="9", fg="gold", width=10, height=3, bd=0, bg="black",
              cursor="hand2", command=lambda: botonat(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(buttons_display, text="*", fg="gold", width=10, height=3, bd=0, bg="black",
                  cursor="hand2", command=lambda: botonat("*")).grid(row=1, column=3, padx=1, pady=1)

four = Button(buttons_display, text="4", fg="gold", width=10, height=3, bd=0, bg="black",
              cursor="hand2", command=lambda: botonat(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(buttons_display, text="5", fg="gold", width=10, height=3, bd=0, bg="black",
              cursor="hand2", command=lambda: botonat(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(buttons_display, text="6", fg="gold", width=10, height=3, bd=0, bg="black",
             cursor="hand2", command=lambda: botonat(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(buttons_display, text="-", fg="gold", width=10, height=3, bd=0, bg="black",
               cursor="hand2", command=lambda: botonat("-")).grid(row=2, column=3, padx=1, pady=1)

one = Button(buttons_display, text="1", fg="gold", width=10, height=3, bd=0, bg="black",
             cursor="hand2", command=lambda: botonat(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(buttons_display, text="2", fg="gold", width=10, height=3, bd=0, bg="black",
             cursor="hand2", command=lambda: botonat(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(buttons_display, text="3", fg="gold", width=10, height=3, bd=0, bg="black",
               cursor="hand2", command=lambda: botonat(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(buttons_display, text="+", fg="gold", width=10, height=3, bd=0, bg="black",
              cursor="hand2", command=lambda: botonat("+")).grid(row=3, column=3, padx=1, pady=1)

zero = Button(buttons_display, text="0", fg="gold", width=21, height=3, bd=0, bg="black", cursor="hand2",
              command=lambda: botonat(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

la_vriguluououo = Button(buttons_display, text=",", fg="gold", width=10, height=3, bd=0, bg="black",
                         cursor="hand2", command=lambda: botonat(",")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(buttons_display, text="=", fg="gold", width=10, height=3, bd=0, bg="black",
                cursor="hand2", command=lambda: equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
