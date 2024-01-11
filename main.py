"""
CustomCMD dev-1.3
A replacement to Command Prompt with a scripting API, configuration system, and more!
"""

### IMPORTS ###
import base64, json, sys, os, importlib.util
sys.path.append(os.getcwd())

def start(config: dict) -> None:
    for cmd in ['cls', 'title Command Prompt', 'color ' + config["DEFAULT_COLOR"]]: os.system(cmd)
    os.chdir(config["STARTING_DIRECTORY"])
    print(config["START_MESSAGE"])

from CustomCommands import CommandManager, exec_cmd, Command
from ConfigManager import ConfigManager

### MAIN ###
configManager = ConfigManager("config.json")
scriptManager = CommandManager(os.path.join(os.getcwd(), "save", "scripts"), configManager.config)

config = configManager.config

start(config)

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
