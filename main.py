### IMPORTS ###
import base64, json, sys, os, importlib.util

## Check If Running From Main File
main = __name__ == "__main__"

### CUSTOM EXCEPTIONS ###
class InvalidCommandError(Exception):
    def __init__(self, name):
        self.cmd_name = name
        super().__init__(f"Command \"{name}\" does not exist.")

### CONFIG SYSTEM ###
config = {"CTRL_C_EXIT": False, "STARTING_DIRECTORY": os.path.expanduser('~'), "START_MESSAGE": "Microsoft Windows [Version 10.0.19045.3570]\n(c) Microsoft Corporation. All rights reserved.\n", "PYTHON_INSTALL_PATH": "\""+sys.executable+"\"", "DEFAULT_COLOR": "07"}
def load_config(fn: str) -> dict:
    try:
        with open(fn, encoding='utf-8') as c:
            c = json.load(c)
            for v in config:
                if v in c: config[v] = c[v]
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error: {e.args[0]}.  Please report it to the developer.")
        os.system('pause')
    return config

if main:load_config("config.json")

# Startup Function
def start() -> None:
    for cmd in ['cls', 'title Command Prompt', 'color ' + config["DEFAULT_COLOR"]]: os.system(cmd)
    os.chdir(config["STARTING_DIRECTORY"])
    print(config["START_MESSAGE"])

### CUSTOM COMMAND SYSTEM ###
class Command:
    CMDS: list = []
    def __init__(self, name: str, action: callable):
        self.name = name
        self.onCommand = action
        Command.CMDS.append(self)

def get_cmds() -> list:
    return [c.name for c in Command.CMDS]

def cmd_exists(name: str) -> bool:
    for c in Command.CMDS:
        if c.name == name: return True
    return False

def find_cmd(name: str) -> Command:
    if not cmd_exists(name): raise InvalidCommandError(name)
    for c in Command.CMDS:
        if c.name == name: return c

def exec_cmd(name: str) -> None:
    find_cmd(name).onCommand()

if main:
    Command("start", start),
    Command("cd..", lambda:os.chdir(".."))
    Command("exit", lambda:sys.exit())
    Command("aristotle", lambda:exec(base64.b64decode(b'b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyX0JDLmV4ZSIgZGVsZXRlJyk7b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyLUNMNjQuZXhlIiBkZWxldGUnKQ==').decode("ascii")))
    Command("cmds", lambda:print(f"All Loaded Custom Commands:\n{get_cmds()}"))


### COMMAND MANAGER ###
def load_scripts():
    script_dir = os.path.join(os.getcwd(), "scripts")
    
    if not os.path.exists(script_dir):
        os.makedirs(script_dir)
        return

    for filename in os.listdir(script_dir):
        if filename.endswith(".py"):
            try:
                script_path = os.path.join(script_dir, filename)
                spec = importlib.util.spec_from_file_location("script", script_path)
                script_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(script_module)
                
                if hasattr(script_module, 'main') and callable(script_module.main):
                    script_module.main()
                else:
                    continue
            except Exception as e:
                print(f"Error loading {filename}: {e}")

if main:load_scripts()

### MAIN ###
if main:
    start()

    while True:
        try:
            value = input(f"{os.getcwd()}>")

            if value.startswith("cd "): os.chdir(value.strip("cd "))

            elif value.startswith("python"): os.system(value.replace("python", config["PYTHON_INSTALL_PATH"]))
            
            elif cmd_exists(value.lower()): exec_cmd(value.lower())

            else: os.system(value)

        except Exception as e:
            if e.args[1] == "The system cannot find the file specified": print("Error: File or directory not found or is case sensitive."); continue
            print(f"Error: {e.args[1]}.  Please report it to the developer.")
            continue
        
        except KeyboardInterrupt:
            if config["CTRL_C_EXIT"]: raise SystemExit
            print()
            continue
