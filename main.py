import tkinter

grid = [[0 for j in range(14)]for i in range(14)]

for i in range(14):
    grid[0][i] = 100
    grid[13][i] = 100
    grid[i][0] = 100
    grid[i][13] = 100


for i in range(2, 13, 2):
    grid[1][i] = 1
    grid[3][i] = 1
    grid[11][i] = 2
    grid[9][i] = 2

for i in range(1, 13, 2):
    grid[2][i] = 1
    grid[4][i] = 1
    grid[12][i] = 2
    grid[10][i] = 2

def play(coord):
    x, y = coord[0], coord[1]
    if grid[x][y] == 0:
        return
    if grid[x][y] == 1:
        return
    if grid[x][y] == 0:
        return




root = tkinter.Tk()
root.geometry("500x500")

button = {}
for i in range(1, 13):
    for j in range(1, 13):
        button[(i, j)] = tkinter.Button(root, text=f"{grid[i][j]}", command = lambda coord=(i, j): play(coord))
        button[(i, j)].grid(row=i, column=j, ipadx=5, ipady=1)

root.mainloop()










for i in range(14):
    print(grid[i])