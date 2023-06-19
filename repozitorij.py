koordinate = [None] * 3
for x in range(len(koordinate)):
    koordinate[x] = [None] * 3
    for y in range(len(koordinate)):
        koordinate[x][y] = [10 * (x + 1), 10 * (y + 1)]

root = None
canvas = None
rects = None

def setRoot(newroot):
    global root
    root = newroot

def getRoot():
    return root

def setCanvas(newcanvas):
    global canvas
    canvas = newcanvas

def getCanvas():
    return canvas

def setRects(newrects):
    global rects
    rects = newrects

def getRects():
    return rects