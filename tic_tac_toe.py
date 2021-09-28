from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("300x322")
root.resizable(0,0)
root.title("Tic-tac-toe game")
root.wm_iconbitmap("tac_tic_toe.ico")


def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

i=1
def mark(b):
    global i
    i=i+1
    if(i%2==0):
         if(b["text"]==""):
             b["text"] = "0"
    else:
        if (b["text"] == ""):
            b["text"] = "X"
    if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0"):
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0"):
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0"):
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0"):
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0"):
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0"):
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()

    elif(b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0"):
        b3.config(bg="yellow")
        b5.config(bg="yellow")
        b7.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations 0 wins")
        disable_buttons()

    elif(b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        b3.config(bg="yellow")
        b5.config(bg="yellow")
        b7.config(bg="yellow")
        tmsg.showinfo("Tic tac toe", "Congratulations X wins")
        disable_buttons()
    elif(i==9):
        tmsg.showinfo("Tic tac toe", "It's a tie")

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global i
    i=1
    b1=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b1))
    b1.grid(row=0, column=0)
    b2=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b2))
    b2.grid(row=0, column=1)
    b3=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b3))
    b3.grid(row=0, column=2)
    b4=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b4))
    b4.grid(row=1, column=0)
    b5=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b5))
    b5.grid(row=1, column=1)
    b6=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b6))
    b6.grid(row=1, column=2)
    b7=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b7))
    b7.grid(row=2, column=0)
    b8=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b8))
    b8.grid(row=2, column=1)
    b9=Button(root, height=6, width=13, activebackground="grey", command=lambda :mark(b9))
    b9.grid(row=2, column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

my_option = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="More", menu=my_option)
my_option.add_command(label="Restart", command=reset)
reset()
root.mainloop()