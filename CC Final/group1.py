#numpy is a python library that allows us to perform a much more robust set of functions and methods concerning numbers
import numpy as np

#matplotlib, and specifically pyplot, are libraries that we use to visualize data
import matplotlib.pyplot as plt

def main():

    a1, b1, c1, eq1 = generate_equation()
    a2, b2, c2, eq2 = generate_equation()
    x_correct = generate_x(a1, a2, b1, b2, c1, c2)
    y_correct = generate_y(a1, b1, c1, x_correct)

    x = np.linspace(-10, 10, 100)
    y1 = (c1 - a1 * x) / b1
    y2 = (c2 - a2 * x) / b2

    plt.plot(x, y1, label=eq1)
    plt.plot(x, y2, label=eq2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('System of Linear Equations')
    plt.legend()
    plt.grid(True)
    plt.show()

    while True:
        user_input = input("What is the solution to the system of linear equations?\n(Enter a for a point, b for no solution, or c for infinite solutions): ")
        if user_input.lower() == 'a':
            user_answer = input("Enter the values of x and y separated by spaces (e.g., 'x y'): ").split()
            try:
                x_user = float(user_answer[0])
                y_user = float(user_answer[1])
                if x_user == x_correct and y_user == y_correct:
                    print(f"Correct! The solution is ({x_correct}, {y_correct})")
                    break
                else:
                    print("Incorrect. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
        elif user_input.lower() == 'b':
            print("Incorrect. There is a solution.")
        elif user_input.lower() == 'c':
            print("Incorrect. There is a unique solution.")
        else:
            print("Invalid input. Try again.")


def generate_equation():
    a, b, c = np.random.randint(-10, 10, size=3)
    return [a, b, c, f"{a}x + {b}y = {c}"]


def generate_x(a1, a2, b1, b2, c1, c2):
    return (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)


def generate_y(a1, b1, c1, x_correct):
    return (c1 - a1 * x_correct) / b1


if __name__ == "__main__":
    main()