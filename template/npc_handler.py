





class npcHandler:
    def __init__(self):
        self.npc_list = []
        

    def update(self):
        [npc.update() for npc in self.npc_list]
        

    def add_npc(self, npc):
        self.npc_list.append(npc)