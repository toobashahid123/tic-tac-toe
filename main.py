import tkinter as tk
from tkinter import *
from tkinter import messagebox
# Create the main window
root = tk.Tk()
# Set the window title
root.title("tic tac toe game")
# Set the window size
#root.geometry("300x200")
 

# X starts so true
clicked = False
count = 0 

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# check to see if someone won

def checkifwon():
    global winner
    winner = False

    if b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X':
        b1.config(bg = 'red')
        b2.config(bg = 'red')
        b3.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "X" WON... !!!!!')
        disable_all_buttons()

    elif b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X':
        b4.config(bg = 'red')
        b5.config(bg = 'red')
        b6.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "X" WON... !!!!!')
        disable_all_buttons()

    elif b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X':
        b7.config(bg = 'red')
        b8.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "X" WON... !!!!!')
        disable_all_buttons()    

    elif b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg = 'red')
        b5.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "X" WON... !!!!!')
        disable_all_buttons() 

    elif b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X':
        b3.config(bg = 'red')
        b5.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "X" WON... !!!!!')
        disable_all_buttons()  
#check for O wins
    elif b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
        b1.config(bg = 'red')
        b2.config(bg = 'red')
        b3.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "O" WON... !!!!!')
        disable_all_buttons()                 


    elif b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O':
        b4.config(bg = 'red')
        b5.config(bg = 'red')
        b6.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "O" WON... !!!!!')
        disable_all_buttons()     

    elif b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O':
        b7.config(bg = 'red')
        b8.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "O" WON... !!!!!')
        disable_all_buttons() 

    elif b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O':
        b1.config(bg = 'red')
        b5.config(bg = 'red')
        b9.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "O" WON... !!!!!')
        disable_all_buttons()  

    elif b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O':
        b3.config(bg = 'red')
        b5.config(bg = 'red')
        b7.config(bg = 'red')
        winner = True
        messagebox.showinfo("tictactoe",' CONGRACTULATIONS "O" WON... !!!!!')
        disable_all_buttons() 

# check if its a tie
    if count == 9 and winner == False:
        messagebox.showinfo("tictactoe",'Hey Its A Tie !!!!!')
        disable_all_buttons() 
             


# button clicked function
def b_click(b):
    global clicked, count

    if b['text'] == " "  and clicked == True:
        b["text"] = "X"
        clicked =False
        count +=1
        checkifwon()
    elif b['text'] == " "  and clicked == False:
         b["text"] = "O"
         clicked =True
         count +=1
         checkifwon()
    else:
        messagebox.showerror("tic tac toe","hey this box is already taken")
def reset():
    global clicked,count 
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    clicked = False
    count = 0

    b1 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b1))
    b2 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b2))
    b3 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b3))

    b4 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b4))
    b5 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b5))
    b6 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b6))

    b7 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b7))
    b8 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b8))
    b9 = Button(root, text=' ', font=('helvetica', 20), height=3, width=6, bg='systemButtonFace', command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu = my_menu)

options = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options" , menu = options)
options.add_command(label="Reset Game" , command = reset)

reset()
# Run the main loop
root.mainloop()
