import tkinter as tk
from tkinter import Label, BooleanVar, Checkbutton, messagebox

walls = []
obstacles = []


# checks the wall input boxes for any input other than int or float.
def exception_check_wall():
    try:
        testw = float(wallWidth.get("1.0", 'end-1c'))
        testh = float(wallHeight.get("1.0", 'end-1c'))
    except ValueError:
        messagebox.showerror("Input error", "Please ensure all inputs are numbers.")
    else:
        add_wall()


# takes the height and width from the input boxes, calculates the total area, and appends to walls[].
def add_wall(total_area=0, total_obst_area=0):
    for widget in frameC.winfo_children():  # destroys the current output frame contents.
        widget.destroy()
    for widget in frameB.winfo_children():
        widget.destroy()
    width = float(wallWidth.get("1.0", 'end-1c'))
    height = float(wallHeight.get("1.0", 'end-1c'))
    for ob in obstacles:  # calculates the total area of any obstacles.
        total_obst_area += ob[1]
    area = (round(width * height, 2)) - total_obst_area  # /(width * height) - obstacle area/ rounded to 2 dec.pla.
    walls.append([len(walls)+1, area])
    for wall in walls:
        label_walls = tk.Label(frameC, text=f"Wall {wall[0]}:   {wall[1]}m²")
        label_walls.pack()
    for wall in walls:
        total_area += wall[1]
    label_area = tk.Label(frameB, text=f"Total area:   {total_area}m²")
    label_area.pack()
    for widget in frameObstTotal.winfo_children():
        widget.destroy()
    for widget in frameObstList.winfo_children():
        widget.destroy()
    obstacles.clear()
    frameObstList.config(width=81, height=21)
    frameObstTotal.config(width=81, height=21)
    paint_needed(total_area)


def obst():
    if is_obst.get():  # TRUE
        obstWidthLabel.grid(row=3, column=0, padx=5, pady=10)
        obstWidth.grid(row=3, column=1, padx=10, pady=10)
        obstMeterLabel.grid(row=3, column=2, pady=10)
        multiplyLabel2.grid(row=3, column=3, padx=1, pady=10)
        obstHeightLabel.grid(row=3, column=4, pady=10)
        obstHeight.grid(row=3, column=5, padx=10, pady=10)
        obstMeterLabel2.grid(row=3, column=6, pady=10)
        addObstButton.grid(row=3, column=7, padx=15)
        frameObstTotal.grid(row=4, column=1, columnspan=3, padx=10, pady=10)
        frameObstList.grid(row=4, column=5, columnspan=3, padx=10, pady=10)
    else:  # FALSE
        obstWidthLabel.grid_forget()
        obstWidth.grid_forget()
        obstMeterLabel.grid_forget()
        multiplyLabel2.grid_forget()
        obstHeightLabel.grid_forget()
        obstHeight.grid_forget()
        obstMeterLabel2.grid_forget()
        addObstButton.grid_forget()
        frameObstTotal.grid_forget()
        frameObstList.grid_forget()


# checks the obstacle input boxes for any input other than int or float.
def exception_check_obst():
    try:
        testw = float(obstWidth.get("1.0", 'end-1c'))
        testh = float(obstHeight.get("1.0", 'end-1c'))
    except ValueError:
        messagebox.showerror("Input error", "Please ensure all inputs are numbers.")
    else:
        add_obst()


def add_obst(total_area=0):
    for widget in frameObstTotal.winfo_children():
        widget.destroy()
    for widget in frameObstList.winfo_children():
        widget.destroy()
    width = float(obstWidth.get("1.0", 'end-1c'))
    height = float(obstHeight.get("1.0", 'end-1c'))
    area = round(width * height, 2)
    obstacles.append([len(obstacles)+1, area])
    for ob in obstacles:
        label_oblist = tk.Label(frameObstList, text=f"Obstacle {ob[0]}:   {ob[1]}m²")
        label_oblist.pack()
    for ob in obstacles:
        total_area += ob[1]
    label_area = tk.Label(frameObstTotal, text=f"Total obstacle area:   {total_area}m²")
    label_area.pack()


