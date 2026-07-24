import npc
import light




class npcHandler:
    def __init__(self):
        self.npc_list = []
        self.light_list = []
        

    def update(self,playerpos,A,pL,screen,pz):
        [npc.update(playerpos,A,pL,screen,pz) for npc in self.npc_list]
        [light.update(playerpos,A,pL,screen,pz) for light in self.light_list]
        self.npc_list = [npc for npc in self.npc_list if not npc.remove]
        

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_light(self, light):
        self.light_list.append(light)
        
    def raycast(self, px, py, wx1, wy1, wx2, wy2):
        [npc.raycast(px, py, wx1, wy1, wx2, wy2) for npc in self.npc_list]

    def lraycast(self, px, py, wx1, wy1, wx2, wy2):
            [light.raycast(px, py, wx1, wy1, wx2, wy2) for light in self.light_list]

