""" Calculator.py by Kevin Bravo
    This is my final assignment which is a graphing calculator
"""

#first we have to import the libraries for our graphing capabilities

import matplotlib.pyplot as plt
import numpy as np

#next we define our main function which will allow the user to navigate through
#our program

def main():
    while True:
#this line gets the response from our menu which asks the user what they want to
#do
        response = menu()
        if response == 1:
            print("enter an equation in standard form")
            _equation = raw_input("y=")
            equation = _equation.replace("^", "**")
#we get their equation and pass it to another function which will graph it
            coordinates(equation, _equation)
        elif response == 2:
            print("How many points of (x,y) would you like to enter?")
            number = input()
            x = []
            y = []
#I created a for loop to be able to get multiple plot points from the user and
#then I append their values to the empty arrays
            for i in range(int(number)):
                print("enter a value for x")
                xvalue = input()
                x.append(float(xvalue))
                print("enter a value for y")
                yvalue = input()
                y.append(float(yvalue))
#next we pass our arrays to the function points in order to graph them
            points(x, y)
        elif response == 0:
            print("Goodbye")
            break
        else:
            print("please enter '1' '2' or '0'")

def menu():
    print("Graphing Calculator")
    print("0) Quit")
    print("1) Enter an equation")
    print("2) Plot points")
    print("Please select an option")
    response = input()
    return response

def coordinates(equation, _equation):
#I stumbled across the lambda function and did more research on it to use it as
#a solver for the equations
    if equation == "sinx":
        equation = "np.sin(x)"
    elif equation == "cosx":
        equation = "np.cos(x)"
        
    f = lambda x: eval(equation)
#then I used numpy to create x values to plug into the equation
    x = np.linspace(-10, 10, 101)
#we then evaluate those numbers and get an array of y values
    y = f(x)
#matplotlib then plots the arrays and displays them with the show command
    plt.plot(x, y, label = "f(x)= " + _equation)
    plt.legend(loc = 2)
    plt.grid()
    plt.show()

def points(x,y):
#our points function will only need matplotlib in order to display the points
    plt.plot(x,y, 'b-o')
    plt.grid()
    plt.show()
        
if __name__ == "__main__":
    main()
