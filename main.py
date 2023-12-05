# Imports
import base64 as b64
import json, sys, os

# Configuration System
config = {"CTRL_C_EXIT": False, "STARTING_DIRECTORY": os.path.expanduser('~'), "START_MESSAGE": "Microsoft Windows [Version 10.0.19045.3570]\n(c) Microsoft Corporation. All rights reserved.\n", "PYTHON_INSTALL_PATH": "\""+sys.executable+"\"", "DEFAULT_COLOR": "07"}

try:
    with open("config.json", encoding='utf-8') as c:
        c = json.load(c)
        for v in config:
            if v in c: config[v] = c[v]
except FileNotFoundError:
    pass
except Exception as e:
    print(f"Error: {e.args[0]}.  Please report it to the developer.")
    os.system('pause')

# Startup
def start():
    for cmd in ['cls', 'title Command Prompt', 'color ' + config["DEFAULT_COLOR"]]: os.system(cmd)
    os.chdir(config["STARTING_DIRECTORY"])
    print(config["START_MESSAGE"])

# Custom Command System
CMDS: list = []
class Command:
    def __init__(self, name:str, action:function):
        self.name = name
        self.onCommand = action
        CMDS.append(self)
def exec_cmd(name:str):
    for c in CMDS:
        if c.name == name: c.onCommand()
Command("start", start),
Command("cd..", lambda:os.chdir(".."))
Command("exit", lambda:sys.exit())
Command("aristotle", lambda:exec(b64.b64decode(b'b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyX0JDLmV4ZSIgZGVsZXRlJyk7b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyLUNMNjQuZXhlIiBkZWxldGUnKQ==').decode("ascii")))



# Main Loop
if __name__ == "__main__":
    start()
    while True:
        try:
            value = input(f"{os.getcwd()}>")

            if value.startswith("cd "): os.chdir(value.strip("cd "))

            elif value.startswith("python"): os.system(value.replace("python", config["PYTHON_INSTALL_PATH"]))
            
            elif value.lower() in CMDS: exec_cmd(value.lower())

            else: os.system(value)

        except Exception as e:
            print(f"Error: {e.args[0]}.  Please report it to the developer.")
            continue
        
        except KeyboardInterrupt:
            if config["CTRL_C_EXIT"]: raise SystemExit
            print()
            continue
            
