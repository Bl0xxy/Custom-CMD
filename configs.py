### IMPORTS ###
import base64, json, sys, os, importlib.util
sys.path.append(os.getcwd())

### CONFIG SYSTEM ###
config = {"CTRL_C_EXIT": False, "STARTING_DIRECTORY": os.path.expanduser('~'), "START_MESSAGE": "Microsoft Windows [Version 10.0.19045.3570]\n(c) Microsoft Corporation. All rights reserved.\n", "PYTHON_INSTALL_PATH": "\""+sys.executable+"\"", "DEFAULT_COLOR": "07"}

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

load_config("config.json")

# Startup Function
def start() -> None:
    for cmd in ['cls', 'title Command Prompt', 'color ' + config["DEFAULT_COLOR"]]: os.system(cmd)
    os.chdir(config["STARTING_DIRECTORY"])
    print(config["START_MESSAGE"])

### MAIN ###

start()

while True:
    try:
        command, *args = input(f"{os.getcwd()}>").split(" ")
        
        if command == "start": start()
        elif command == "cd..": os.chdir('..')
        elif command == "cd": os.chdir(' '.join(args))
        elif command == "exit": sys.exit()
        else: os.system([command] + args)

    except Exception as e:
        try:
            print(f"Error: {e.args[1]}.  Please report it to the developer.")
            continue
        except:
            try:
                print(f"Unhandled Error: {e.args[1]}.  Please report it to the developer.")
            except SystemExit:
                sys.exit()
            except:
                print("Unhandled Error.  Please report it to the developer.")
    
    except KeyboardInterrupt:
        if config["CTRL_C_EXIT"]: raise SystemExit
        print()
        continue
