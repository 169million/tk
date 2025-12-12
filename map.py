import tkinter as tk
import json
import os

ROWS, COLS = 11,11
root = tk.Tk()
data = []
labels = []

if not os.path.exists("map.json") or os.path.getsize("map.json") == 0:
    with open("map.json", "w") as f:
        json.dump([[False]*COLS for _ in range(ROWS)], f)

def toggle(r, c, lbl):
    global data
    data[r][c] = not data[r][c]
    lbl.config(bg="black" if data[r][c] else "white")
    with open("map.json", "w") as j:
        json.dump(data, j)

def start():
    global data, labels
    for row in labels:
        for lbl in row:
            lbl.destroy()
    labels = []
    with open("map.json", "r") as j:
        data = json.load(j)
    while len(data) < ROWS:
        data.append([False]*COLS)
    for row in data:
        while len(row) < COLS:
            row.append(False)
    for r in range(ROWS):
        row_labels = []
        for c in range(COLS):
            lbl = tk.Label(root, width=10, height=5,bg="black" if data[r][c] else "white", bd=0)
            lbl.grid(row=r, column=c,padx=1,pady=1)
            lbl.bind("<Button-1>", lambda e, r=r, c=c, l=lbl: toggle(r, c, l))
            row_labels.append(lbl)
        labels.append(row_labels)

def clear(event=None):
    global data
    data = [[False]*COLS for _ in range(ROWS)]
    with open("map.json", "w") as f:
        json.dump(data, f)
    start()

start()
root.bind("c", clear)
root.mainloop()
