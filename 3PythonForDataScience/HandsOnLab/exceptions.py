
def example_1(a=1):
    try:
        b = int(input("Please enter a number to divide a: "))
        a = a/b
        print("Success a =", a)
    except ZeroDivisionError:
        print("The number you provided cant divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")


def example_2(a=1):
    try:
        b = int(input("Please enter a number to divide a: "))
        a = a / b
    except ZeroDivisionError:
        print("The number you provided cant divide 1 because it is 0")
    except ValueError:
        print("You did not provide a number")
    except:
        print("Something went wrong")
    else:
        print("success a =", a)
    finally:
        print("Processing Complete")


example_2()
