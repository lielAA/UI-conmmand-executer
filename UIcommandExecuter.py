from tkinter import Tk, Button, Label, Entry, Text, END
import os


# execute command from entry by os.popen and print to the txt box
def executer_func():
    command = txtField.get()
    try:
        data = os.popen(command).read()
    except:
        data = "'{0}' is not recognized as an internal or external command,operable program or batch file.".format(command)
    txtBx.insert(END, data)


# clear text from txt box
def clear_text():
    txtBx.delete('0.0', END)


masterW = Tk()
masterW.title("executerCMD")
masterW.geometry("450x450")
masterW.iconbitmap('cmd_16549.ico')
masterW.resizable(False, False)

# execute command button
executeBtn = Button(masterW, text="execute", command=executer_func)
executeBtn.place(x=382, y=5)

# clear TextBox button
clearTXB = Button(masterW, text="clear", command=clear_text)
clearTXB.place(x=400, y=370)


# Command label
lbl = Label(masterW, text="Command: ")
lbl.place(x=0, y=10)

# Entry label (text field)
txtField = Entry(masterW, width="50", bd="3")
txtField.place(x=65, y=10)

# TextBox
txtBx = Text(masterW, width="53", height="20", bd="3")
txtBx.place(x=5, y=40)

masterW.mainloop()
