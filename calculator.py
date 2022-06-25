# 1
def myfunc():
    print('Hello World')

# 2
def myfunc(name):
    #return 'Hello {}'.format(name)
    print('Hello {}'.format(name))

# 3
def myfunc(x):
    if x == True:
        # print('Hello')
        return 'Hello'
    elif x == False:
        # print('Goodbye')
        return 'Goodbye'

# 4
def myfunc(x,y,z):
    if z:
        # print(x)
        return x
    else:
        # print(y)
        return y

# 5
def myfunc(a,b):
    print(a+b)
    # return a+b

# 6
def is_even(n):
    if n%2 == 0:
        return True
        # print(True)  **tested to make sure it DOESN'T work
    else:
        return False

















































































from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
# 'bt_equal':This method calculates the expression 
# present in input field
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""

expression = ""

# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()
# Let us creating a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

#Let us create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
#Let us creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(win, width=312, height=272.5, bg="grey")

btns_frame.pack()
# first row
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
# second row
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
# third row
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
# fourth row
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1) 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

win.mainloop()
def check_even(random_list):
    awway = []
    for element in random_list:
        if element%2==0:
            awway.append(element)
        else:
            pass
    return awway
a = check_even([1,2,3,4,5,67,8928,7,12,31,231,23,66,3,63,26])
print(a)


'''ages = [('naruto', 32), ('luffy', 19), ('Eren', 16), ('jojo', 21)]
def oldest(ages):
    max_age=0
    individual=''
    for name,age in ages:
        if age> max_age:
            max_age=age
            individual=name
        else:
            pass
    return max_age,individual
print(oldest(ages))'''




ages = [('naruto', 32), ('luffy', 19), ('Eren', 15), ('Gintoki', 29)]
def oldest(ages):
    max_age=0
    individual=''
    for name,age in ages:
        if age> max_age:
            max_age=age
            individual=name
        else:
            pass
    return individual, max_age
print(oldest(ages))
name,age=oldest(ages)
print(name)
print(age)




def check_even(numbers):
    return [num for num in numbers if num % 2 == 0]



ages = [('naruto', 32), ('luffy', 19), ('Eren', 15), ('Gintoki', 29)]
oldest = sorted(ages, key=lambda v: v[1], reverse=True)[0]


ages = [('naruto', 32), ('luffy', 19), ('Eren', 15), ('Gintoki', 29)]
oldest = sorted(ages, reverse=True)[0]
print(oldest)


from numpy import integer

count = 0
while (count < 3):
    print("Hello Geek")
    count = count + 1





# Question 3
nums = [2, 5, 12, 1, 5, 8, 13, 12, 4, 17, 99]
for i in nums:
    if i<int(input("enter a number: ")):
        print(i)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Please provide a number: "))
print([y for y in a if y < number])

# question 2
Number=input("Enter a number: ")
if Number == int:
    print(str(Number)+" is an integer number")
elif Number == float:
    print(str(Number)+ "is a float number")
elif Number == complex:
    print(str(Number)+" is a complex number")
else:
    print("input coundn't be indentified,\n please enter an approperate value")


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Please provide a number: "))
print([y for y in a if y < number])

from numpy import integer


Number=input("Enter a number: ")
if Number == (int==True):
    print(str(Number)+" is an integer number")
elif Number == (float==True):
    print(str(Number)+ "is a float number")
elif Number == (complex==True):
    print(str(Number)+" is a complex number")
else:
    print("input coundn't be indentified,\n please enter an approperate value")
