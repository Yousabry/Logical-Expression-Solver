'''
Solves expressions using truth tables
Uses tkniter to input variables and expression
'''
from tkinter import *
root = Tk()

def possibilityset(expression, list_of_var):
    #Returns True if there is a mistake in the expression
    possibilities = ['T','F']
    solutions = []
    for value1 in possibilities:
        for value2 in possibilities:
            for value3 in possibilities:
                #These two give us the 4 possible comb
                newexpression = expression.replace(list_of_var[0],value1)
                newexpression = newexpression.replace(list_of_var[1],value2)
                newexpression = newexpression.replace(list_of_var[2],value3)
                solutions.append(solver(newexpression))
    tablemaker(solutions,list_of_var)

def solver(newexpression):
    #Returns the solutions (T or F) for the expression
    while len(newexpression) != 1:
        #Spaces
        newexpression = newexpression.replace(' ','')
        #Negation
        newexpression = newexpression.replace('¬T','F')
        newexpression = newexpression.replace('¬F','T')

        #Disjunctions
        newexpression = newexpression.replace('T∨T','T')
        newexpression = newexpression.replace('T∨F','T')
        newexpression = newexpression.replace('F∨T','T')
        newexpression = newexpression.replace('F∨F','F')

        #Conjuctions
        newexpression = newexpression.replace('T∧T','T')
        newexpression = newexpression.replace('T∧F','F')
        newexpression = newexpression.replace('F∧T','F')
        newexpression = newexpression.replace('F∧F','F')

        #If and Only If
        newexpression = newexpression.replace('T↔T','T')
        newexpression = newexpression.replace('T↔F','F')
        newexpression = newexpression.replace('F↔T','F')
        newexpression = newexpression.replace('F↔F','T')

        #Implication
        newexpression = newexpression.replace('T→T','T')
        newexpression = newexpression.replace('T→F','F')
        newexpression = newexpression.replace('F→T','T')
        newexpression = newexpression.replace('F→F','T')

        #Parentheses
        newexpression = newexpression.replace('(T)','T')
        newexpression = newexpression.replace('(F)','F')

    return newexpression

def tablemaker(solutions,list_of_var):

    print('{}\t{}\t{}\t\tResult'.format(list_of_var[0],list_of_var[1],list_of_var[2]))
    print('------------------------------------')
    print('T\tT\tT\t\t{}'.format(solutions[0]))
    print('T\tT\tF\t\t{}'.format(solutions[1]))
    print('T\tF\tT\t\t{}'.format(solutions[2]))
    print('T\tF\tF\t\t{}'.format(solutions[3]))
    print('F\tT\tT\t\t{}'.format(solutions[4]))
    print('F\tT\tF\t\t{}'.format(solutions[5]))
    print('F\tF\tT\t\t{}'.format(solutions[6]))
    print('F\tF\tF\t\t{}'.format(solutions[7]))

    root.destroy()

root.geometry('300x300')
def addcharacter(expression,character):
    oldtext = expression.get()
    newtext = oldtext + character
    expression.delete(0,END)
    expression.insert(0,newtext)

def setup(expression,listofvar):
    acexpression = expression.get()
    print(acexpression)
    expression.config(state='disabled')
    possibilityset(acexpression,listofvar)

def expressionSetup():
    global variable1,variable2,variable3,continuebutton,root

    frame2 = Frame(root)
    frame2.pack(side=BOTTOM)

    var1 = variable1.get()
    var2 = variable2.get()
    var3 = variable3.get()
    #Disabling entrys after proceeding
    variable1.config(state='disabled')
    variable2.config(state='disabled')
    variable3.config(state='disabled')
    continuebutton.config(state='disabled')

    labelexp = Label(frame2,text='Enter your expression below:')
    expression = Entry(frame2)
    variableButton1 = Button(frame2,text=var1,command=lambda: addcharacter(expression,var1))
    variableButton2 = Button(frame2,text=var2,command=lambda: addcharacter(expression,var2))
    variableButton3 = Button(frame2,text=var3,command=lambda: addcharacter(expression,var3))
    notButton = Button(frame2,text='¬',command=lambda: addcharacter(expression,'¬'))
    andButton = Button(frame2,text='∧',command=lambda: addcharacter(expression,'∧'))
    orButton = Button(frame2,text='∨',command=lambda: addcharacter(expression,'∨'))
    IMPButton = Button(frame2,text='→',command=lambda: addcharacter(expression,'→'))
    IAOFButton = Button(frame2,text='↔',command=lambda: addcharacter(expression,'↔'))
    openparButton = Button(frame2,text='(',command=lambda: addcharacter(expression,'('))
    closeparButton = Button(frame2,text=')',command=lambda: addcharacter(expression,')'))
    solveButton = Button(frame2,text='Solve',command=lambda: setup(expression,[var1,var2,var3]))

    labelexp.grid(row=0,column=0,columnspan=10)
    expression.grid(row=1,column=0,columnspan=10)
    variableButton1.grid(row=2,column=0)
    variableButton2.grid(row=2,column=1)
    variableButton3.grid(row=2,column=2)
    notButton.grid(row=2,column=3)
    andButton.grid(row=2,column=4)
    orButton.grid(row=2,column=5)
    IMPButton.grid(row=2,column=6)
    IAOFButton.grid(row=2,column=7)
    openparButton.grid(row=2,column=8)
    closeparButton.grid(row=2,column=9)
    solveButton.grid(row=3,column=0,columnspan=10)

frame1 = Frame(root)
root.title('Expression Solver')
frame1.pack()

label1 = Label(frame1,text='Variable 1')
variable1 = Entry(frame1,width=1)
label1.grid(row=0,column=0)
variable1.grid(row=0,column=1)

label2 = Label(frame1,text='Variable 2')
label2.grid(row=1,column=0)
variable2 = Entry(frame1,width=1)
variable2.grid(row=1,column=1)

label3 = Label(frame1,text='Variable 3')
variable3 = Entry(frame1,width=1)
label3.grid(row=2,column=0)
variable3.grid(row=2,column=1)

continuebutton = Button(frame1,text='continue',command=expressionSetup)
continuebutton.grid(row=4,columnspan=2)

root.mainloop()
