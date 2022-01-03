import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        root.configure(background = 'black')
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_192=tk.Button(root)
        GButton_192["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_192["font"] = ft
        GButton_192["fg"] = "#c13535"
        GButton_192["justify"] = "center"
        GButton_192["text"] = "FINISH"
        GButton_192.place(x=400,y=200,width=70,height=25)
        GButton_192["command"] = self.GButton_192_command
        
        GLabel_722=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_722["font"] = ft
        GLabel_722["fg"] = "#333333"
        GLabel_722["justify"] = "center"
        GLabel_722["text"] = "label"
        GLabel_722.place(x=60,y=50,width=70,height=25)

        GLineEdit_299=tk.Entry(root)
        GLineEdit_299["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_299["font"] = ft
        GLineEdit_299["fg"] = "#333333"
        GLineEdit_299["justify"] = "center"
        GLineEdit_299["text"] = "Entry"
        GLineEdit_299.place(x=160,y=50,width=70,height=25)

        GLineEdit_333=tk.Entry(root)
        GLineEdit_333["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_333["font"] = ft
        GLineEdit_333["fg"] = "#333333"
        GLineEdit_333["justify"] = "center"
        GLineEdit_333["text"] = "Entry"
        GLineEdit_333.place(x=300,y=50,width=70,height=25)

        GLabel_203=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_203["font"] = ft
        GLabel_203["fg"] = "#333333"
        GLabel_203["justify"] = "center"
        GLabel_203["text"] = "label"
        GLabel_203.place(x=60,y=90,width=70,height=25)

        GLineEdit_429=tk.Entry(root)
        GLineEdit_429["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_429["font"] = ft
        GLineEdit_429["fg"] = "#333333"
        GLineEdit_429["justify"] = "center"
        GLineEdit_429["text"] = "Entry"
        GLineEdit_429.place(x=160,y=90,width=70,height=25)

        GLineEdit_814=tk.Entry(root)
        GLineEdit_814["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_814["font"] = ft
        GLineEdit_814["fg"] = "#333333"
        GLineEdit_814["justify"] = "center"
        GLineEdit_814["text"] = "Entry"
        GLineEdit_814.place(x=300,y=90,width=70,height=25)

        GLabel_77=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_77["font"] = ft
        GLabel_77["fg"] = "#333333"
        GLabel_77["justify"] = "center"
        GLabel_77["text"] = "label"
        GLabel_77.place(x=60,y=130,width=70,height=25)

        GLineEdit_326=tk.Entry(root)
        GLineEdit_326["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_326["font"] = ft
        GLineEdit_326["fg"] = "#333333"
        GLineEdit_326["justify"] = "center"
        GLineEdit_326["text"] = "Entry"
        GLineEdit_326.place(x=160,y=130,width=70,height=25)

        GLineEdit_112=tk.Entry(root)
        GLineEdit_112["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_112["font"] = ft
        GLineEdit_112["fg"] = "#333333"
        GLineEdit_112["justify"] = "center"
        GLineEdit_112["text"] = "Entry"
        GLineEdit_112.place(x=300,y=130,width=70,height=25)

        GLabel_176=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_176["font"] = ft
        GLabel_176["fg"] = "#333333"
        GLabel_176["justify"] = "center"
        GLabel_176["text"] = "label"
        GLabel_176.place(x=60,y=170,width=70,height=25)

        GLineEdit_497=tk.Entry(root)
        GLineEdit_497["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_497["font"] = ft
        GLineEdit_497["fg"] = "#333333"
        GLineEdit_497["justify"] = "center"
        GLineEdit_497["text"] = "Entry"
        GLineEdit_497.place(x=160,y=170,width=70,height=25)

        GLineEdit_898=tk.Entry(root)
        GLineEdit_898["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_898["font"] = ft
        GLineEdit_898["fg"] = "#333333"
        GLineEdit_898["justify"] = "center"
        GLineEdit_898["text"] = "Entry"
        GLineEdit_898.place(x=300,y=170,width=70,height=25)

        GLabel_652=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_652["font"] = ft
        GLabel_652["fg"] = "#333333"
        GLabel_652["justify"] = "center"
        GLabel_652["text"] = "label"
        GLabel_652.place(x=60,y=210,width=70,height=25)

        GLineEdit_150=tk.Entry(root)
        GLineEdit_150["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_150["font"] = ft
        GLineEdit_150["fg"] = "#333333"
        GLineEdit_150["justify"] = "center"
        GLineEdit_150["text"] = "Entry"
        GLineEdit_150.place(x=160,y=210,width=70,height=25)

        GLineEdit_86=tk.Entry(root)
        GLineEdit_86["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_86["font"] = ft
        GLineEdit_86["fg"] = "#333333"
        GLineEdit_86["justify"] = "center"
        GLineEdit_86["text"] = "Entry"
        GLineEdit_86.place(x=300,y=210,width=70,height=25)

        GLabel_30=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_30["font"] = ft
        GLabel_30["fg"] = "#333333"
        GLabel_30["justify"] = "center"
        GLabel_30["text"] = "label"
        GLabel_30.place(x=60,y=250,width=70,height=25)

        GLineEdit_44=tk.Entry(root)
        GLineEdit_44["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_44["font"] = ft
        GLineEdit_44["fg"] = "#333333"
        GLineEdit_44["justify"] = "center"
        GLineEdit_44["text"] = "Entry"
        GLineEdit_44.place(x=160,y=250,width=70,height=25)

        GLineEdit_394=tk.Entry(root)
        GLineEdit_394["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_394["font"] = ft
        GLineEdit_394["fg"] = "#333333"
        GLineEdit_394["justify"] = "center"
        GLineEdit_394["text"] = "Entry"
        GLineEdit_394.place(x=300,y=250,width=70,height=25)

        GLabel_723=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_723["font"] = ft
        GLabel_723["fg"] = "#333333"
        GLabel_723["justify"] = "center"
        GLabel_723["text"] = "label"
        GLabel_723.place(x=60,y=290,width=70,height=25)

        GLineEdit_211=tk.Entry(root)
        GLineEdit_211["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_211["font"] = ft
        GLineEdit_211["fg"] = "#333333"
        GLineEdit_211["justify"] = "center"
        GLineEdit_211["text"] = "Entry"
        GLineEdit_211.place(x=160,y=290,width=70,height=25)

        GLineEdit_918=tk.Entry(root)
        GLineEdit_918["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_918["font"] = ft
        GLineEdit_918["fg"] = "#333333"
        GLineEdit_918["justify"] = "center"
        GLineEdit_918["text"] = "Entry"
        GLineEdit_918.place(x=300,y=290,width=70,height=25)

        GLabel_221=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_221["font"] = ft
        GLabel_221["fg"] = "#333333"
        GLabel_221["justify"] = "center"
        GLabel_221["text"] = "label"
        GLabel_221.place(x=60,y=330,width=70,height=25)

        GLineEdit_554=tk.Entry(root)
        GLineEdit_554["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_554["font"] = ft
        GLineEdit_554["fg"] = "#333333"
        GLineEdit_554["justify"] = "center"
        GLineEdit_554["text"] = "Entry"
        GLineEdit_554.place(x=160,y=330,width=70,height=25)

        GLineEdit_105=tk.Entry(root)
        GLineEdit_105["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_105["font"] = ft
        GLineEdit_105["fg"] = "#333333"
        GLineEdit_105["justify"] = "center"
        GLineEdit_105["text"] = "Entry"
        GLineEdit_105.place(x=300,y=330,width=70,height=25)

        GLabel_313=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_313["font"] = ft
        GLabel_313["fg"] = "#333333"
        GLabel_313["justify"] = "center"
        GLabel_313["text"] = "label"
        GLabel_313.place(x=60,y=370,width=70,height=25)

        GLineEdit_682=tk.Entry(root)
        GLineEdit_682["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_682["font"] = ft
        GLineEdit_682["fg"] = "#333333"
        GLineEdit_682["justify"] = "center"
        GLineEdit_682["text"] = "Entry"
        GLineEdit_682.place(x=160,y=370,width=70,height=25)

        GLineEdit_109=tk.Entry(root)
        GLineEdit_109["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_109["font"] = ft
        GLineEdit_109["fg"] = "#333333"
        GLineEdit_109["justify"] = "center"
        GLineEdit_109["text"] = "Entry"
        GLineEdit_109.place(x=300,y=370,width=70,height=25)

        GLabel_733=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_733["font"] = ft
        GLabel_733["fg"] = "#333333"
        GLabel_733["justify"] = "center"
        GLabel_733["text"] = "label"
        GLabel_733.place(x=60,y=410,width=70,height=25)

        GLineEdit_604=tk.Entry(root)
        GLineEdit_604["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_604["font"] = ft
        GLineEdit_604["fg"] = "#333333"
        GLineEdit_604["justify"] = "center"
        GLineEdit_604["text"] = "Entry"
        GLineEdit_604.place(x=160,y=410,width=70,height=25)

        GLineEdit_364=tk.Entry(root)
        GLineEdit_364["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_364["font"] = ft
        GLineEdit_364["fg"] = "#333333"
        GLineEdit_364["justify"] = "center"
        GLineEdit_364["text"] = "Entry"
        GLineEdit_364.place(x=300,y=410,width=70,height=25)

        GLabel_728=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_728["font"] = ft
        GLabel_728["fg"] = "#333333"
        GLabel_728["justify"] = "center"
        GLabel_728["text"] = "label"
        GLabel_728.place(x=60,y=450,width=70,height=25)

        GLineEdit_628=tk.Entry(root)
        GLineEdit_628["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_628["font"] = ft
        GLineEdit_628["fg"] = "#333333"
        GLineEdit_628["justify"] = "center"
        GLineEdit_628["text"] = "Entry"
        GLineEdit_628.place(x=160,y=450,width=70,height=25)

        GLineEdit_402=tk.Entry(root)
        GLineEdit_402["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_402["font"] = ft
        GLineEdit_402["fg"] = "#333333"
        GLineEdit_402["justify"] = "center"
        GLineEdit_402["text"] = "Entry"
        GLineEdit_402.place(x=300,y=450,width=70,height=25)

        GLabel_285=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_285["font"] = ft
        GLabel_285["fg"] = "#333333"
        GLabel_285["justify"] = "center"
        GLabel_285["text"] = "Runs"
        GLabel_285.place(x=160,y=10,width=70,height=25)

        GLabel_780=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_780["font"] = ft
        GLabel_780["fg"] = "#333333"
        GLabel_780["justify"] = "center"
        GLabel_780["text"] = "Wickets"
        GLabel_780.place(x=300,y=10,width=70,height=25)
    def GButton_192_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
