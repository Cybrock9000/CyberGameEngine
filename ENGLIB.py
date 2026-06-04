import re



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