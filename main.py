import tkinter
long = 10
grid = [[0 for j in range(12)]for i in range(12)]
player_turn = 0
old_play = [0, 0]

def debug(coord):
    print(f"--------{coord}---------------")
    for i in range(12):
        print(grid[i])


for i in range(12):
    grid[0][i] = 100
    grid[11][i] = 100
    grid[i][0] = 100
    grid[i][11] = 100


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
                button[(i, j)].config(text = 0)

def play(coord):
    global player_turn
    x, y = coord[0], coord[1]
    if (grid[x][y] != ((player_turn % 2)+1)) and (grid[x][y] != 3):
        return
    debug(coord)
    if grid[x][y] == 3:
        grid[x][y] = ((player_turn % 2)+1)
        button[(x, y)].config(text=((player_turn % 2)+1))
        grid[old_play[0]][old_play[1]] = 0
        button[(old_play[0]), (old_play[1])].config(text=0)
        player_turn += 1
        clean()
        return
    clean()
    old_play[0], old_play[1] = x, y
    if ((player_turn % 2)+1) == 2:
        for i in [-1, 1]:
            if grid[x-1][y+i] == 0:
                grid[x-1][y+i] = 3
                button[(x-1, y+i)].config(text="3")
    if ((player_turn % 2) + 1) == 1:
        for i in [-1, 1]:
            if grid[x+1][y+i] == 0:
                grid[x+1][y+i] = 3
                button[(x+1, y+i)].config(text="3")







root = tkinter.Tk()
root.geometry("500x500")

button = {}
for i in range(1, 11):
    for j in range(1, 11):
        button[(i, j)] = tkinter.Button(root, text=f"{grid[i][j]}", command = lambda coord=(i, j): play(coord))
        button[(i, j)].grid(row=i, column=j, ipadx=5, ipady=1)

root.mainloop()









