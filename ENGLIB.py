import re
import os


def updatename(name):
    fileS = f"{name}/settings.py" #change the name in the settings.py of the project

    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^NAME\s*=.*$",f"NAME = '{name}'",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)
        
def savemap(name,maplst,wallamount):
    fileS = f"{name}/map.py" #save the current map after making a wall

    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^wall_data\s*=.*$",f"wall_data = {maplst}",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)
        
    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^wallamount\s*=.*$",f"wallamount = {wallamount}",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)
        
def updatePlayerPos(name,pos):
    fileS = f"{name}/main.py" #change the players position

    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^playerStartPos\s*=.*$",f"playerStartPos = {pos}",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)
        
def updateDarkness(name,val):
    fileS = f"{name}/settings.py" #change the Darkness value

    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^DARK\s*=.*$",f"DARK = {val}",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)

'''def scriptCompliler(script): #might use this
    if script.endswith('.py'):
        pass

    elif script.endswith('.cy'):
        with open(script, 'r') as f:
            scriptlist = f.read().split()

        print(scriptlist)

        pyfile = os.path.splitext(script)[0] + '.py'

        with open(pyfile, 'w') as f:
            for i in range(len(scriptlist)):
                if scriptlist[i].startswith('*'):
                    continue

                if scriptlist[i] == 'Type':
                    if i + 1 < len(scriptlist) and scriptlist[i + 1] == 'NPC':
                        f.write('test')'''
            


#scriptCompliler("C:/Users/ethan/OneDrive/Desktop/Engine/CyberGameEngine/demo/scripts/enemy.cy")