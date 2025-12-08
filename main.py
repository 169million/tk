import tkinter as tk
import math
import random
import collision

game_running = True

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
    for i, widget in enumerate(widgetsorder):
        widget.pack(**settings[i])
def whatscreenactive():
    return screens.winfo_children()[-1]
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

player = tk.Label(SecondScreen, text="🙂", font=("Arial", 25))
player.place(x=200, y=200)

enemynumber = 5
enemys = {}
for i in range(enemynumber):
    enemys[i] = tk.Label(SecondScreen, text="😠", font=("Arial", 25))
    erx = random.randint(500,1000)
    ery = random.randint(500,1000)
    enemys[i].place(x=erx,y=ery)

# enemy = tk.Label(SecondScreen, text="😠", font=("Arial", 25))
# enemy.place(x=500,y=500)

font_size = int(player.cget("font").split()[1])

keys_pressed = set()

def key_press(event):
    keys_pressed.add(event.keysym.lower())

def key_release(event):
    keys_pressed.discard(event.keysym.lower())

def move():
    if whatscreenactive() is SecondScreen:
        ex,ey,dx,dy,distance,esx,esy = [],[],[],[],[],[],[]
        x, y = player.winfo_x(), player.winfo_y()

        step = 5
        estep = 6
        
        for i in range(len(enemys)):
            ex.append(enemys[i].winfo_x())
            ey.append(enemys[i].winfo_y())
            dx.append(x - ex[i])
            dy.append(y - ey[i])
            distance.append(math.hypot(dx[i],dy[i]))
            esx.append((dx[i] / distance[i]) * estep)
            esy.append((dy[i] / distance[i]) * estep)
        # dx = x - ex
        # dy = y - ey
        # distance = math.hypot(dx, dy)
        # print(distance)
        # if distance != 0:
        #     ndx = dx / distance
        #     ndy = dy / distance
        # else:
        #     ndx = ndy = 0

        # esx = ndx * estep
        # esy = ndy * estep

        if "shift_l" in keys_pressed or "shift_r" in keys_pressed:
            step = 10
        if "w" in keys_pressed and y-step >= 0:
            y -= step
        if "s" in keys_pressed and y+step <= (SecondScreen.winfo_height() - (font_size/2)):
            y += step
        if "a" in keys_pressed and x-step >= 0:
            x -= step
        if "d" in keys_pressed and x+step <= (SecondScreen.winfo_width() - (font_size/2)):
            x += step
        

        player.place(x=x, y=y)
        for i in range(len(enemys)):
            ex[i] += esx[i]
            ey[i] += esy[i]
            enemys[i].place(x=int(ex[i]),y=int(ey[i]))
            collision.load(root, player, enemys[i])
        # enemy.place(x=int(ex), y=int(ey))
        # collision.load(root, player, enemy)

    root.after(20, move)

SecondScreen.bind_all("<KeyPress>", key_press)
SecondScreen.bind_all("<KeyRelease>", key_release)

root.after(100, move)
order([testing2],
      [{}])

HomeScreen.tkraise()
root.bind("<Escape>", lambda event: root.destroy())
root.mainloop()