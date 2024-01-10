### IMPORTS ###
import base64, json, sys, os, importlib.util
sys.path.append(os.getcwd())

## Check If Running From Main File
main = __name__ == "__main__"

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

# Startup Function
def start() -> None:
    for cmd in ['cls', 'title Command Prompt']: os.system(cmd)

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

### MAIN ###
if main:
    Command("start", start),
    Command("cd..", lambda:os.chdir(".."))
    Command("exit", sys.exit)
    Command("cmds", lambda:print(f"All Loaded Custom Commands:\n{get_cmds()}"))
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
            print()
            continue
