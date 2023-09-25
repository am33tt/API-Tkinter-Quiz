import tkinter as tk

def change_text():
    new_text = "This is a long piece of text that needs to be wrapped within the canvas width. It should automatically wrap to fit."
    canvas.itemconfig(text_item, text=new_text)

root = tk.Tk()
root.title("Wrapped Text on Canvas Example")

canvas = tk.Canvas(root, width=400, height=200, bg='white')
canvas.pack()

initial_text = "This is a short text."
text_item = canvas.create_text(200, 100, text=initial_text, font=("Helvetica", 12), width=300)

button = tk.Button(root, text="Change Text", command=change_text)
button.pack()

root.mainloop()


