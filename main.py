import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
from tkinter import messagebox

field = pd.DataFrame([[None, None, None], [None, None, None], [None, None, None]])


class App:
    def __init__(self, root):
        # setting title
        root.title("Tic Tac Toe game")
        # setting window size
        width = 506
        height = 545
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        button_x1 = tk.Button(root)
        button_x1["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x1["font"] = ft
        button_x1["fg"] = "#ffffff"
        button_x1["justify"] = "center"
        button_x1["text"] = "X"
        button_x1.place(x=100, y=140, width=40, height=25)
        button_x1["command"] = self.button_x1_command

        button_x2 = tk.Button(root)
        button_x2["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x2["font"] = ft
        button_x2["fg"] = "#ffffff"
        button_x2["justify"] = "center"
        button_x2["text"] = "X"
        button_x2.place(x=200, y=140, width=40, height=25)
        button_x2["command"] = self.button_x2_command

        button_x3 = tk.Button(root)
        button_x3["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x3["font"] = ft
        button_x3["fg"] = "#ffffff"
        button_x3["justify"] = "center"
        button_x3["text"] = "X"
        button_x3.place(x=300, y=140, width=40, height=25)
        button_x3["command"] = self.button_x3_command

        button_x4 = tk.Button(root)
        button_x4["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x4["font"] = ft
        button_x4["fg"] = "#ffffff"
        button_x4["justify"] = "center"
        button_x4["text"] = "X"
        button_x4.place(x=100, y=270, width=40, height=25)
        button_x4["command"] = self.button_x4_command

        button_x5 = tk.Button(root)
        button_x5["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x5["font"] = ft
        button_x5["fg"] = "#ffffff"
        button_x5["justify"] = "center"
        button_x5["text"] = "X"
        button_x5.place(x=200, y=270, width=40, height=25)
        button_x5["command"] = self.button_x5_command

        button_x6 = tk.Button(root)
        button_x6["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x6["font"] = ft
        button_x6["fg"] = "#ffffff"
        button_x6["justify"] = "center"
        button_x6["text"] = "X"
        button_x6.place(x=300, y=270, width=40, height=25)
        button_x6["command"] = self.button_x6_command

        button_x7 = tk.Button(root)
        button_x7["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x7["font"] = ft
        button_x7["fg"] = "#ffffff"
        button_x7["justify"] = "center"
        button_x7["text"] = "X"
        button_x7.place(x=100, y=400, width=40, height=25)
        button_x7["command"] = self.button_x7_command

        button_x8 = tk.Button(root)
        button_x8["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x8["font"] = ft
        button_x8["fg"] = "#ffffff"
        button_x8["justify"] = "center"
        button_x8["text"] = "X"
        button_x8.place(x=200, y=400, width=40, height=25)
        button_x8["command"] = self.button_x8_command

        button_x9 = tk.Button(root)
        button_x9["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        button_x9["font"] = ft
        button_x9["fg"] = "#ffffff"
        button_x9["justify"] = "center"
        button_x9["text"] = "X"
        button_x9.place(x=300, y=400, width=40, height=25)
        button_x9["command"] = self.button_x9_command

        self.g_message_00 = tk.Message(root)
        self.g_message_00["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_00["font"] = ft
        self.g_message_00["fg"] = "#333333"
        self.g_message_00["justify"] = "center"
        self.g_message_00["text"] = ""
        self.g_message_00.place(x=100, y=40, width=90, height=90)

        self.g_message_10 = tk.Message(root)
        self.g_message_10["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_10["font"] = ft
        self.g_message_10["fg"] = "#333333"
        self.g_message_10["justify"] = "center"
        self.g_message_10["text"] = ""
        self.g_message_10.place(x=100, y=170, width=90, height=90)

        self.g_message_20 = tk.Message(root)
        self.g_message_20["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_20["font"] = ft
        self.g_message_20["fg"] = "#333333"
        self.g_message_20["justify"] = "center"
        self.g_message_20["text"] = ""
        self.g_message_20.place(x=100, y=300, width=90, height=90)

        self.g_message_01 = tk.Message(root)
        self.g_message_01["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_01["font"] = ft
        self.g_message_01["fg"] = "#333333"
        self.g_message_01["justify"] = "center"
        self.g_message_01["text"] = ""
        self.g_message_01.place(x=200, y=40, width=90, height=90)

        self.g_message_11 = tk.Message(root)
        self.g_message_11["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_11["font"] = ft
        self.g_message_11["fg"] = "#333333"
        self.g_message_11["justify"] = "center"
        self.g_message_11["text"] = ""
        self.g_message_11.place(x=200, y=170, width=90, height=90)

        self.g_message_21 = tk.Message(root)
        self.g_message_21["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_21["font"] = ft
        self.g_message_21["fg"] = "#333333"
        self.g_message_21["justify"] = "center"
        self.g_message_21["text"] = ""
        self.g_message_21.place(x=200, y=300, width=90, height=90)

        self.g_message_02 = tk.Message(root)
        self.g_message_02["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_02["font"] = ft
        self.g_message_02["fg"] = "#333333"
        self.g_message_02["justify"] = "center"
        self.g_message_02["text"] = ""
        self.g_message_02.place(x=300, y=40, width=90, height=90)

        self.g_message_12 = tk.Message(root)
        self.g_message_12["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_12["font"] = ft
        self.g_message_12["fg"] = "#333333"
        self.g_message_12["justify"] = "center"
        self.g_message_12["text"] = ""
        self.g_message_12.place(x=300, y=170, width=90, height=90)

        self.g_message_22 = tk.Message(root)
        self.g_message_22["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times', size=30)
        self.g_message_22["font"] = ft
        self.g_message_22["fg"] = "#333333"
        self.g_message_22["justify"] = "center"
        self.g_message_22["text"] = ""
        self.g_message_22.place(x=300, y=300, width=90, height=90)

        button_o1 = tk.Button(root)
        button_o1["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o1["font"] = ft
        button_o1["fg"] = "#000000"
        button_o1["justify"] = "center"
        button_o1["text"] = "O"
        button_o1.place(x=150, y=140, width=40, height=25)
        button_o1["command"] = self.button_o1_command

        button_o2 = tk.Button(root)
        button_o2["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o2["font"] = ft
        button_o2["fg"] = "#000000"
        button_o2["justify"] = "center"
        button_o2["text"] = "O"
        button_o2.place(x=250, y=140, width=40, height=25)
        button_o2["command"] = self.button_o2_command

        button_o3 = tk.Button(root)
        button_o3["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o3["font"] = ft
        button_o3["fg"] = "#000000"
        button_o3["justify"] = "center"
        button_o3["text"] = "O"
        button_o3.place(x=250, y=270, width=40, height=25)
        button_o3["command"] = self.button_o3_command

        button_o4 = tk.Button(root)
        button_o4["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o4["font"] = ft
        button_o4["fg"] = "#000000"
        button_o4["justify"] = "center"
        button_o4["text"] = "O"
        button_o4.place(x=150, y=270, width=40, height=25)
        button_o4["command"] = self.button_o4_command

        button_o5 = tk.Button(root)
        button_o5["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o5["font"] = ft
        button_o5["fg"] = "#000000"
        button_o5["justify"] = "center"
        button_o5["text"] = "O"
        button_o5.place(x=350, y=140, width=40, height=25)
        button_o5["command"] = self.button_o5_command

        button_o6 = tk.Button(root)
        button_o6["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o6["font"] = ft
        button_o6["fg"] = "#000000"
        button_o6["justify"] = "center"
        button_o6["text"] = "O"
        button_o6.place(x=350, y=270, width=40, height=25)
        button_o6["command"] = self.button_o6_command

        button_o7 = tk.Button(root)
        button_o7["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o7["font"] = ft
        button_o7["fg"] = "#000000"
        button_o7["justify"] = "center"
        button_o7["text"] = "O"
        button_o7.place(x=150, y=400, width=40, height=25)
        button_o7["command"] = self.button_o7_command

        button_o8 = tk.Button(root)
        button_o8["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o8["font"] = ft
        button_o8["fg"] = "#000000"
        button_o8["justify"] = "center"
        button_o8["text"] = "O"
        button_o8.place(x=250, y=400, width=40, height=25)
        button_o8["command"] = self.button_o8_command

        button_o9 = tk.Button(root)
        button_o9["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        button_o9["font"] = ft
        button_o9["fg"] = "#000000"
        button_o9["justify"] = "center"
        button_o9["text"] = "O"
        button_o9.place(x=350, y=400, width=40, height=25)
        button_o9["command"] = self.button_o9_command

        GLabel_675 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_675["font"] = ft
        GLabel_675["fg"] = "#333333"
        GLabel_675["justify"] = "center"
        GLabel_675["text"] = "Tic Tac Toe"
        GLabel_675["relief"] = "ridge"
        GLabel_675.place(x=130, y=10, width=223, height=30)

    def button_x1_command(self):
        self.g_message_00["bg"] = "#00babd"
        self.g_message_00["fg"] = "#ffffff"
        self.g_message_00["text"] = "❌"
        field.iloc[0, 0] = 1
        self.check_sum()

    def button_x2_command(self):
        self.g_message_01["bg"] = "#00babd"
        self.g_message_01["fg"] = "#ffffff"
        self.g_message_01["text"] = "❌"
        field.iloc[0, 1] = 1
        self.check_sum()

    def button_x3_command(self):
        self.g_message_02["bg"] = "#00babd"
        self.g_message_02["fg"] = "#ffffff"
        self.g_message_02["text"] = "❌"
        field.iloc[0, 2] = 1
        self.check_sum()

    def button_x4_command(self):
        self.g_message_10["bg"] = "#00babd"
        self.g_message_10["fg"] = "#ffffff"
        self.g_message_10["text"] = "❌"
        field.iloc[1, 0] = 1
        self.check_sum()

    def button_x5_command(self):
        self.g_message_11["bg"] = "#00babd"
        self.g_message_11["fg"] = "#ffffff"
        self.g_message_11["text"] = "❌"
        field.iloc[1, 1] = 1
        self.check_sum()

    def button_x6_command(self):
        self.g_message_12["bg"] = "#00babd"
        self.g_message_12["fg"] = "#ffffff"
        self.g_message_12["text"] = "❌"
        field.iloc[1, 2] = 1
        self.check_sum()

    def button_x7_command(self):
        self.g_message_20["bg"] = "#00babd"
        self.g_message_20["fg"] = "#ffffff"
        self.g_message_20["text"] = "❌"
        field.iloc[2, 0] = 1
        self.check_sum()

    def button_x8_command(self):
        self.g_message_21["bg"] = "#00babd"
        self.g_message_21["fg"] = "#ffffff"
        self.g_message_21["text"] = "❌"
        field.iloc[2, 1] = 1
        self.check_sum()

    def button_x9_command(self):
        self.g_message_22["bg"] = "#00babd"
        self.g_message_22["fg"] = "#ffffff"
        self.g_message_22["text"] = "❌"
        field.iloc[2, 2] = 1
        self.check_sum()

    def button_o1_command(self):
        self.g_message_00["bg"] = "#ff8c00"
        self.g_message_00["fg"] = "#ffffff"
        self.g_message_00["text"] = "⭕"
        field.iloc[0, 0] = 0
        self.check_sum()

    def button_o2_command(self):
        self.g_message_01["bg"] = "#ff8c00"
        self.g_message_01["fg"] = "#ffffff"
        self.g_message_01["text"] = "⭕"
        field.iloc[0, 1] = 0
        self.check_sum()

    def button_o3_command(self):
        self.g_message_11["bg"] = "#ff8c00"
        self.g_message_11["fg"] = "#ffffff"
        self.g_message_11["text"] = "⭕"
        field.iloc[1, 1] = 0
        self.check_sum()

    def button_o4_command(self):
        self.g_message_10["bg"] = "#ff8c00"
        self.g_message_10["fg"] = "#ffffff"
        self.g_message_10["text"] = "⭕"
        field.iloc[1, 0] = 0
        self.check_sum()

    def button_o5_command(self):
        self.g_message_02["bg"] = "#ff8c00"
        self.g_message_02["fg"] = "#ffffff"
        self.g_message_02["text"] = "⭕"
        field.iloc[0, 2] = 0
        self.check_sum()

    def button_o6_command(self):
        self.g_message_12["bg"] = "#ff8c00"
        self.g_message_12["fg"] = "#ffffff"
        self.g_message_12["text"] = "⭕"
        field.iloc[1, 2] = 0
        self.check_sum()

    def button_o7_command(self):
        self.g_message_20["bg"] = "#ff8c00"
        self.g_message_20["fg"] = "#ffffff"
        self.g_message_20["text"] = "⭕"
        field.iloc[2, 0] = 0
        self.check_sum()

    def button_o8_command(self):
        self.g_message_21["bg"] = "#ff8c00"
        self.g_message_21["fg"] = "#ffffff"
        self.g_message_21["text"] = "⭕"
        field.iloc[2, 1] = 0
        self.check_sum()

    def button_o9_command(self):
        self.g_message_22["bg"] = "#ff8c00"
        self.g_message_22["fg"] = "#ffffff"
        self.g_message_22["text"] = "⭕"
        field.iloc[2, 2] = 0
        self.check_sum()

    def check_sum(self):
        field['sum_1'] = field[[0, 1, 2]].sum(axis=1)
        field['sum_0'] = (field[[0, 1, 2]] == 0).sum(axis=1)
        field.loc["sum_1"] = field.iloc[0:3, 0:3].sum()
        field.loc["sum_0"] = (field.iloc[0:3, 0:3] == 0).sum()

        field.iloc[3, 3] = 3 if field.iloc[0, 0] == field.iloc[1, 1] == field.iloc[2, 2] == 1 or field.iloc[0, 2] == \
                                field.iloc[1, 1] == field.iloc[2, 0] == 1 else 0

        field.loc['sum_0', ['sum_1']] = field.loc['sum_0', ['sum_0']] = 0
        field.iloc[4, 4] = 3 if field.iloc[0, 2] == field.iloc[1, 1] == field.iloc[2, 0] == 0 or field.iloc[0, 0] == \
                                field.iloc[1, 1] == field.iloc[2, 2] == 0 else 0

        if 3 in field['sum_0'].values or 3 in field.loc["sum_0"].values:
            is_ok = messagebox.showinfo(title="WIN",
                                        message="Player 0 win!")
            if is_ok:
                root.destroy()

        if 3 in field['sum_1'].values or 3 in field.loc["sum_1"].values:
            is_ok = messagebox.showinfo(title="WIN",
                                        message="Player X win!")
            if is_ok:
                root.destroy()

        if None not in field.iloc[0:3, 0:3].values:
            is_ok = messagebox.showinfo(title="Draw",
                                        message="Nobody win")
            if is_ok:
                root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
