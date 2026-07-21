import npc





class npcHandler:
    def __init__(self):
        self.npc_list = []
        

    def update(self,playerpos,A,pL,screen,pz):
        [npc.update(playerpos,A,pL,screen,pz) for npc in self.npc_list]
        

    def add_npc(self, npc):
        self.npc_list.append(npc)
        
    def raycast(self, px, py, wx1, wy1, wx2, wy2):
        [npc.raycast(px, py, wx1, wy1, wx2, wy2) for npc in self.npc_list]