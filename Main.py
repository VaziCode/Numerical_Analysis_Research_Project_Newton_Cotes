
#Name:Tal vazana, ID:313454472

"""
The function we are going to work with
"""
f = lambda x: 1/(x**3+1)


def midpoint(a, b, n):
    """
    The midpoint method which will calculate the area by the given points a and b
    the chance of the result been accurate is by the size of n.
    This is for open method
    :param a:float, stat point
    :param b:float, end point
    :param n:int, the number of times the range is divided into area calculations
    :return:float, area
    """
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
        tmp = result
        print("N = ",i, ",result",abs(tmp))
    tmp = result
    result *= h
    print("result = {}*{}".format(abs(tmp),h))

    return abs(result)


def trapezoidal(x0, xn, n):
    """
    The trapezoidal method which will calculate the area by the given points x0 and xn
    the chance of the result been accurate is by the size of n.
    This is for closed method
    :param x0:float, stat point
    :param xn:float, end point
    :param n:int, the number of times the range is divided into area calculations
    :return:float, area
    """
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)
        tmp = integration
        print("N = ",i, ",result",abs(tmp))

    # Finding final integration value
    print("result = {}*{}/2".format(abs(integration),h,2))
    integration = abs(integration * h / 2)

    return integration


def main():
    """
    The main menu, here the user will decide which method he would like to use
    :return:None
    """
    sub_interval = 10
    while True:
        print("----------------------------------------")
        print("Hello ! the function is --> f(x) = 1/(x**3+1)\n"
              "Which method do you wish to solve with?\nPress 1 --> Closed Method\n"
              "Press 2 --> Open Method\nPress another key to EXIT\n")
        choice1 = input()
        if choice1 == "1" or choice1 == "2":
            lower_limit = float(input("Enter lower limit of integration: "))
            upper_limit = float(input("Enter upper limit of integration: "))
            print("Would you like to add value to the sub of the intervals?\n")
            print("Press Y/N\n")
            choice2 = input()
            if choice2 == "Y" or choice2 == "y":
                sub_interval = int(input("Enter number of sub intervals: "))
        if choice1 == "1":
            result = trapezoidal(lower_limit, upper_limit, sub_interval)
            print("Integration result by Trapezoidal method is: %0.6f" % (result))
        elif choice1 == "2":
            result = midpoint(lower_limit, upper_limit, sub_interval)
            print("Integration result by midpoint method is: %0.6f" % (result))

        else:
            print("\n----------------------------------------")
            print("Goodbye!")
            print("\n----------------------------------------")
            # stop the loop
            break


main()



