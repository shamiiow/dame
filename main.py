import tkinter
long = 10
grid = [[0 for j in range(12)]for i in range(12)]
player_turn = 0
old_play = [0, 0]



def dim(event) -> None:
        print("*********Size of the window*********")
        print("width :", root.winfo_width())
        print("height :", root.winfo_height())
        print("******Coordinate of the window******")
        print("x :", root.winfo_x())
        print("y :", root.winfo_y())
        print("------------------------------------")

def debug(coord):
    print(f"--------{coord}, {old_play}---------------")
    for i in range(12):
        print(grid[i])


for i in range(12):
    grid[0][i] = 69
    grid[11][i] = 420
    grid[i][0] = 42
    grid[i][11] = 177013


for i in range(2, 11, 2):
    grid[1][i] = 1
    grid[3][i] = 1
    grid[9][i] = 2
    grid[7][i] = 2

for i in range(1, 11, 2):
    grid[2][i] = 1
    grid[4][i] = 1
    grid[10][i] = 2
    grid[8][i] = 2

def clean():
    for i in range(12):
        for j in range(12):
            if grid[i][j] == 3:
                grid[i][j] = 0
                button[(i, j)].config(image=img[0])

def winorloose():
    global whiter
    global blackr
    if whiter == 0:
        white.config(text="Desole mais\ntu as perdu")
        black.config(text="Bravo,\ntu as gagné")
    if blackr == 0:
        black.config(text="Desole mais\ntu as perdu")
        white.config(text="Bravo,\ntu as gagne")

def play(coord):
    global whiter
    global blackr
    global player_turn
    x, y = coord[0], coord[1]
    xx, yy = abs(coord[0] - old_play[0]), abs(coord[1] - old_play[1])
    xxx, yyy = (coord[0] + old_play[0])//2, (coord[1] + old_play[1])//2
    if (grid[x][y] != ((player_turn % 2)+1)) and (grid[x][y] != 3):
        return
    debug(coord)
    if grid[x][y] == 3:
        grid[x][y] = ((player_turn % 2) + 1)
        button[(x, y)].config(image=img[((player_turn % 2)+1)])
        button[(old_play[0]), (old_play[1])].config(image=img[0])
        player_turn += 1
        if abs(coord[0] - old_play[0]) == 1:
            grid[old_play[0]][old_play[1]] = 0

        elif xx == 2:
            if grid[xxx][yyy] == 1:
                whiter -= 1
                white.config(text=f"Pions blanc restant :\n{whiter}")
            if grid[xxx][yyy] == 2:
                blackr -= 1
                black.config(text=f"Pions noir restant :\n{blackr}")

            grid[xxx][yyy] = 0
            button[(xxx, yyy)].config(image=img[0])
        clean()
        winorloose()
        return

    clean()
    old_play[0], old_play[1] = x, y
    if ((player_turn % 2)+1) == 2:
        for i in [-1, 1]:
            if grid[x-1][y+i] == 0:
                grid[x-1][y+i] = 3
                button[(x-1, y+i)].config(image=img[3])
        for i in [-1, 1]:
            for j in [-1, 1]:

                if (grid[x+i][y+j] == 1) and (grid[x+i+i][y+j+j] == 0):
                    grid[x+i+i][y+j+j] = 3
                    button[(x+i+i, y+j+j)].config(image=img[3])

    if ((player_turn % 2) + 1) == 1:
        for i in [-1, 1]:
            if grid[x+1][y+i] == 0:
                grid[x+1][y+i] = 3
                button[(x+1, y+i)].config(image=img[3])
        for i in [-1, 1]:
            for j in [-1, 1]:

                if (grid[x+i][y+j] == 2) and (grid[x+i+i][y+j+j] == 0):
                    grid[x+i+i][y+j+j] = 3
                    button[(x+i+i, y+j+j)].config(image=img[3])


whiter = 1
blackr = 20


root = tkinter.Tk()
root.geometry("876x702")

img = {}
for i in range(6):
    img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

button = {}
for i in range(1, 11):
    for j in range(1, 11):
        button[(i, j)] = tkinter.Button(root, image=img[grid[i][j]], command = lambda coord=(i, j): play(coord))
        button[(i, j)].grid(row=i, column=j)
        button[(i, j)].bind("<Button-2>", dim)

white = tkinter.Label(text=f"Pions blanc restant :\n{whiter}", font=("Minecraft", 12))
black = tkinter.Label(text=f"Pions noir restant :\n{blackr}", font=("Minecraft", 12))

white.grid(column=11, row=1)
black.grid(column=11, row=7)


root.mainloop()