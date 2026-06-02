import re



def updatename(name):
    fileS = f"{name}/settings.py" #change the name in the settings.py of the project

    with open(fileS, "r") as file:
        content = file.read()


    content = re.sub(r"^NAME\s*=.*$",f"NAME = '{name}'",content,flags=re.MULTILINE)

    with open(fileS, "w") as file:
        file.write(content)