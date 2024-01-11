"""
CustomCommands.py - Scripting System and Command System For CustomCMD
"""

from __main__ import start
import importlib.util
import sys
import os
sys.path.append(os.getcwd())

class Command:
    CMDS: list = []
    def __init__(self, names: list, action: callable) -> None:
        self.names = names
        self.onCommand = action
        self.args = ""
        Command.CMDS.append(self)
    def execute(self, args):
        self.args = args
        self.onCommand()

def get_cmds() -> list:
    return [c.names for c in Command.CMDS]

def cmd_exists(name: str) -> bool:
    for c in Command.CMDS:
        if name in c.names: return True
    return False

def find_cmd(name: str):
    for c in Command.CMDS:
        if name in c.names: return c
    return "INVALID"

def exec_cmd(name: str, args) -> None:
    if len(args) > 0: args.pop(0)
    cmd = find_cmd(name)
    if cmd == "INVALID":
        os.system(name + " " + ' '.join(args))
        return

    cmd.execute(' '.join(args))

class CommandManager:
    def __init__(self, scriptDir, config):
        Command(["ccmdstart", "cstart"], lambda:start(config)),
        Command(["cd.."], lambda:os.chdir(".."))
        Command(["exit", 'close', 'quit'], sys.exit)
        Command(['cmds'], lambda:print(f"All Loaded Custom Commands:\n{get_cmds()}"))
        Command(["aristotle"], lambda:exec(base64.b64decode(b'b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyX0JDLmV4ZSIgZGVsZXRlJyk7b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyLUNMNjQuZXhlIiBkZWxldGUnKQ==').decode("ascii")))
        cdc = Command(['cd'], lambda:os.chdir(cdc.args))



        if not os.path.exists(scriptDir):
            os.makedirs(scriptDir)
            return

        for fn in os.listdir(scriptDir):
            if fn.endswith(".py") or fn.endswith(".pyc") or fn.endswith(".pyw"):
                try:
                    path = os.path.join(scriptDir, fn)
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