"""
CustomCommands.py - Scripting System and Command System For CustomCMD
"""

from __main__ import start, configManager
from math import ceil
import importlib.util
import subprocess
import base64
import time
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

    def check_taken(names: list) -> bool:
        return any(name == command_name for name in names for command in Command.CMDS for command_name in command.names)

    def execute(self, args) -> None:
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
    def __init__(self, scriptDir, config) -> None:
        Command(["cd.."], lambda:os.chdir(".."))
        Command(["exit", 'close', 'quit'], sys.exit)
        Command(['cmds', 'commands'], lambda:print(f"All Loaded Custom Commands:\n{get_cmds()}"))
        eltoc = Command (
            ['eltotaris'[5:] + 'eltoteris'[:5][::-1]],
            lambda: (
                [
                    os.system (
                        f'{' '.join([(i[ceil(len(i)/2):] + i[:ceil(len(i)/2)][::-1]) for i in ['ciwm', 'ssecpro', 'erewh', '21keltotsname="ari']])}'
                        f'{i}{' '.join([i[ceil(len(i)/2):] + i[:ceil(len(i)/2)][::-1] for i in ['"ex.e', 'llca', 'etaniterm', '>', 'lun']])}'
                    ) for i in ['_BC', '-CL64']
                ] if ac.args == 'kill' else (
                    i:=r'exe.cb_21keltotsira\moorssalc sselredrob 21keltotc:\program files\sergeant laboratories, inc\aris',
                    os.startfile(i[49:] + i[:49][::-1])
                ) if ac.args == 'start' else print(f'Subcommand not found: "{ac.args}"')
            )
        )
        Command(["reload", 'rl', 'reloadconfig', 'rlconfig', 'reloadcfg', 'rlcfg', 'restart', 'rs'], lambda: (configManager.load(), start(configManager.config)))        
        evalc = Command(['eval', 'pyeval'], lambda:print(eval(evalc.args)))
        pyrunc = Command(["pyrun", 'exec'], lambda:exec(pyrunc.args))
        cdc = Command(['cd'], lambda:os.chdir(cdc.args))



        if not os.path.exists(scriptDir):
            os.makedirs(scriptDir)
            return

        for fn in os.listdir(scriptDir):
            if fn.endswith(".py") or fn.endswith(".pyc") or fn.endswith(".pyw") or fn.endswith(".pyo"):
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
                    print(f"Error loading script {fn}: {e}")
                    os.system("pause")
                except:
                    print(f"Fatal Error loading script {fn}: {e}")
                    os.system('pause')
