import spade 
import asyncio
from konstante import SERVER
from repozitorij import getRoot, koordinate
import json

class InputHandler(spade.agent.Agent):
    class InputHandlerBehaviour(spade.behaviour.OneShotBehaviour):
        def left(self, event):
            for x in range(len(koordinate)):
                for y in range(len(koordinate)):
                    por = spade.message.Message(
                        to = f"gpucore_{x}_{y}@{SERVER}", 
                        body = json.dumps({
                            "coordinateIdx": 0,
                            "coordinateOffset": -10,
                        }), 
                        metadata = {
                            "performative": "inform",
                            "ontology": "movepixel",
                            "language": "json"
                        }
                    )
                    asyncio.run(self.send(por))
        def right(self, event):
            for x in range(len(koordinate)):
                for y in range(len(koordinate)):
                    por = spade.message.Message(
                        to = f"gpucore_{x}_{y}@{SERVER}", 
                        body = json.dumps({
                            "coordinateIdx": 0,
                            "coordinateOffset": 10,
                        }), 
                        metadata = {
                            "performative": "inform",
                            "ontology": "movepixel",
                            "language": "json",
                        }
                    )
                    asyncio.run(self.send(por))
        def up(self, event):
            for x in range(len(koordinate)):
                for y in range(len(koordinate)):
                    por = spade.message.Message(
                        to = f"gpucore_{x}_{y}@{SERVER}", 
                        body = json.dumps({
                            "coordinateIdx": 1,
                            "coordinateOffset": -10,
                        }), 
                        metadata = {
                            "performative": "inform",
                            "ontology": "movepixel",
                            "language": "json",
                        }
                    )
                    asyncio.run(self.send(por))
        def down(self, event):
            for x in range(len(koordinate)):
                for y in range(len(koordinate)):
                    por = spade.message.Message(
                        to = f"gpucore_{x}_{y}@{SERVER}", 
                        body = json.dumps({
                            "coordinateIdx": 1,
                            "coordinateOffset": 10,
                        }), 
                        metadata = {
                            "performative": "inform",
                            "ontology": "movepixel",
                            "language": "json",
                        }
                    )
                    asyncio.run(self.send(por))

        async def run(self):
            root = getRoot()
            root.bind("<Left>", self.left)
            root.bind("<Right>", self.right)
            root.bind("<Up>", self.up)
            root.bind("<Down>", self.down)

    async def setup(self):
        print("input handler started")
        self.add_behaviour(self.InputHandlerBehaviour())