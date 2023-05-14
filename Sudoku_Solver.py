import numpy as np
from tkinter import *
from tkinter import messagebox
import keyboard


#------------------------------------------

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

defaultgrid = [[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0]]

def windows_configuration():
        Sudoku.geometry("600x700")
        Sudoku.title("SUDOKU SOLVER")
        Sudoku.resizable(False, False)
        icon = PhotoImage(file="ico.png")
        Sudoku.iconphoto(True, icon)
        Sudoku.config(bg="white")

def headline():
    headline = Label(Sudoku, 
                text="SUDOKU SOLVER", 
                font=("Arial", 10), 
                fg="BLACK",
                bg="white")                     # Informacija na dnu stranice ko je napravio igricu
    return headline

def create_button ():
        s_b = Button(Sudoku, 
                text= "solve", 
                font=("Arial", 15), 
                fg="black",  
                relief="groove", 
                bd=5,  
                compound="center",
                command= clicked_solve)
        return (s_b) 

def clicked_solve():
    global grid
    global defaultgrid
    for row in range(0,9):
        for column in range(0,9):
            field=("field{}{}".format(column, row))
            getnumber=globals()[field].get()
            grid[column][row]=getnumber
            if grid[column][row] == "":
                grid[column][row] = 0
                getnumber = 0
            if getnumber not in ['0','1','2','3','4','5','6','7','8','9',0,1,2,3,4,5,6,7,8,9]:
                messagebox.showerror("ERROR", "Game SUDOKU use only numbers! \n try again")
            grid[column][row]=int(grid[column][row])

    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] != 0:
                number = grid[row][column]
                by_the_rule(row, column, number)
    
    if grid != defaultgrid:
        solve()
        messagebox.showinfo("info", "No more possible solution!")
    else: 
        return False

def by_the_rule(row, column, number):
    global grid
    global defaultgrid
    count1=0
    count2=0
    count3=0
    if grid == defaultgrid:
        messagebox.showerror("ERROR", "There is no numbers in fields, is NOT by the rules of game SUDOKU \n try again")
        update_field()
        delete_function(by_the_rule())
        return False

    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            count1 += 1
            if count1 == 2:
                messagebox.showerror("ERROR", "Numbers in fields is NOT by the rules of game SUDOKU \n try again")
                update_field()
                delete_function(by_the_rule())
                return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            count2 += 1
            if count2 == 2:
                messagebox.showerror("ERROR", "Numbers in fields is NOT by the rules of game SUDOKU \n try again")
                update_field()
                delete_function(by_the_rule())
                return False
    
    #Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                count3 += 1
                if count3 == 2:
                    messagebox.showerror("ERROR", "Numbers in fields is NOT by the rules of game SUDOKU \n try again")
                    update_field()
                    delete_function(by_the_rule())
                    return False

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = int(number)
                        solve()
                        grid[row][column] = 0

                return
      
    update_field()
    msg_box = messagebox.askquestion("info", "Maby there is more possible solutions \n Do you want proceed?", icon="warning")
    if msg_box == "no":
        print ("no more")
        delete_function(solve())
        

def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def update_field():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            field=("field{}{}".format(column, row))
            globals()[field].delete(0, END)
            if grid[column][row] == 0:
                grid[column][row] = ""
            globals()[field].insert(0, grid[column][row])
    return False

#------------------------------------------

Sudoku = Tk()

canvas = Canvas(Sudoku, width=600, height=600, bg="gray")

slika = PhotoImage(file='sudoku_table.png')
sudoku_table = canvas.create_image(0,0,image=slika,anchor=NW)

windows_configuration()

#------------------------------------------

headline().pack(side="top", pady=10)
canvas.pack()
create_button().pack(side="bottom", pady=10)

for row in range(0,9):
    for column in range(0,9):
        number = int(grid[column][row])
        if number < 1 or number > 9:
            number = ""
        field=("field{}{}".format(column, row))
        globals()[field] = Entry(canvas, font=("Arial", 30), justify = CENTER, borderwidth=0, relief="flat")
        globals()[field] .insert(0, number)
        x= 66 * row + 35
        y= 66 * column + 35
        canvas.create_window(x, y, height=50, width=25, window = globals()[field] )

Sudoku.mainloop()

#------------------------------------------
