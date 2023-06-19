from konstante import SERVER
from repozitorij import koordinate, setRoot, getRoot, setCanvas, getCanvas, setRects
from inputhandler import InputHandler
from monitor import Monitor
from gpucore import GPUCore
import tkinter

setRoot(tkinter.Tk())
root = getRoot()
setCanvas(tkinter.Canvas(root))
canvas = getCanvas()
canvas.pack()

rect = [[None] * 3 for i in range(3)]

for x in range(len(koordinate)):
    for y in range(len(koordinate)):
        rect[x][y] = canvas.create_rectangle(koordinate[x][y][0], koordinate[x][y][1], koordinate[x][y][0] + 10, koordinate[x][y][1] + 10, fill="blue")

setRects(rect)

canvas.update()

gpuCore = [[None] * 3 for i in range(3)]
for x in range(len(koordinate)):
    for y in range(len(koordinate)):
        gpuCore[x][y] = GPUCore(f"gpucore_{x}_{y}@{SERVER}", f"gpucore_{x}_{y}")
        gpuCore[x][y].setCoreIndex(x, y) 
        gpuCore[x][y].start()

inputHandler = InputHandler(f"handler@{SERVER}", "handler")
inputHandler.start()

monitor = Monitor(f"monitor@{SERVER}", "monitor")
monitor.start()

root.mainloop()