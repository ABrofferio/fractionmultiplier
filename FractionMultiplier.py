#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import random
from fractions import Fraction



class Multiplication:
    def __init__(self, master):
        master.title('Multiplication Madness')
        master.resizable(False, False)

        self.frame1 = ttk.Frame(master, width = 500, height = 300)
        self.frame1.pack()
        heading = ttk.Label(self.frame1, text = "Welcome to Multiplication Madness. Pick your level and practice your multiplication!")
        heading.grid(row = 0, column = 1, columnspan = 2)
        selection = ttk.Label(self.frame1, text = "Take Your Pick")
        selection.grid(row = 1, column = 1, columnspan = 2)

        #choosing a level
        self.listbox = Listbox(self.frame1, height = 3)
        self.listbox.grid(row = 2, column = 1, columnspan = 2)
        self.listbox.insert(0,"Easy")
        self.listbox.insert(1,"Medium")
        self.listbox.insert(2,"Hard")
        start = ttk.Button(self.frame1, text ="Let's Get Started!", command = self.start)
        start.grid(row = 3, column = 1, columnspan = 2)
        
        #the interactive math portion
        self.frame2 = ttk.Frame(master, width = 600, height = 300)
        self.frame2.pack()
        self.variable1 = ttk.Entry(self.frame2, width = 10)
        self.variable1.grid(row = 0, column = 1)
        multiply = ttk.Label(self.frame2, text = "X")
        multiply.grid(row = 0, column = 2)
        self.variable2 = ttk.Entry(self.frame2, width = 10)
        self.variable2.grid(row = 0, column = 3)
        equal = ttk.Label(self.frame2, text = "=")
        equal.grid(row = 0, column = 4)
        self.answer = ttk.Entry(self.frame2, width = 10)
        self.answer.grid(row = 0, column = 5)
        
        #hidden entry boxes for hint button
        self.numer = ttk.Label(self.frame2, text = "Multiply the numerators!")
        self.numer.grid(row = 1, column = 0)
        self.numvar1 = ttk.Entry(self.frame2, width = 10)
        self.numvar1.grid(row = 1, column = 1)
        self.multiply2 = ttk.Label(self.frame2, text = "X")
        self.multiply2.grid(row = 1, column = 2)
        self.numvar2 = ttk.Entry(self.frame2, width = 10)
        self.numvar2.grid(row = 1, column = 3)
        self.equal2 = ttk.Label(self.frame2, text = "=")
        self.equal2.grid(row = 1, column = 4)
        self.answer2 = ttk.Entry(self.frame2, width = 10)
        self.answer2.grid(row = 1, column = 5)

        self.denom = ttk.Label(self.frame2, text = "Multiply the denominators!")
        self.denom.grid(row = 2, column = 0)
        self.denvar1 = ttk.Entry(self.frame2, width = 10)
        self.denvar1.grid(row = 2, column = 1)
        self.multiply3 = ttk.Label(self.frame2, text = "X")
        self.multiply3.grid(row = 2, column = 2)
        self.denvar2 = ttk.Entry(self.frame2, width = 10)
        self.denvar2.grid(row = 2, column = 3)
        self.equal3 = ttk.Label(self.frame2, text = "=")
        self.equal3.grid(row = 2, column = 4)
        self.answer3 = ttk.Entry(self.frame2, width = 10)
        self.answer3.grid(row = 2, column = 5)
        
        self.hide()

        #buttons 
        hint = ttk.Button(self.frame2, text ="hint", command = self.hint)
        hint.grid(row = 3, column = 1)
        submit = ttk.Button(self.frame2, text ="submit", command = self.submit)
        submit.grid(row = 3, column = 2)
        Next = ttk.Button(self.frame2, text ="next", command = self.Next)
        Next.grid(row = 3, column = 3)
        

    def start(self):
        self.variable1.delete(0,END)
        self.variable2.delete(0,END)
        if self.listbox.get(self.listbox.curselection()) == "Easy":
            numer8tor = (random.randrange(1,9))
            denomin8tor = (random.randrange(2,10))
            self.fract = Fraction(numerator = numer8tor, denominator=denomin8tor)
            self.variable1.insert(0, self.fract)
            whole_numb = (random.randrange(1,10))
            self.variable2.insert(0, whole_numb)
            self.numvar1.insert(0,numer8tor)
            self.numvar2.insert(0,self.variable2.get())
            self.denvar1.insert(0,denomin8tor)
            self.denvar2.insert(0,1)
            self.Answer2 = (int(self.numvar1.get())*int(self.numvar2.get()))
            self.answer2.insert(0,self.Answer2)
            self.Answer3 = (int(self.denvar1.get())*int(self.denvar2.get()))
            self.answer3.insert(0,self.Answer3)

            
        elif self.listbox.get(self.listbox.curselection()) == "Medium":
            numer8tor = (random.randrange(1,10))
            denomin8tor = (random.randrange(2,100))
            self.fract = Fraction(numerator = numer8tor, denominator=denomin8tor)
            self.variable1.insert(0, self.fract)
            whole_numb = (random.randrange(1,10))
            self.variable2.delete(0,END)
            self.variable2.insert(0, whole_numb)
            self.numvar1.insert(0,numer8tor)
            self.numvar2.insert(0,self.variable2.get())
            self.denvar1.insert(0,denomin8tor)
            self.denvar2.insert(0,1)
            self.Answer2 = (int(self.numvar1.get())*int(self.numvar2.get()))
            self.answer2.insert(0,self.Answer2)
            self.Answer3 = (int(self.denvar1.get())*int(self.denvar2.get()))
            self.answer3.insert(0,self.Answer3)

        elif self.listbox.get(self.listbox.curselection()) == "Hard":
            numer8tor = (random.randrange(1,100))
            denomin8tor = (random.randrange(2,100))
            self.fract = Fraction(numerator = numer8tor, denominator=denomin8tor)
            self.variable1.insert(0, self.fract)
            whole_numb = (random.randrange(1,100))
            self.variable2.delete(0,END)
            self.variable2.insert(0, whole_numb)
            self.numvar1.insert(0,numer8tor)
            self.numvar2.insert(0,self.variable2.get())
            self.denvar1.insert(0,denomin8tor)
            self.denvar2.insert(0,1)
            self.Answer2 = (int(self.numvar1.get())*int(self.numvar2.get()))
            self.answer2.insert(0,self.Answer2)
            self.Answer3 = (int(self.denvar1.get())*int(self.denvar2.get()))
            self.answer3.insert(0,self.Answer3)

    def hint(self):
        self.numer.grid()
        self.numvar1.grid()
        self.multiply2.grid()
        self.numvar2.grid()
        self.equal2.grid()
        self.answer2.grid()
        
        self.denom.grid()
        self.denvar1.grid()
        self.multiply3.grid()
        self.denvar2.grid()
        self.equal3.grid()
        self.answer3.grid()

    def submit(self):
        #correct answer
        var1 = (self.variable1.get())
        var1_array = var1.split("/")
        var1_array.append("1")
        var1_1 = (float(var1_array[0]))
        var1_2 = (float(var1_array[1]))
        var2 = (self.variable2.get())
        var2_array = var2.split("/")
        var2_array.append("1")
        var2_1 = (float(var2_array[0]))
        var2_2 = (float(var2_array[1]))
        self.ANSWER = (var1_1*var2_1)/(var1_2*var2_2)                   
       
        #user answer
        user_answer = (self.answer.get())
        user_array = user_answer.split("/")
        user_array.append('1')
        user_1 = float(user_array[0])
        user_2 = float(user_array[1])
        given_answer = user_1/user_2

        if str(given_answer) == str(self.ANSWER):
            self.congrats = ttk.Label(self.frame2, text = "Congrats!")
            self.congrats.grid(row = 4, column = 2)
            self.variable1.delete(0,END)
            self.variable2.delete(0,END)
            self.answer.delete(0,END)
        else:
            self.try_again = ttk.Label(self.frame2, text = "Try Again!")
            self.try_again.grid(row = 4, column = 2)
            self.answer.delete(0,END)

        self.hide()
    def Next(self):
        self.numvar1.delete(0,END)
        self.numvar2.delete(0,END)
        self.denvar1.delete(0,END)
        self.denvar2.delete(0,END)
        self.answer2.delete(0,END)
        self.answer3.delete(0,END)

        self.start()
        self.hide()

    def hide(self):
        
        self.numer.grid_remove()
        self.numvar1.grid_remove()
        self.multiply2.grid_remove()
        self.numvar2.grid_remove()
        self.equal2.grid_remove()
        self.answer2.grid_remove()

        self.denom.grid_remove()
        self.denvar1.grid_remove()
        self.multiply3.grid_remove()
        self.denvar2.grid_remove()
        self.equal3.grid_remove()
        self.answer3.grid_remove()

def main():
    root = Tk()
    app = Multiplication(root)
    root.mainloop

if __name__ == "__main__" : main()
