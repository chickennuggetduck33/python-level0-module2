import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    q = simpledialog.askstring(None, prompt="what would you like to know?")
    # Make a variable and initialize it to a random number between 0 and 3
    number = random.randint(0, 3)
    # If the random number is 0
    if number == 0:
        messagebox.showinfo(message="yes")
        # tell the user "Yes"
    elif number == 1:
        messagebox.showinfo(message="no")
    elif number == 2:
        messagebox.showinfo(message="maybe ask google")
    elif number == 3:
        messagebox.showinfo(message="don't ask me")
    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
