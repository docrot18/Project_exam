import math
import re
import tkinter
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Roboto", 35, "bold"), bg="#F8F8FF", foreground="#000000")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "=", "*", "x^2", "Graph",
            "1", "2", "3", "/", "**", "Pi",
            "4", "5", "6", "+", "10^x", "|x|",
            "7", "8", "9", "-", "√", "x!",
            "(", "0", ")", "+-", "MOD", "log(x)",
            "sin", "cos", "tg", "ctn", "1/x", "ln(x)"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#B0C4DE", font=("Roboto", 16), command=com).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 600:
                x = 10
                y += 81

    def logicalc(self, operation):

        if operation == "C":
            self.formula = ""

        elif operation == "/":
            if self.formula[-1] in '+-*/%':
                self.formula = self.formula[:-1]
            self.formula = self.formula + "/"

        elif operation == "*":
            if self.formula[-1] in '+-*/%':
                self.formula = self.formula[:-1]
            self.formula = self.formula + "*"

        elif operation == "-":
            if self.formula[-1] in '+-*/%':
                self.formula = self.formula[:-1]
            self.formula = self.formula + "-"

        elif operation == "+":
            if self.formula[-1] in '+-*/%':
                self.formula = self.formula[:-1]
            self.formula = self.formula + "+"

        elif operation == "DEL":
            self.formula = self.formula[0:-1]

        elif operation == "√":
            if eval(self.formula) < 0:
                self.formula = "Error"
            elif eval(self.formula) >= 0:
                self.formula = str((eval(self.formula)) ** 0.5)

        elif operation == "sin":
            self.formula = str(math.radians(eval(self.formula)))
            self.formula = str(math.sin((eval(self.formula))))
            self.formula = round((eval(self.formula)), 2)

        elif operation == "cos":
            self.formula = str(math.radians(eval(self.formula)))
            self.formula = str(math.cos((eval(self.formula))))
            self.formula = round((eval(self.formula)), 2)

        elif operation == "ctn":
            if eval(self.formula) == 180 or eval(self.formula) == 360 or eval(self.formula) > 360:
                self.formula = "Error"
            elif eval(self.formula) != 180 or eval(self.formula) != 360:
                self.formula = str(math.radians(eval(self.formula)))
                self.formula = str(1 / math.tan((eval(self.formula))))
                self.formula = round((eval(self.formula)), 2)

        elif operation == "tg":
            if eval(self.formula) == 90 or eval(self.formula) == 270 or eval(self.formula) > 360:
                self.formula = "Error"
            elif eval(self.formula) != 90 or eval(self.formula) != 270:
                self.formula = str(math.radians(eval(self.formula)))
                self.formula = str(math.tan((eval(self.formula))))
                self.formula = round((eval(self.formula)), 2)

        elif operation == "=":
            self.formula = str(eval(self.formula))

        elif operation == "x^2":
            self.formula = str(math.pow((eval(self.formula)), 2))

        elif operation == "10^x":
            self.formula = str(10 ** eval(self.formula))

        elif operation == "+-":
            self.formula = str(-1 * eval(self.formula))

        elif operation == "MOD":
            if self.formula[-1] in '+-*/%':
                self.formula = self.formula[:-1]
            self.formula = self.formula + "%"

        elif operation == "1/x":
            self.formula = str(1 / eval(self.formula))

        elif operation == "Pi":
            self.formula = math.pi

        elif operation == "|x|":
            self.formula = str(abs(eval(self.formula)))

        elif operation == "x!":
            self.formula = str(math.factorial(eval(self.formula)))

        elif operation == "log(x)":
            self.formula = str(math.log10(eval(self.formula)))

        elif operation == "ln(x)":
            self.formula = str(math.log(eval(self.formula)))

        elif operation == "Graph":
            self.OpenGraph()


        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

    def OpenGraph(self):
        top = Toplevel()
        top.title("GRAPH")
        top.geometry("1000x600")
        exampleText = StringVar
        Intext = StringVar
        Intext2 = StringVar
        top.resizable(False, False)
        text = Label(top, text="Введите выражение", font="Roboto 30", ).place(rely=0.25, relx=0.3)
        textY = Label(top, text="Y=", font="Roboto 30").place(rely=0.335, relx=0.31)
        textIn = Label(top, text="в интервале от", font="Roboto 15").place(rely=0.435, relx=0.28)
        textIn2 = Label(top, text="до", font="Roboto 15").place(rely=0.435, relx=0.49)
        example = Entry(top, textvariable=exampleText, font="Roboto 30", width=13)
        example.pack(padx=375, pady=(200, 0))
        x1 = Entry(top, textvariable=Intext, font="Roboto 15", width=3)
        x1.place(relx=0.44, rely=0.44)
        x2 = Entry(top, textvariable=Intext2, font="Roboto 15", width=3)
        x2.place(relx=0.53, rely=0.44)
        result = Button(top, text="Построить график", font="Roboto 15", width=15, height=1,
                        command=lambda: self.GraphBuild(example.get(), x1.get(), x2.get())).place(rely=0.53, relx=0.4)

    def GraphBuild(self, test, x1, x2):
        plt.rcParams['toolbar'] = 'None'
        x = np.linspace(int(x1), int(x2), 101)
        s = test
        if 'x**' in s:
            a, oper, b = test.partition('**')
            if a == 'x':
                y1 = x ** int(re.sub('\D', '', test))
            else:
                y1 = int(re.sub('\D', '', a)) * x ** int(b)
        elif 'x*' in s:
            a, oper, b = test.partition('*')
            if a == 'x':
                y1 = x * int(re.sub('\D', '', test))
            else:
                y1 = int(re.sub('\D', '', a)) * x * int(b)
        elif 'x+' in s:
            a, oper, b = test.partition('+')
            if a == 'x':
                y1 = x + int(re.sub('\D', '', test))
            else:
                y1 = int(re.sub('\D', '', a)) * x + int(b)
        elif 'x-' in s:
            a, oper, b = test.partition('-')
            if a == 'x':
                y1 = x - int(re.sub('\D', '', test))
            else:
                y1 = int(re.sub('\D', '', a)) * x - int(b)
        elif '/x' in s:
            y1 = int(re.sub('\D', '', test)) / x
        elif 'sin' in s:
            y1 = np.sin(x)
        elif 'cos' in s:
            y1 = np.cos(x)
        elif 'tg' in s:
            y1 = np.tan(x)
        else:
            test = str(eval(test))
            y1 = np.linspace(int(test), int(test), 101)
        ay, ax = plt.subplots()
        plt.plot([int(x1), int(x2)], [0, 0], color='black')
        plt.plot([0, 0], [-y1, y1], color='black')
        ax.plot(x, y1, linestyle='solid')
        plt.show()


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#F8F8FF"
    root.geometry("720x640+400+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
