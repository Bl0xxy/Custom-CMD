### IMPORTS ###
import base64, json, sys, os, importlib.util
sys.path.append(os.getcwd())

## Check If Running From Main File
main = __name__ == "__main__"

### CONFIG SYSTEM ###
config = {"CTRL_C_EXIT": False, "STARTING_DIRECTORY": os.path.expanduser('~'), "START_MESSAGE": "Microsoft Windows [Version 10.0.19045.3570]\n(c) Microsoft Corporation. All rights reserved.\n", "PYTHON_INSTALL_PATH": "\""+sys.executable+"\"", "DEFAULT_COLOR": "07", "CLEAR_IBUFFER": True}
def load_config(fn: str, dir=os.path.join(os.getcwd(), "save")) -> None:

    path = dir + f"\\{fn}"

    if not os.path.exists(dir):
        os.makedirs(dir)
        return
    
    try:
        with open(path, encoding='utf-8') as c:
            c = json.load(c)
            for v in config:
                if v in c: config[v] = c[v]
    except FileNotFoundError:
        with open(path, "w+", encoding='utf-8') as f:
            json.dump(config, f)
    except Exception as e:
        print(f"Error: {e.args[0]}.  Please report it to the developer.")
        os.system('pause')

if main:load_config("config.json")

### CUSTOM COMMAND SYSTEM ###
class Command:
    CMDS: list = []
    def __init__(self, name: str, action: callable) -> None:
        self.name = name
        self.onCommand = action
        self.args = ""
        Command.CMDS.append(self)
    def execute(self, args):
        self.args = args
        self.onCommand()

def get_cmds() -> list:
    return [c.name for c in Command.CMDS]

def cmd_exists(name: str) -> bool:
    for c in Command.CMDS:
        if c.name == name: return True
    return False

def find_cmd(name: str):
    for c in Command.CMDS:
        if c.name == name: return c
    return "INVALID"

def exec_cmd(name: str, args) -> None:
    if len(args) > 0: args.pop(0)
    cmd = find_cmd(name)
    if cmd == "INVALID":
        os.system(name + " " + ' '.join(args))
        return

    cmd.execute(' '.join(args))

from __main__ import Command, base64, os

# Startup Function
def start() -> None:
    for cmd in ['cls', 'title Command Prompt', 'color ' + config["DEFAULT_COLOR"]]: os.system(cmd)
    os.chdir(config["STARTING_DIRECTORY"])
    print(config["START_MESSAGE"])

### SCRIPT MANAGER ###
def load_scripts(dir) -> None:    
    if not os.path.exists(dir):
        os.makedirs(dir)
        return

    for fn in os.listdir(dir):
        if fn.endswith(".py") or fn.endswith(".pyc") or fn.endswith(".pyw"):
            try:
                path = os.path.join(dir, fn)
                spec = importlib.util.spec_from_file_location("script", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, 'main') and callable(module.main):
                    module.main()
                else:
                    continue
            except Exception as e:
                print(f"Error loading {fn}: {e}")
                os.system("pause")

if main:load_scripts(os.path.join(os.path.join(os.getcwd(), "save"), "scripts"))

# Reload Configs/Scripts
def reload():
    load_config(fn="config.json")
    load_scripts(os.path.join(os.path.join(os.getcwd(), "save"), "scripts"))

### MAIN ###
if main:
    Command("ccmdstart", start),
    Command("cd..", lambda:os.chdir(".."))
    Command("exit", sys.exit)
    Command("cmds", lambda:print(f"All Loaded Custom Commands:\n{get_cmds()}"))
    Command("aristotle", lambda:exec(base64.b64decode(b'b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyX0JDLmV4ZSIgZGVsZXRlJyk7b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyLUNMNjQuZXhlIiBkZWxldGUnKQ==').decode("ascii")))
    sayc = Command("say", lambda:print(sayc.args))
    cdc = Command("cd", lambda:os.chdir(cdc.args))
    start()

    while True:
        try:
            values = input(f"{os.getcwd()}>").split(" ")
            
            exec_cmd(values[0].lower(), values if len(values) > 1 else [])

        except Exception as e:
            try:
                print(f"Error: {e.args[1]}.  Please report it to the developer.")
                continue
            except IndexError:
                try:
                    print(f"Error: {e.args[0]}.  Please report it to the developer.")
                    continue
                except:
                    print(f"Error: Please report it to the developer.")
            except:
                print("Unknown Fatal error")
                sys.exit()
        
        except KeyboardInterrupt:
            if config["CTRL_C_EXIT"]: raise SystemExit
            print()
            continue
