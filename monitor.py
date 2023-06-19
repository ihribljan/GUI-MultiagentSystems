import spade
from repozitorij import koordinate, getCanvas, getRects

class Monitor(spade.agent.Agent):
    class MonitorBehaviour(spade.behaviour.PeriodicBehaviour):
        async def run(self): 
            canvas = getCanvas()
            rects = getRects()
            for x in range(len(koordinate)):
                for y in range(len(koordinate)):
                    canvas.moveto(rects[x][y], koordinate[x][y][0], koordinate[x][y][1])

    async def setup(self):
        self.add_behaviour(self.MonitorBehaviour(period=0.2))