def paint_needed(total_area):
    for widget in frameD.winfo_children():  # destroys the current output frame contents.
        widget.destroy()
    layers_of_paint = int(coats_of_paint.get())
    total_paint = (total_area * 0.1) * layers_of_paint
    if layers_of_paint > 1:
        plural = "coats"
    else:
        plural = "coat"
    label_paint = tk.Label(frameD, text=f"Total paint needed for {layers_of_paint} {plural}:   {total_paint:0.2f} litres\nTotal accounting for 10% wastage:   {total_paint*1.1:0.2f} litres")
    label_paint.pack()


root = tk.Tk()
root.title("Paint Calculator")
root.iconbitmap("C:/Users/Admin/Documents/Programming/Python/PaintCalculator/paint-bucket.ico")
root.configure(background="#8ca5f0")

frameA = tk.Frame(root, width=200, height=50, bg="pink")
frameA.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

wallWidthLabel = Label(frameA, background="pink", text="Width:")
wallWidthLabel.grid(row=0, column=0, padx=5, pady=10)

wallWidth = tk.Text(frameA, width=20, height=1)
wallWidth.grid(row=0, column=1, pady=10)

widthMeterLabel = Label(frameA, background="pink", text="m", justify="left")
widthMeterLabel.grid(row=0, column=2, pady=10)

multiplyLabel = Label(frameA, background="pink", text="×", justify="right")
multiplyLabel.grid(row=0, column=3, padx=1, pady=10)

wallHeightLabel = Label(frameA, background="pink", text="Height:", justify="right")
wallHeightLabel.grid(row=0, column=4, pady=10)

wallHeight = tk.Text(frameA, width=20, height=1)
wallHeight.grid(row=0, column=5, pady=10)

heightMeterLabel = Label(frameA, background="pink", text="m", justify="left")
heightMeterLabel.grid(row=0, column=6, pady=10)

addWallButton = tk.Button(frameA, text="Add wall", height=1, command=exception_check_wall)
addWallButton.grid(row=0, column=7, padx=15)

coats_label = Label(frameA, background="pink", text="How many coats?:   ", justify="left")
coats_label.grid(row=1, column=0, columnspan=2, pady=10)

coats_of_paint = tk.Spinbox(frameA, from_=1, to=99, width=3)
coats_of_paint.grid(row=1, column=1, columnspan=4, padx=5, pady=10)

obstructLabel = Label(frameA, background="pink", text="Are there any additional areas that don't need painting? (Doors, windows, etc.):")
obstructLabel.grid(row=2, column=0, columnspan=6, padx=5, pady=10)

is_obst = BooleanVar()
obstructCheck = Checkbutton(frameA, background="pink", activebackground="pink", command=obst, variable=is_obst, onvalue=True, offvalue=False)
obstructCheck.grid(row=2, column=6, columnspan=1, padx=5, pady=10)

obstWidthLabel = Label(frameA, background="pink", text="Width:")

obstWidth = tk.Text(frameA, width=20, height=1)

obstMeterLabel = Label(frameA, background="pink", text="m", justify="left")

multiplyLabel2 = Label(frameA, background="pink", text="×", justify="right")

obstHeightLabel = Label(frameA, background="pink", text="Height:", justify="right")

obstHeight = tk.Text(frameA, width=20, height=1)

obstMeterLabel2 = Label(frameA, background="pink", text="m", justify="left")

addObstButton = tk.Button(frameA, text="Add obstacle", height=1, command=exception_check_obst)

frameObstTotal = tk.Frame(frameA, width=81, height=21, bg="white")

frameObstList = tk.Frame(frameA, width=81, height=21, bg="white")


frameB = tk.Frame(root, width=81, height=21, bg="white")
frameB.grid(row=1, column=0, padx=10, pady=10)

frameC = tk.Frame(root, width=81, height=21, bg="white")
frameC.grid(row=1, column=1, rowspan=5, padx=10, pady=10)

frameD = tk.Frame(root, width=81, height=21, bg="white")
frameD.grid(row=2, column=0, padx=10, pady=10)

#frameE = tk.Frame(root, width=81, height=21, bg="white")
#frameE.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
