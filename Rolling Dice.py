import random            # random value to execute
from tkinter import *    # * is the import into tkinter library

root = Tk()              # Tk means Tkinter Window make
root.geometry("600x300") # Define Dimension Length and Breadth . In ("600x300") Multipiy symbol use x char    

text_1= Label(root,text='',font =("arial",250))   # Difine label inside dimension,text and font-name & size 

def roll_the_dice():      #define function of command
    num_code=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2684','\u2685']  # num of dice 1,2,3,4,5,6 as a symbol
    text_1.config(text=f'{random.choice(num_code)}{random.choice(num_code)}')   # num of dice is execute
    text_1.pack()

button_1 =Button(root,text="Roll the dice",command=roll_the_dice) # define button use text and command
button_1.place(x=250,y=0)          # Button Position

root.mainloop()  # close the program
