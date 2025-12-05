import tkinter as tk
import collision

root = tk.Tk()
root.attributes("-fullscreen", True)
screenw = root.winfo_screenwidth()
screenh = root.winfo_screenheight()

root.title("First Tkinter project")
root.configure(background="white")
root.geometry(f"{screenw}x{screenh}")

screens = tk.Frame(root)
screens.pack(fill="both", expand=True)

HomeScreen = tk.Frame(screens)
HomeScreen.place(relwidth=1, relheight=1)

SecondScreen = tk.Frame(screens)
SecondScreen.place(relwidth=1,relheight=1)

def order(widgetsorder, settings):
    for index, widget in enumerate(widgetsorder):
        widget.pack(**settings[index])

# Screen 1
testing = tk.Label(HomeScreen, text="\"testing this\"")
def changetext():
    testing.config(text="it worked!")
def changescreen(screen):
    screen.tkraise()
btn1 = tk.Button(HomeScreen,
                text="click to change text",
                command=changetext)
btn2 = tk.Button(HomeScreen,
                 text="click to change screen",
                 command=lambda: changescreen(SecondScreen))
order([btn1,testing,btn2], 
             [{"padx": 5, "pady": 5},
              {},
              {"padx": 5, "pady": 5}])
# Screen 2
testing2 = tk.Label(SecondScreen, text="woah, second screen")

player = tk.Label(SecondScreen, text="🙂", font="50")
player.place(x=200, y=200)

collision.set_player(player, root)
# --- Track which keys are pressed ---
keys_pressed = set()

def key_press(event):
    keys_pressed.add(event.keysym.lower())

def key_release(event):
    keys_pressed.discard(event.keysym.lower())

def move():
    x, y = player.winfo_x(), player.winfo_y()
    step = 5
    if "shift_l" in keys_pressed or "shift_r" in keys_pressed:
        step = 10

    if "w" in keys_pressed and y-step >= 0:
        y -= step
    if "s" in keys_pressed and y+step <= (SecondScreen.winfo_height() - (int(player.cget("font"))/2)):
        y += step
    if "a" in keys_pressed and x-step >= 0:
        x -= step
    if "d" in keys_pressed and x+step <= (SecondScreen.winfo_width() - (int(player.cget("font"))/2)):
        x += step

    player.place(x=x, y=y)
    root.after(20, move)  # repeat every 20 ms

# Bind key events
SecondScreen.bind_all("<KeyPress>", key_press)
SecondScreen.bind_all("<KeyRelease>", key_release)

# Start the movement loop
move()

order([testing2],
      [{}])

HomeScreen.tkraise()
root.bind("<Escape>", lambda event: root.destroy())
root.mainloop()