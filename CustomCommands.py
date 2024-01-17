"""
CustomCommands.py - Scripting System and Command System For CustomCMD
"""

from __main__ import start
import importlib.util
import subprocess
import base64
import sys
import os
sys.path.append(os.getcwd())

class CommandOverrideError(Exception):
    def __init__(self, message="Command Cannot Be Overriden"):
        self.message = message

        super().__init__(self.message)

class Command:
    CMDS: list = []
    def __init__(self, names: list, action: callable) -> None:
        self.names = names
        self.onCommand = action
        self.args = ""
        
        if Command.check_taken(self.names):
            self.names = ["command-" + str(len(Command.CMDS))]
            raise CommandOverrideError(f"Command name \"{names[0]}\" is taken!  Default command name generated: {self.names[0]}")
        
        Command.CMDS.append(self)

    def check_taken(names: list):
        for name in names:
            for command in Command.CMDS:
                for command_name in command.names:
                    if name == command_name:
                        return True

        return False

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
        Command(["cd.."], lambda:os.chdir(".."))
        Command(["exit", 'close', 'quit'], sys.exit)
        Command(['cmds'], lambda:print(f"All Loaded Custom Commands:\n{get_cmds()}"))
        Command(["aristotle"], lambda: ([os.system("wmic process where name=\"AristotleK12" + i + ".exe\" call terminate") for i in ['_BC', '-CL64']]))
        Command(["reload", 'rl', 'reloadconfig', 'rlconfig', 'reloadcfg', 'rlcfg', 'restart'], lambda: (configManager.load(), start(configManager.config)))
        pyrunc = Command(["pyrun"], lambda:exec(command.args))
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
                    print(f"Error loading {fn}: {e.message}")
                    os.system("pause")
                except:
                    print(f"Fatal Error loading {fn}: {e.message}")
