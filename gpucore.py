import spade
from repozitorij import koordinate
import json

class GPUCore(spade.agent.Agent):
    class GPUCoreBehaviour(spade.behaviour.CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)
            if msg:
                if msg.get_metadata("ontology") == "movepixel":
                    request = json.loads(msg.body)
                    coordinateIdx = request['coordinateIdx']
                    coordinateOffset = request['coordinateOffset']
                    koordinate[self.agent.x][self.agent.y][coordinateIdx] += coordinateOffset
                    axis = "x" if coordinateIdx == 0 else "y"
                    print(f"GPU Core assigned to rect ({self.agent.x}, {self.agent.y}) moved the rect {coordinateOffset}px on {axis} axis")

    async def setup(self):
        print(f"Initialized GPU Core for position ({self.x}, {self.y})")
        self.add_behaviour(self.GPUCoreBehaviour())        

    def setCoreIndex(self, x, y):
        self.x = x
        self.y = y
