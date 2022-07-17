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

        self.button_510 = tk.Button(root)
        self.button_510["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        self.button_510["font"] = ft
        self.button_510["fg"] = "#ffffff"
        self.button_510["justify"] = "center"
        self.button_510["text"] = "X"
        self.button_510.place(x=100, y=140, width=40, height=25)
        self.button_510["command"] = self.GButton_510_command

        self.GButton_99 = tk.Button(root)
        self.GButton_99["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        self.GButton_99["font"] = ft
        self.GButton_99["fg"] = "#ffffff"
        self.GButton_99["justify"] = "center"
        self.GButton_99["text"] = "X"
        self.GButton_99.place(x=200, y=140, width=40, height=25)
        self.GButton_99["command"] = self.GButton_99_command

        self.GButton_45 = tk.Button(root)
        self.GButton_45["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        self.GButton_45["font"] = ft
        self.GButton_45["fg"] = "#ffffff"
        self.GButton_45["justify"] = "center"
        self.GButton_45["text"] = "X"
        self.GButton_45.place(x=300, y=140, width=40, height=25)
        self.GButton_45["command"] = self.GButton_45_command

        GButton_881 = tk.Button(root)
        GButton_881["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        GButton_881["font"] = ft
        GButton_881["fg"] = "#ffffff"
        GButton_881["justify"] = "center"
        GButton_881["text"] = "X"
        GButton_881.place(x=100, y=270, width=40, height=25)
        GButton_881["command"] = self.GButton_881_command

        GButton_255 = tk.Button(root)
        GButton_255["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        GButton_255["font"] = ft
        GButton_255["fg"] = "#ffffff"
        GButton_255["justify"] = "center"
        GButton_255["text"] = "X"
        GButton_255.place(x=200, y=270, width=40, height=25)
        GButton_255["command"] = self.GButton_255_command

        GButton_578 = tk.Button(root)
        GButton_578["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        GButton_578["font"] = ft
        GButton_578["fg"] = "#ffffff"
        GButton_578["justify"] = "center"
        GButton_578["text"] = "X"
        GButton_578.place(x=300, y=270, width=40, height=25)
        GButton_578["command"] = self.GButton_578_command

        GButton_933 = tk.Button(root)
        GButton_933["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        GButton_933["font"] = ft
        GButton_933["fg"] = "#ffffff"
        GButton_933["justify"] = "center"
        GButton_933["text"] = "X"
        GButton_933.place(x=100, y=400, width=40, height=25)
        GButton_933["command"] = self.GButton_933_command

        GButton_355 = tk.Button(root)
        GButton_355["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        GButton_355["font"] = ft
        GButton_355["fg"] = "#ffffff"
        GButton_355["justify"] = "center"
        GButton_355["text"] = "X"
        GButton_355.place(x=200, y=400, width=40, height=25)
        GButton_355["command"] = self.GButton_355_command

        GButton_860 = tk.Button(root)
        GButton_860["bg"] = "#00babd"
        ft = tkFont.Font(family='Times', size=10)
        GButton_860["font"] = ft
        GButton_860["fg"] = "#ffffff"
        GButton_860["justify"] = "center"
        GButton_860["text"] = "X"
        GButton_860.place(x=300, y=400, width=40, height=25)
        GButton_860["command"] = self.GButton_860_command

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

        GButton_477 = tk.Button(root)
        GButton_477["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_477["font"] = ft
        GButton_477["fg"] = "#000000"
        GButton_477["justify"] = "center"
        GButton_477["text"] = "O"
        GButton_477.place(x=150, y=140, width=40, height=25)
        GButton_477["command"] = self.GButton_477_command

        GButton_423 = tk.Button(root)
        GButton_423["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_423["font"] = ft
        GButton_423["fg"] = "#000000"
        GButton_423["justify"] = "center"
        GButton_423["text"] = "O"
        GButton_423.place(x=250, y=140, width=40, height=25)
        GButton_423["command"] = self.GButton_423_command

        GButton_973 = tk.Button(root)
        GButton_973["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_973["font"] = ft
        GButton_973["fg"] = "#000000"
        GButton_973["justify"] = "center"
        GButton_973["text"] = "O"
        GButton_973.place(x=250, y=270, width=40, height=25)
        GButton_973["command"] = self.GButton_973_command

        GButton_830 = tk.Button(root)
        GButton_830["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_830["font"] = ft
        GButton_830["fg"] = "#000000"
        GButton_830["justify"] = "center"
        GButton_830["text"] = "O"
        GButton_830.place(x=150, y=270, width=40, height=25)
        GButton_830["command"] = self.GButton_830_command

        GButton_615 = tk.Button(root)
        GButton_615["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_615["font"] = ft
        GButton_615["fg"] = "#000000"
        GButton_615["justify"] = "center"
        GButton_615["text"] = "O"
        GButton_615.place(x=350, y=140, width=40, height=25)
        GButton_615["command"] = self.GButton_615_command

        GButton_360 = tk.Button(root)
        GButton_360["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_360["font"] = ft
        GButton_360["fg"] = "#000000"
        GButton_360["justify"] = "center"
        GButton_360["text"] = "O"
        GButton_360.place(x=350, y=270, width=40, height=25)
        GButton_360["command"] = self.GButton_360_command

        GButton_839 = tk.Button(root)
        GButton_839["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_839["font"] = ft
        GButton_839["fg"] = "#000000"
        GButton_839["justify"] = "center"
        GButton_839["text"] = "O"
        GButton_839.place(x=150, y=400, width=40, height=25)
        GButton_839["command"] = self.GButton_839_command

        GButton_769 = tk.Button(root)
        GButton_769["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_769["font"] = ft
        GButton_769["fg"] = "#000000"
        GButton_769["justify"] = "center"
        GButton_769["text"] = "O"
        GButton_769.place(x=250, y=400, width=40, height=25)
        GButton_769["command"] = self.GButton_769_command

        GButton_134 = tk.Button(root)
        GButton_134["bg"] = "#ff8c00"
        ft = tkFont.Font(family='Times', size=10)
        GButton_134["font"] = ft
        GButton_134["fg"] = "#000000"
        GButton_134["justify"] = "center"
        GButton_134["text"] = "O"
        GButton_134.place(x=350, y=400, width=40, height=25)
        GButton_134["command"] = self.GButton_134_command

        GLabel_675 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=18)
        GLabel_675["font"] = ft
        GLabel_675["fg"] = "#333333"
        GLabel_675["justify"] = "center"
        GLabel_675["text"] = "Tic Tac Toe"
        GLabel_675["relief"] = "ridge"
        GLabel_675.place(x=130, y=10, width=223, height=30)

    def GButton_510_command(self):
        self.g_message_00["bg"] = "#00babd"
        self.g_message_00["fg"] = "#ffffff"
        self.g_message_00["text"] = "❌"
        field.iloc[0, 0] = 1
        self.check_sum()

    def GButton_99_command(self):
        self.g_message_01["bg"] = "#00babd"
        self.g_message_01["fg"] = "#ffffff"
        self.g_message_01["text"] = "❌"
        field.iloc[0, 1] = 1
        self.check_sum()

    def GButton_45_command(self):
        self.g_message_02["bg"] = "#00babd"
        self.g_message_02["fg"] = "#ffffff"
        self.g_message_02["text"] = "❌"
        field.iloc[0, 2] = 1
        self.check_sum()

    def GButton_881_command(self):
        self.g_message_10["bg"] = "#00babd"
        self.g_message_10["fg"] = "#ffffff"
        self.g_message_10["text"] = "❌"
        field.iloc[1, 0] = 1
        self.check_sum()

    def GButton_255_command(self):
        self.g_message_11["bg"] = "#00babd"
        self.g_message_11["fg"] = "#ffffff"
        self.g_message_11["text"] = "❌"
        field.iloc[1, 1] = 1
        self.check_sum()

    def GButton_578_command(self):
        self.g_message_12["bg"] = "#00babd"
        self.g_message_12["fg"] = "#ffffff"
        self.g_message_12["text"] = "❌"
        field.iloc[1, 2] = 1
        self.check_sum()

    def GButton_933_command(self):
        self.g_message_20["bg"] = "#00babd"
        self.g_message_20["fg"] = "#ffffff"
        self.g_message_20["text"] = "❌"
        field.iloc[2, 0] = 1
        self.check_sum()

    def GButton_355_command(self):
        self.g_message_21["bg"] = "#00babd"
        self.g_message_21["fg"] = "#ffffff"
        self.g_message_21["text"] = "❌"
        field.iloc[2, 1] = 1
        self.check_sum()

    def GButton_860_command(self):
        self.g_message_22["bg"] = "#00babd"
        self.g_message_22["fg"] = "#ffffff"
        self.g_message_22["text"] = "❌"
        field.iloc[2, 2] = 1
        self.check_sum()

    def GButton_477_command(self):
        self.g_message_00["bg"] = "#ff8c00"
        self.g_message_00["fg"] = "#ffffff"
        self.g_message_00["text"] = "⭕"
        field.iloc[0, 0] = 0
        self.check_sum()

    def GButton_423_command(self):
        self.g_message_01["bg"] = "#ff8c00"
        self.g_message_01["fg"] = "#ffffff"
        self.g_message_01["text"] = "⭕"
        field.iloc[0, 1] = 0
        self.check_sum()

    def GButton_973_command(self):
        self.g_message_11["bg"] = "#ff8c00"
        self.g_message_11["fg"] = "#ffffff"
        self.g_message_11["text"] = "⭕"
        field.iloc[1, 1] = 0
        self.check_sum()

    def GButton_830_command(self):
        self.g_message_10["bg"] = "#ff8c00"
        self.g_message_10["fg"] = "#ffffff"
        self.g_message_10["text"] = "⭕"
        field.iloc[1, 0] = 0
        self.check_sum()

    def GButton_615_command(self):
        self.g_message_02["bg"] = "#ff8c00"
        self.g_message_02["fg"] = "#ffffff"
        self.g_message_02["text"] = "⭕"
        field.iloc[0, 2] = 0
        self.check_sum()

    def GButton_360_command(self):
        self.g_message_12["bg"] = "#ff8c00"
        self.g_message_12["fg"] = "#ffffff"
        self.g_message_12["text"] = "⭕"
        field.iloc[1, 2] = 0
        self.check_sum()

    def GButton_839_command(self):
        self.g_message_20["bg"] = "#ff8c00"
        self.g_message_20["fg"] = "#ffffff"
        self.g_message_20["text"] = "⭕"
        field.iloc[2, 0] = 0
        self.check_sum()

    def GButton_769_command(self):
        self.g_message_21["bg"] = "#ff8c00"
        self.g_message_21["fg"] = "#ffffff"
        self.g_message_21["text"] = "⭕"
        field.iloc[2, 1] = 0
        self.check_sum()

    def GButton_134_command(self):
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


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
