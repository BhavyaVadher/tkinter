import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# lebel
my_lebel = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_lebel.pack()

window.mainloop()